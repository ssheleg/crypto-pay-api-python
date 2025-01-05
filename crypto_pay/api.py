import requests
from urllib.parse import urlencode

class Api:
    """
    API client for CryptoPay.
    """

    default_api_options = {
        'protocol': 'https',
        'hostname': 'pay.crypt.bot',
    }

    def __init__(self, token, options=None):
        """
        Initialize the API client.

        :param token: Your API token
        :param options: Optional API options
        """
        self.token = token
        self.options = {**self.default_api_options, **(options or {})}
        if 'hostname' in self.options:
            self.options['hostname'] = self.options['hostname'].split('://')[-1]

    def build_request(self, method, params=None):
        """
        Build the API request URL and headers.

        :param method: API method name
        :param params: Parameters for the API method
        :return: Tuple of (url, headers)
        """
        params = {k: v for k, v in (params or {}).items() if v not in [None, '', []]}
        query_string = urlencode(params)
        url = f"{self.options['protocol']}://{self.options['hostname']}/api/{method}?{query_string}"
        headers = {'Crypto-Pay-API-Token': self.token}
        return url, headers

    def make_request(self, url, headers):
        """
        Make the API request and return the result.

        :param url: Request URL
        :param headers: Request headers
        :return: API response result
        """
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            if not data.get('ok'):
                raise Exception(f"API call failed: {data.get('error', 'Unknown error')}")
            return data['result']
        except requests.RequestException as e:
            raise Exception(f"HTTP request failed: {str(e)}")

    def call_api(self, method, params=None):
        """
        Call the specified API method.

        :param method: API method name
        :param params: Parameters for the API method
        :return: API response result
        """
        url, headers = self.build_request(method, params)
        return self.make_request(url, headers)