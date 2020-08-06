import time
import requests
import singer
import zlib
import json
import base64


from tap_framework.client import BaseClient
from requests.auth import HTTPBasicAuth


LOGGER = singer.get_logger()

API_ENDPOINT = 'https://api.tickettailor.com'


class TicketTailorClient(BaseClient):

    def __init__(self, config):
        super().__init__(config)

        self.user_agent = self.config.get('user_agent')
        self.token = self.config.get('token')

    def get_authorization(self):
        pass

    def make_request(self, url, method, params, base_backoff=45, body=None):
        LOGGER.info("Making {} request to {}".format(method, url))

        headers = {}

        if self.user_agent:
            headers['User-Agent'] = self.user_agent

        response = requests.request(
            method,
            url,
            params=params,
            auth=HTTPBasicAuth(self.token, '')
        )

        LOGGER.info("Received response ({}) from server".format(response.status_code))

        if response.status_code in [429, 504]:
            LOGGER.info('Got a 429, sleeping for {} seconds and trying again'
                        .format(base_backoff))
            time.sleep(base_backoff)
            return self.public_fetch(url, method, params, base_backoff * 2)

        if response.status_code == 404:
            LOGGER.info('Got a 404, no data is available')
            return None

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()
