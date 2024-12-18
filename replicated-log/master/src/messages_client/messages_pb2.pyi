from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[PingStatus]
    OK: _ClassVar[PingStatus]
    UNREACHABLE: _ClassVar[PingStatus]
    ERROR: _ClassVar[PingStatus]
UNKNOWN: PingStatus
OK: PingStatus
UNREACHABLE: PingStatus
ERROR: PingStatus

class AppendRequest(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    message: str
    def __init__(self, id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class AppendResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class GetAllMessagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("id", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    message: str
    def __init__(self, id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class GetAllMessagesResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageResponse]
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageResponse, _Mapping]]] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: PingStatus
    def __init__(self, status: _Optional[_Union[PingStatus, str]] = ...) -> None: ...
