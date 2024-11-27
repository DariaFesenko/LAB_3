import base64
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class NetworkHelper:
    def __init__(self, base_url_1, base_url_2, username, password):
        self.base_url_1 = base_url_1
        self.base_url_2 = base_url_2
        auth_string = f"{username}:{password}"
        self.encoded_auth = base64.b64encode(auth_string.encode()).decode()
        self.headers = {"Authorization": f"Basic {self.encoded_auth}"}

    def _get_url(self, api_id):
        if api_id == 1:
            return self.base_url_1
        elif api_id == 2:
            return self.base_url_2
        else:
            raise ValueError("Invalid API ID")

    def get_list(self, api_id):
        url = self._get_url(api_id)
        print(f"URL: {url}")
        print(f"Headers: {self.headers}")
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Помилка при запиті: {response.status_code}")
            print(response.text)

    def get_item_by_id(self, api_id, item_id):
        url = f"{self._get_url(api_id)}{item_id}/"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Помилка при запиті: {response.status_code}")
            print(response.text)

    def create_item(self, api_id, data):
        url = self._get_url(api_id)
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Помилка при запиті: {response.status_code}")
            print(response.text)

    def update_item_by_id(self, api_id, item_id, data):
        url = f"{self._get_url(api_id)}{item_id}/"
        response = requests.put(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Помилка при запиті: {response.status_code}")
            print(response.text)

    def delete_item_by_id(self, api_id, item_id):
        url = f"{self._get_url(api_id)}{item_id}/"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            return {"message": "Item deleted successfully"}
        else:
            print(f"Помилка при запиті: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    helper = NetworkHelper(
        base_url_1='http://127.0.0.1:8001/api/agents/',
        base_url_2='http://127.0.0.1:8001/api/clients/',
        username="acer",
        password="004344668"
    )

    print("Отримуємо список агентів:")
    agents = helper.get_list(api_id=1)
    print(agents)

    print("Отримуємо агента за ID:")
    agent = helper.get_item_by_id(api_id=1, item_id=1)
    print(agent)

    print("Створюємо нового агента:")
    new_agent = {"name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "+1-555-789-1234"}
    created_agent = helper.create_item(api_id=1, data=new_agent)
    print(created_agent)

    print("Оновлюємо агента:")
    updated_data = {"name": "John Doe Updated", "email": "sophie.dupont@example.fr", "phone": "+33-1-2345-6789"}
    updated_agent = helper.update_item_by_id(api_id=1, item_id=1, data=updated_data)
    print(updated_agent)

    print("\nОтримуємо список клієнтів:")
    clients = helper.get_list(api_id=2)
    print(clients)

    print("Отримуємо клієнта за ID:")
    client = helper.get_item_by_id(api_id=2, item_id=1)
    print(client)

    print("Створюємо нового клієнта:")
    new_client = {"name": "Michael Smith", "email": "michael.smith@example.com", "phone": "+1-444-123-4567"}
    created_client = helper.create_item(api_id=2, data=new_client)
    print(created_client)

    print("Оновлюємо клієнта:")
    updated_client_data = {"name": "Michael Smith Updated", "email": "michael.smith.updated@example.com", "phone": "+1-444-765-4321"}
    updated_client = helper.update_item_by_id(api_id=2, item_id=1, data=updated_client_data)
    print(updated_client)