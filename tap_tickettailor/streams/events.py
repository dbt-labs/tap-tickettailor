from tap_tickettailor.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class EventsStream(BaseStream):
    API_METHOD = 'events'
    TABLE = 'events'
    KEY_PROPERTIES = ['id']

    def response_key(self):
        return 'data'
