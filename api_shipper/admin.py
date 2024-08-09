from django.contrib import admin, messages
from django.http.request import HttpRequest
from .models import Truck, Package, Approval
from django.urls import path, reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import requests


# Register your models here.
admin.site.register(Truck)
admin.site.register(Package)



from django.contrib import admin
from django.utils.html import format_html
from .models import Approval

from django.contrib import admin
from django.utils.html import format_html
from .models import Approval

class ApprovalAdmin(admin.ModelAdmin):
    list_display = ('id', 'approval_truck', 'visualization_link', 'status')
    readonly_fields = ('id', 'approval_truck', 'visualization_link', 'packages', 'status')
    actions = ['approve_selected', 'reject_selected']

    def visualization_link(self, obj):
        if obj.link:
            return format_html('<a href="{0}" target="_blank">Visualization</a>', obj.link)
        return 'No link'

    visualization_link.short_description = 'Link'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object exists, make all fields readonly
            return self.readonly_fields
        return self.readonly_fields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # Include the clickable link in the change view template context
        extra_context['visualization_link'] = self.visualization_link(self.get_object(request, object_id))
        extra_context['show_save_and_add_another'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


    def approve_selected(self, request, queryset):
        # Filter queryset to only include items that are pending
        pending_approvals = queryset.filter(status='pending')

        for approval in pending_approvals:
            try:
                # Post request to API
                response = requests.post(
                    'http://localhost:8000/api/visualize-packages/',
                    json={'truck_id': str(approval.approval_truck.id)}
                )
                print(response.json())

                if response.ok:
                    allocated_boxes = response.json().get('mark_boxes')  # Assuming API returns a list of box IDs
                    print("123456", response.json())

                    for box_id in allocated_boxes:
                        try:
                            package = Package.objects.get(name=box_id, destination=approval.approval_truck.destination)
                            package.status = "allocated"
                            package.allocation = approval.approval_truck.model_name
                            package.save()  # Don't forget to save the changes
                        except Package.DoesNotExist:
                            print(f"Package with name {box_id} and destination {approval.approval_truck.destination} does not exist.")
                else:
                    self.message_user(request, f"Failed to get allocated boxes for truck {approval.approval_truck.id}.", level=messages.ERROR)
                    continue

            except requests.RequestException as e:
                self.message_user(request, f"Error occurred while communicating with the API: {str(e)}", level=messages.ERROR)
                continue

            # Update the status to approved
            approval.status = 'approved'
            approval.save()

        # Provide feedback to the user
        updated_count = pending_approvals.count()
        if updated_count:
            self.message_user(request, f'{updated_count} approvals have been approved.')
        else:
            self.message_user(request, 'No pending approvals selected or all selected items are already processed.', level=messages.ERROR)

    approve_selected.short_description = 'Approve selected approvals'



    def reject_selected(self, request, queryset):
        # Filter queryset to only include items that are pending
        pending_approvals = queryset.filter(status='pending')
        
        # Update the status to rejected
        updated_count = pending_approvals.update(status='rejected')
        
        # Provide feedback to the user
        if updated_count:
            self.message_user(request, f'{updated_count} approvals have been rejected.')
        else:
            self.message_user(request, 'No pending approvals selected or all selected items are already processed.', level=messages.ERROR)

    reject_selected.short_description = 'Reject selected approvals'

admin.site.register(Approval, ApprovalAdmin)

