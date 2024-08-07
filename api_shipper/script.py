import json
import sys
import requests

def main(data):
    # Parse JSON data
    try:
        data = json.loads(data)
        truck = data['truck']
        boxes = data['boxes']
        
        # Print or process data
        print(f"Truck Data: {truck}")
        print(f"Boxes Data: {boxes}")

        url = 'http://localhost:8081/process'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json=data)
        print("Status Code:", response.status_code)
        print("Response Body:", response.json()) 

        
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    except requests.RequestException as e:
        print("Request failed:", str(e))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data_to_send = sys.argv[1]
        main(data_to_send)
    else:
        print("No data provided")

