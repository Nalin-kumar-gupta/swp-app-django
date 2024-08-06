# BUILD
docker-compose -f local.yml build --no-cache

# RUN
docker-compose -f local.yml up

# migrations 
docker-compose -f local.yml run web python manage.py makemigrations
docker-compose -f local.yml run web python manage.py migrate

# create super user
docker-compose -f local.yml run web python manage.py createsuperuser

# create data
docker-compose -f local.yml run web python manage.py populate_inventory

# Package Viewset
List Packages: GET /api/packages/
Retrieve a Package: GET /api/packages/{id}/
Create a Package: POST /api/packages/
Update a Package: PUT /api/packages/{id}/ or PATCH /packages/{id}/
Delete a Package: DELETE /api/packages/{id}/

# Truck Viewset 
List Trucks: GET /api/trucks/
Retrieve a Truck: GET /api/trucks/{id}/
Create a Truck: POST /api/trucks/
Update a Truck: PUT /api/trucks/{id}/ or PATCH /trucks/{id}/
Delete a Truck: DELETE /api/trucks/{id}/