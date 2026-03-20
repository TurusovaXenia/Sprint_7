import requests


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, url):
        return self.session.get(self.base_url + url)

    def post(self, url, payload):
        return self.session.post(self.base_url + url, data=payload)

    def delete(self, url):
        return self.session.delete(self.base_url + url)
