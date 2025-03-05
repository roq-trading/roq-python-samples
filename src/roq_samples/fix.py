#!/usr/bin/env python

"""
Copyright (c) 2017-2025, Hans Erik Thrane

Demonstrates FIX message encoding/decoding
"""

from datetime import datetime, timedelta

from fastcore.all import typedispatch

import roq

encoder = roq.fix.codec.Encoder(sender_comp_id="me", target_comp_id="you")

logon = roq.fix.codec.Logon(
    heart_bt_int=30,  # XXX TODO timedelta(seconds=30),
    username="my_name",
    password="xyz",
    encrypt_method=roq.fix.EncryptMethod.NONE,
)

message = encoder.encode(logon, datetime.now())

print('message="{}", length={}'.format(message.decode().replace(chr(1), "|"), len(message)))


@typedispatch
def callback(header: roq.fix.Header, logon: roq.fix.codec.Logon):
    print("logon={}, header={}".format(logon, header))


@typedispatch
def callback(header: roq.fix.Header, logout: roq.fix.codec.Logout):
    print("logout={}, header={}".format(logout, header))


@typedispatch
def callback(header: roq.fix.Header, test_request: roq.fix.codec.TestRequest):
    print("test_request={}, header={}".format(test_request, header))


@typedispatch
def callback(header: roq.fix.Header, heartbeat: roq.fix.codec.Heartbeat):
    print("heartbeat={}, header={}".format(heartbeat, header))


@typedispatch
def callback(header: roq.fix.Header, resend_request: roq.fix.codec.ResendRequest):
    print("resend_request={}, header={}".format(resend_request, header))


@typedispatch
def callback(header: roq.fix.Header, reject: roq.fix.codec.Reject):
    print("reject={}, header={}".format(reject, header))


@typedispatch
def callback(header: roq.fix.Header, business_message_reject: roq.fix.codec.BusinessMessageReject):
    print("business_message_reject={}, header={}".format(business_message_reject, header))


@typedispatch
def callback(header: roq.fix.Header, user_request: roq.fix.codec.UserRequest):
    print("user_request={}, header={}".format(user_request, header))


@typedispatch
def callback(header: roq.fix.Header, user_response: roq.fix.codec.UserResponse):
    print("user_response={}, header={}".format(user_response, header))


@typedispatch
def callback(
    header: roq.fix.Header,
    trading_session_status_request: roq.fix.codec.TradingSessionStatusRequest,
):
    print("trading_session_status_request={}, header={}".format(trading_session_status_request, header))


@typedispatch
def callback(header: roq.fix.Header, trading_session_status: roq.fix.codec.TradingSessionStatus):
    print("trading_session_status={}, header={}".format(trading_session_status, header))


@typedispatch
def callback(header: roq.fix.Header, security_list_request: roq.fix.codec.SecurityListRequest):
    print("security_list_request={}, header={}".format(security_list_request, header))


@typedispatch
def callback(header: roq.fix.Header, security_list: roq.fix.codec.SecurityList):
    print("security_list={}, header={}".format(security_list, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header,
#     security_definition_request: roq.fix.codec.SecurityDefinitionRequest,
# ):
#     print("security_definition_request={}, header={}".format(security_definition_request, header))


# @typedispatch
# def callback(header: roq.fix.Header, security_definition: roq.fix.codec.SecurityDefinition):
#     print("security_definition={}, header={}".format(security_definition, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, security_status_request: roq.fix.codec.SecurityStatusRequest
# ):
#     print("security_status_request={}, header={}".format(security_status_request, header))


# @typedispatch
# def callback(header: roq.fix.Header, security_status: roq.fix.codec.SecurityStatus):
#     print("security_status={}, header={}".format(security_status, header))


# @typedispatch
# def callback(header: roq.fix.Header, market_data_request: roq.fix.codec.MarketDataRequest):
#     print("market_data_request={}, header={}".format(market_data_request, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, market_data_request_reject: roq.fix.codec.MarketDataRequestReject
# ):
#     print("market_data_request_reject={}, header={}".format(market_data_request_reject, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header,
#     market_data_snapshot_full_refresh: roq.fix.codec.MarketDataSnapshotFullRefresh,
# ):
#     print(
#         "market_data_snapshot_full_refresh={}, header={}".format(
#             market_data_snapshot_full_refresh, header
#         )
#     )


# @typedispatch
# def callback(
#     header: roq.fix.Header,
#     market_data_incremental_refresh: roq.fix.codec.MarketDataIncrementalRefresh,
# ):
#     print(
#         "market_data_incremental_refresh={}, header={}".format(
#             market_data_incremental_refresh, header
#         )
#     )


# @typedispatch
# def callback(header: roq.fix.Header, order_status_request: roq.fix.codec.OrderStatusRequest):
#     print("order_status_request={}, header={}".format(order_status_request, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, order_mass_status_request: roq.fix.codec.OrderMassStatusRequest
# ):
#     print("order_mass_status_request={}, header={}".format(order_mass_status_request, header))


# @typedispatch
# def callback(header: roq.fix.Header, new_order_single: roq.fix.codec.NewOrderSingle):
#     print("new_order_single={}, header={}".format(new_order_single, header))


# @typedispatch
# def callback(header: roq.fix.Header, order_cancel_request: roq.fix.codec.OrderCancelRequest):
#     print("order_cancel_request={}, header={}".format(order_cancel_request, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header,
#     order_cancel_replace_request: roq.fix.codec.OrderCancelReplaceRequest,
# ):
#     print("order_cancel_replace_request={}, header={}".format(order_cancel_replace_request, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, order_mass_cancel_request: roq.fix.codec.OrderMassCancelRequest
# ):
#     print("order_mass_cancel_request={}, header={}".format(order_mass_cancel_request, header))


# @typedispatch
# def callback(header: roq.fix.Header, order_cancel_reject: roq.fix.codec.OrderCancelReject):
#     print("order_cancel_reject={}, header={}".format(order_cancel_reject, header))


# @typedispatch
# def callback(header: roq.fix.Header, execution_report: roq.fix.codec.ExecutionReport):
#     print("execution_report={}, header={}".format(execution_report, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header,
#     trade_capture_report_request: roq.fix.codec.TradeCaptureReportRequest,
# ):
#     print("trade_capture_report_request={}, header={}".format(trade_capture_report_request, header))


# @typedispatch
# def callback(header: roq.fix.Header, trade_capture_report: roq.fix.codec.TradeCaptureReport):
#     print("trade_capture_report={}, header={}".format(trade_capture_report, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, request_for_positions: roq.fix.codec.RequestForPositions
# ):
#     print("request_for_positions={}, header={}".format(request_for_positions, header))


# @typedispatch
# def callback(
#     header: roq.fix.Header, request_for_positions_ack: roq.fix.codec.RequestForPositionsAck
# ):
#     print("request_for_positions_ack={}, header={}".format(request_for_positions_ack, header))


# @typedispatch
# def callback(header: roq.fix.Header, position_report: roq.fix.codec.PositionReport):
#     print("position_report={}, header={}".format(position_report, header))


decoder = roq.fix.codec.Decoder()

# version 1
length = decoder.dispatch(callback, message)
print("length={}".format(length))
assert length == len(message)

# version 2
# header, length = decoder.decode(message)
# print("length={}".format(length))
# assert length==len(message)
# assert header.msg_type == roq.fix.codec.MsgType.LOGON
# logon = decoder.decode(roq.fix.codec.Logon, message)
# print('logon={}, header={}'.format(logon, header))

tmp = roq.fix.codec.SecListGrp(symbol="BTC-PERPETUAL", security_exchange="deribit")
security_list = roq.fix.codec.SecurityList(
    security_req_id="req1",
    security_response_id="resp1",
    security_request_result=roq.fix.SecurityRequestResult.VALID,
    no_related_sym=[tmp],
)
print("security_list={}".format(security_list))

message = encoder.encode(security_list, datetime.now())

print('message="{}", length={}'.format(message.decode().replace(chr(1), "|"), len(message)))

length = decoder.dispatch(callback, message)

print("length={}".format(length))
