
from tap_tickettailor.streams.events import EventsStream
from tap_tickettailor.streams.issued_tickets import IssuedTicketsStream
from tap_tickettailor.streams.orders import OrdersStream


AVAILABLE_STREAMS = [
   EventsStream,
   IssuedTicketsStream,
   OrdersStream,
]

__all__ = [
   'EventsStream',
   'IssuedTicketsStream',
   'OrdersStream',
]
