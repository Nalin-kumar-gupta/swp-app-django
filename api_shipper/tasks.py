from celery import shared_task
import requests

@shared_task
def call_visualizer_microservice(data_to_send):
    external_server_url = 'http://swp_visualizer:8081/process/'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url=external_server_url, headers=headers, json=data_to_send)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}