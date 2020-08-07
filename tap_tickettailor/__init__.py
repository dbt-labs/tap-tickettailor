#!/usr/bin/env python3

import singer

import tap_framework

from tap_tickettailor.client import TicketTailorClient
from tap_tickettailor.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class TicketTailorRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=["token"])
    client = TicketTailorClient(args.config)
    runner = TicketTailorRunner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == "__main__":
    main()
