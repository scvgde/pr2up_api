import requests
import json


class Power2Up:
    """Класс Power2Up"""

    def __init__(self, api_token):
        """Конструктор"""

        self.api_token = api_token
        self.base_url = "https://pr2up.com/api/v2?action="

    def get_services(self):
        """Получение всех сервисов"""
        api_url = "{}services&key={}".format(self.base_url, self.api_token)
        res = requests.get(api_url)
        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            error = res.json()['error']

            raise Exception(error)

    def create_order(self, service_id, link, quantity):
        """Создание заказа"""
        api_url = "{}add&service={}&link={}&quantity={}&key={}".format(self.base_url, service_id, link, quantity, self.api_token)

        res = requests.get(api_url)

        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            error = res.json()['error']
            if error == "unauthorized":
                raise "Invalid API Token"
            else:
                return res.json()

    def check_status(self, order_id):
        """Проверка статуса заказа"""
        api_url = f"{self.base_url}status&order={order_id}&key={self.api_token}"

        res = requests.get(api_url)

        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            try:
                error = res.json()['error']
            except:
                return {'error': 'Order not found'}
            else:
                if error == "unauthorized":
                    raise "Invalid API Token"
                else:
                    return res.json()

    def create_refill(self, order_id):
        """Создание рефилла"""
        api_url = f"{self.base_url}refill&order={order_id}&key={self.api_token}"

        res = requests.get(api_url)

        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            try:
                error = res.json()['error']
            except:
                return {'error': 'Order not found'}
            else:
                if error == "unauthorized":
                    raise "Invalid API Token"
                else:
                    return res.json()

    def get_balance(self):
        """Получение баланса"""
        api_url = f"{self.base_url}balance&key={self.api_token}"

        res = requests.get(api_url)

        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            error = res.json()['error']
            if error == "unauthorized":
                raise "Invalid API Token"
            else:
                return res.json()

    def cancel_order(self, order_id):
        """Отмена заказа"""
        api_url = f"{self.base_url}cancel&order={order_id}&key={self.api_token}"

        res = requests.get(api_url)

        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            try:
                error = res.json()['error']
            except:
                return {'error': 'Order not found'}
            else:
                if error == "unauthorized":
                    raise "Invalid API Token"
                else:
                    return res.json()