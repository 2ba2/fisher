import requests


class HTTP:
    # 经典类和新式类
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


class Http(object):
    def __init__(self, url):
        self.url = url

    @staticmethod
    def get(url, json_return=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if json_return else ''
        return r.json() if json_return else r.text
