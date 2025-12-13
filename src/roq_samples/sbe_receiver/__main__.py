#!/usr/bin/env python

"""
Copyright (c) 2017-2026, Hans Erik Thrane
"""

from . import Receiver

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="SBE Receiver (TEST)",
        description="Demonstrates how to decode a SBE multicast feed using asyncio",
    )

    parser.add_argument(
        "--loglevel",
        type=str,
        required=False,
        default="info",
        help="logging level",
    )

    parser.add_argument(
        "--local_interface",
        type=str,
        required=True,
        help="ipv4 address of a network interface",
    )
    parser.add_argument(
        "--multicast_snapshot_address",
        type=str,
        required=False,
        help="ipv4 address of a multicast group",
    )
    parser.add_argument(
        "--multicast_snapshot_port",
        type=int,
        required=True,
        help="multicast port",
    )
    parser.add_argument(
        "--multicast_incremental_address",
        type=str,
        required=False,
        help="ipv4 address of a multicast group",
    )
    parser.add_argument(
        "--multicast_incremental_port",
        type=int,
        required=True,
        help="multicast port",
    )

    args = parser.parse_args()

    import logging

    logging.basicConfig(level=args.loglevel.upper())

    del args.loglevel

    Receiver.main(**vars(args))
