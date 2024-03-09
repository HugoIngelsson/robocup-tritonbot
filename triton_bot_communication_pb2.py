# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: triton_bot_communication.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ssl_simulation_robot_control_pb2 as ssl__simulation__robot__control__pb2
import messages_robocup_ssl_detection_pb2 as messages__robocup__ssl__detection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='triton_bot_communication.proto',
  package='proto.triton',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1etriton_bot_communication.proto\x12\x0cproto.triton\x1a\"ssl_simulation_robot_control.proto\x1a$messages_robocup_ssl_detection.proto\"\x81\x01\n\x10TritonBotMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x30\n\x06vision\x18\x02 \x01(\x0b\x32 .proto.vision.SSL_DetectionRobot\x12/\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x1e.proto.simulation.RobotCommandb\x06proto3')
  ,
  dependencies=[ssl__simulation__robot__control__pb2.DESCRIPTOR,messages__robocup__ssl__detection__pb2.DESCRIPTOR,])




_TRITONBOTMESSAGE = _descriptor.Descriptor(
  name='TritonBotMessage',
  full_name='proto.triton.TritonBotMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.triton.TritonBotMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vision', full_name='proto.triton.TritonBotMessage.vision', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='proto.triton.TritonBotMessage.command', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=252,
)

_TRITONBOTMESSAGE.fields_by_name['vision'].message_type = messages__robocup__ssl__detection__pb2._SSL_DETECTIONROBOT
_TRITONBOTMESSAGE.fields_by_name['command'].message_type = ssl__simulation__robot__control__pb2._ROBOTCOMMAND
DESCRIPTOR.message_types_by_name['TritonBotMessage'] = _TRITONBOTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TritonBotMessage = _reflection.GeneratedProtocolMessageType('TritonBotMessage', (_message.Message,), dict(
  DESCRIPTOR = _TRITONBOTMESSAGE,
  __module__ = 'triton_bot_communication_pb2'
  # @@protoc_insertion_point(class_scope:proto.triton.TritonBotMessage)
  ))
_sym_db.RegisterMessage(TritonBotMessage)


# @@protoc_insertion_point(module_scope)