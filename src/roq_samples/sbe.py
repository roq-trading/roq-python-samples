#!/usr/bin/env python

"""
Copyright (c) 2017-2025, Hans Erik Thrane

Demonstrates SBE message encoding/decoding
"""

from datetime import datetime, timedelta

from fastcore.all import typedispatch

import roq

message = (
    b"\x7c\x02"
    b"\x14\x05"
    b"\x01\x00"
    b"\x01\x00"
    b"\x64\x65\x72\x69\x62\x69\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x7b\x00\x00\x00\x00\x00\x00\x00\xc8\x01\x00\x00\x00\x00\x00\x00"
    b"\x7b\x00\x00\x00\x00\x00\x00\x00"
    b"\x7b\x00\x00\x00\x00\x00\x00\x00"
    b"\x01"
    b"\x01\x00"
    b"\x64\x65\x72\x69\x62\x69\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x42\x54\x43\x2d\x50\x45\x52\x50\x45\x54\x55\x41\x4c\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x41\x62\x63\x44\x65\x66\x31\x32\x33\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x04"
    b"\x30\x31\x32\x33\x34\x35"
    b"\x42\x54\x43\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x55\x53\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x42\x54\x43\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x55\x53\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x55\x53\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x9a\x99\x99\x99\x99\x99\xa9\x3f"
    b"\x00\x00\x00\x00\x00\x00\x24\x40"
    b"\x00\x00\x00\x00\x00\x00\xf0\x3f"
    b"\x00\x00\x00\x00\x00\x00\xf0\x3f"
    b"\x00\x00\x00\x00\x00\x38\x8f\x40"
    b"\x00\x00\x00\x00\x00\x00\xf0\x3f"
    b"\x01"
    b"\x55\x53\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x9a\x99\x99\x99\x99\xd9\x5e\x40"
    b"\x42\x54\x43\x2d\x49\x4e\x44\x45\x58\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x47\x4d\x54\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\xd2\x04\x00\x00"
    b"\x29\x09\x00\x00"
    b"\x80\x0d\x00\x00"
    b"\xd7\x11\x00\x00"
    b"\x00\x4c\x2c\x03\x2a\x05\x00\x00"
    b"\x94\x26\x00\x00\x00\x00\x00\x00"
    b"\x00\xf2\xee\xaf\x2c\x06\x00\x00"
    b"\x01"
    b"\x10\x00"
    b"\x02\x00"
    b"\x00\x00\x00\x00\x00\x00\x24\x40"
    b"\x7b\x14\xae\x47\xe1\x7a\x84\x3f"
    b"\x00\x00\x00\x00\x00\x00\x59\x40"
    b"\x9a\x99\x99\x99\x99\x99\xa9\x3f"
)

print(len(message))
print(message)


@typedispatch
def callback(message_info: roq.MessageInfo, reference_data: roq.ReferenceData):
    print("reference_data={}, message_info={}".format(reference_data, message_info))

    encoder = roq.codec.Encoder(roq.codec.Type.SBE)
    message_2 = encoder.encode(message_info, reference_data)
    print(len(message_2))
    print(message_2)
    print(message == message_2)


@typedispatch
def callback(message_info: roq.MessageInfo, market_status: roq.MarketStatus):
    print("market_status={}, message_info={}".format(market_status, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, top_of_book: roq.TopOfBook):
    print("top_of_book={}, message_info={}".format(top_of_book, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, market_by_price_update: roq.MarketByPriceUpdate):
    print("market_by_price_update={}, message_info={}".format(market_by_price_update, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, market_by_order_update: roq.MarketByOrderUpdate):
    print("market_by_order_update={}, message_info={}".format(market_by_order_update, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, trade_summary: roq.TradeSummary):
    print("trade_summary={}, message_info={}".format(trade_summary, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, statistics_update: roq.StatisticsUpdate):
    print("statistics_update={}, message_info={}".format(statistics_update, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, order_ack: roq.OrderAck):
    print("order_ack={}, message_info={}".format(order_ack, message_info))


@typedispatch
def callback(message_info: roq.MessageInfo, order_update: roq.OrderUpdate):
    print("order_update={}, message_info={}".format(order_update, message_info))


decoder = roq.codec.Decoder(roq.codec.Type.SBE)
length = decoder.dispatch(callback, message)
print("length={}".format(length))
assert length == len(message)
