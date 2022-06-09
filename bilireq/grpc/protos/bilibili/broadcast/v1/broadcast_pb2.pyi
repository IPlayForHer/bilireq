"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilibili.rpc.status_pb2
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Action:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Action.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _Action.ValueType  # 0
    """"""

    UPDATE: _Action.ValueType  # 1
    """"""

    DELETE: _Action.ValueType  # 2
    """"""

class Action(_Action, metaclass=_ActionEnumTypeWrapper):
    """"""
    pass

UNKNOWN: Action.ValueType  # 0
""""""

UPDATE: Action.ValueType  # 1
""""""

DELETE: Action.ValueType  # 2
""""""

global___Action = Action


class AuthReq(google.protobuf.message.Message):
    """鉴权请求，通过authorization验证绑定用户mid"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GUID_FIELD_NUMBER: builtins.int
    CONN_ID_FIELD_NUMBER: builtins.int
    LAST_MSG_ID_FIELD_NUMBER: builtins.int
    guid: typing.Text
    """冷启动id，算法uuid，重新起启会变"""

    conn_id: typing.Text
    """连接id，算法uuid，重连会变"""

    last_msg_id: builtins.int
    """最后收到的消息id，用于过虑重连后获取未读的消息"""

    def __init__(self,
        *,
        guid: typing.Text = ...,
        conn_id: typing.Text = ...,
        last_msg_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["conn_id",b"conn_id","guid",b"guid","last_msg_id",b"last_msg_id"]) -> None: ...
global___AuthReq = AuthReq

class AuthResp(google.protobuf.message.Message):
    """鉴权返回"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___AuthResp = AuthResp

class BroadcastFrame(google.protobuf.message.Message):
    """target_path:
      "/" Service-Name "/" {method name} 参考 gRPC Request Path
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPTIONS_FIELD_NUMBER: builtins.int
    TARGET_PATH_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___FrameOption:
        """请求消息信息"""
        pass
    target_path: typing.Text
    """业务target_path"""

    @property
    def body(self) -> google.protobuf.any_pb2.Any:
        """业务pb内容"""
        pass
    def __init__(self,
        *,
        options: typing.Optional[global___FrameOption] = ...,
        target_path: typing.Text = ...,
        body: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body","options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","options",b"options","target_path",b"target_path"]) -> None: ...
global___BroadcastFrame = BroadcastFrame

class FrameOption(google.protobuf.message.Message):
    """message_id: 
      client: 本次连接唯一的消息id，可用于回执
      server: 唯一消息id，可用于上报或者回执
    sequence:
      client: 客户端应该每次请求时frame seq++，会返回对应的对称req/resp
      server: 服务端下行消息，只会返回默认值：0
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_ID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    IS_ACK_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ACK_ORIGIN_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    message_id: builtins.int
    """消息id"""

    sequence: builtins.int
    """frame序号"""

    is_ack: builtins.bool
    """是否进行消息回执(发出MessageAckReq)
    downstream 上只有服务端设置为true，客户端响应
    upstream   上只有客户端设置为true，服务端响应
    响应帧禁止设置is_ack，协议上禁止循环
    通常只有业务帧才可能设置is_ack, 因为协议栈(例如心跳、鉴权)另有响应约定
    """

    @property
    def status(self) -> bilibili.rpc.status_pb2.Status:
        """业务状态码"""
        pass
    ack_origin: typing.Text
    """业务ack来源, 仅downstream时候由服务端填写."""

    timestamp: builtins.int
    """"""

    def __init__(self,
        *,
        message_id: builtins.int = ...,
        sequence: builtins.int = ...,
        is_ack: builtins.bool = ...,
        status: typing.Optional[bilibili.rpc.status_pb2.Status] = ...,
        ack_origin: typing.Text = ...,
        timestamp: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_origin",b"ack_origin","is_ack",b"is_ack","message_id",b"message_id","sequence",b"sequence","status",b"status","timestamp",b"timestamp"]) -> None: ...
global___FrameOption = FrameOption

class HeartbeatReq(google.protobuf.message.Message):
    """心跳请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___HeartbeatReq = HeartbeatReq

class HeartbeatResp(google.protobuf.message.Message):
    """心跳返回"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___HeartbeatResp = HeartbeatResp

class MessageAckReq(google.protobuf.message.Message):
    """消息回执"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACK_ID_FIELD_NUMBER: builtins.int
    ACK_ORIGIN_FIELD_NUMBER: builtins.int
    TARGET_PATH_FIELD_NUMBER: builtins.int
    ack_id: builtins.int
    """消息id"""

    ack_origin: typing.Text
    """ack来源，由业务指定用于埋点跟踪"""

    target_path: typing.Text
    """消息对应的target_path，方便业务区分和监控统计"""

    def __init__(self,
        *,
        ack_id: builtins.int = ...,
        ack_origin: typing.Text = ...,
        target_path: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_id",b"ack_id","ack_origin",b"ack_origin","target_path",b"target_path"]) -> None: ...
global___MessageAckReq = MessageAckReq

class TargetPath(google.protobuf.message.Message):
    """target_path"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TARGET_PATHS_FIELD_NUMBER: builtins.int
    @property
    def target_paths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """需要订阅的target_paths"""
        pass
    def __init__(self,
        *,
        target_paths: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_paths",b"target_paths"]) -> None: ...
global___TargetPath = TargetPath