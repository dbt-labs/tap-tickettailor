import singer
import singer.utils
import singer.metrics

from tap_tickettailor.state import incorporate, save_state

from tap_framework.streams import BaseStream as base
from tap_tickettailor.cache import stream_cache


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']
    CACHE = False

    def get_params(self):
        return {}

    def sync_paginated(self, params):
        table = self.TABLE

        while True:
            response = self.client.make_request(self.API_METHOD, params)
            transformed = self.get_stream_data(response)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))

            if self.CACHE:
                stream_cache[table].extend(transformed)

            meta = response.get('response_metadata', {})
            next_cursor = meta.get('next_cursor', '')

            if len(next_cursor) > 0:
                params['cursor'] = next_cursor
            else:
                break

    def sync_data(self):
        table = self.TABLE
        LOGGER.info('Syncing data for {}'.format(table))
        params = self.get_params()
        self.sync_paginated(params)

        return self.state

    def get_stream_data(self, response):
        transformed = []

        for record in response[self.response_key()]:
            record = self.transform_record(record)
            transformed.append(record)

        return transformed
