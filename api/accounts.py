import requests
from .base import Base


class Accounts(Base):

    def __init__(self):
        self.headers = {"Authorization": "Token {}".format(self.get_config()['apikey'])}
        self.base_url = self.get_config()['baseurl'].replace('"', '')

    def request_get_accounts(self, params=None):
        url = self.base_url +'/v3/a.json'

        return requests.get(url=url, headers=self.headers, params=params)

    def get_accounts(self, params=None):
        response = self.request_get_accounts(params=params)
        return response.json()
