#!/usr/bin/env python

"""
Copyright (c) 2017-2026, Hans Erik Thrane
"""

from . import Strategy

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Strategy (TEST)",
        description="Demonstrates how to implement a client",
    )

    parser.add_argument(
        "--loglevel",
        type=str,
        required=False,
        default="info",
        help="logging level",
    )

    parser.add_argument("connections", metavar="N", type=str, nargs="+", help="connections")

    args = parser.parse_args()

    import logging

    logging.basicConfig(level=args.loglevel.upper())

    del args.loglevel

    logger = logging.getLogger("main")

    import sys
    import roq

    def log_handler(level, message):
        """log handler"""
        if level == roq.logging.Level.DEBUG:
            logger.debug(message)
        elif level == roq.logging.Level.INFO:
            logger.info(message)
        elif level == roq.logging.Level.WARNING:
            logger.warning(message)
        elif level == roq.logging.Level.ERROR:
            logger.error(message)
        elif level == roq.logging.Level.CRITICAL:
            logger.critical(message)
        else:
            sys.exit()

    roq.logging.set_handler(log_handler)

    Strategy.main(args.connections)
