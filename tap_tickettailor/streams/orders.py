from tap_tickettailor.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class OrdersStream(BaseStream):
    API_METHOD = 'orders'
    TABLE = 'orders'
    KEY_PROPERTIES = ['id']

    def response_key(self):
        return 'data'
