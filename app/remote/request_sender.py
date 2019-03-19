import requests


class RequestSender():


    def send_request(self, url, request_body, threshold, min_month, max_month):
        payload = {'threshold': threshold, 'minMonth': min_month, 'maxMonth': max_month}

        headers = {'Content-Type': 'application/json'}

        r = requests.post(url, json=request_body, params=payload, headers=headers)
        return r.json()

    def send_request_with_future_datapath(self, url, request_body):
        headers = {'Content-Type': 'application/json'}
        requests.post(url, json=request_body, headers=headers)