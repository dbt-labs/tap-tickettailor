from tap_tickettailor.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class IssuedTicketsStream(BaseStream):
    API_METHOD = 'issued_tickets'
    TABLE = 'issued_tickets'
    KEY_PROPERTIES = ['id']

    def response_key(self):
        return 'data'
