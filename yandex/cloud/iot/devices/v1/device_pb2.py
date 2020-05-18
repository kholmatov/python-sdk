# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/devices/v1/device.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iot/devices/v1/device.proto',
  package='yandex.cloud.iot.devices.v1',
  syntax='proto3',
  serialized_options=b'\n\037yandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devices',
  serialized_pb=b'\n(yandex/cloud/iot/devices/v1/device.proto\x12\x1byandex.cloud.iot.devices.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x85\x03\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bregistry_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12L\n\rtopic_aliases\x18\x06 \x03(\x0b\x32\x35.yandex.cloud.iot.devices.v1.Device.TopicAliasesEntry\x12:\n\x06status\x18\x07 \x01(\x0e\x32*.yandex.cloud.iot.devices.v1.Device.Status\x1a\x33\n\x11TopicAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\"\x85\x01\n\x11\x44\x65viceCertificate\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x0e\x44\x65vicePassword\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampBj\n\x1fyandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devicesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_DEVICE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.iot.devices.v1.Device.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=455,
  serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_DEVICE_STATUS)


_DEVICE_TOPICALIASESENTRY = _descriptor.Descriptor(
  name='TopicAliasesEntry',
  full_name='yandex.cloud.iot.devices.v1.Device.TopicAliasesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.iot.devices.v1.Device.TopicAliasesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.iot.devices.v1.Device.TopicAliasesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=453,
)

_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='yandex.cloud.iot.devices.v1.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.devices.v1.Device.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.iot.devices.v1.Device.registry_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.Device.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.iot.devices.v1.Device.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iot.devices.v1.Device.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic_aliases', full_name='yandex.cloud.iot.devices.v1.Device.topic_aliases', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.iot.devices.v1.Device.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICE_TOPICALIASESENTRY, ],
  enum_types=[
    _DEVICE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=527,
)


_DEVICECERTIFICATE = _descriptor.Descriptor(
  name='DeviceCertificate',
  full_name='yandex.cloud.iot.devices.v1.DeviceCertificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='yandex.cloud.iot.devices.v1.DeviceCertificate.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='yandex.cloud.iot.devices.v1.DeviceCertificate.fingerprint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate_data', full_name='yandex.cloud.iot.devices.v1.DeviceCertificate.certificate_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.DeviceCertificate.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=530,
  serialized_end=663,
)


_DEVICEPASSWORD = _descriptor.Descriptor(
  name='DevicePassword',
  full_name='yandex.cloud.iot.devices.v1.DevicePassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='yandex.cloud.iot.devices.v1.DevicePassword.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.devices.v1.DevicePassword.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.devices.v1.DevicePassword.created_at', index=2,
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
  serialized_start=665,
  serialized_end=760,
)

_DEVICE_TOPICALIASESENTRY.containing_type = _DEVICE
_DEVICE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEVICE.fields_by_name['topic_aliases'].message_type = _DEVICE_TOPICALIASESENTRY
_DEVICE.fields_by_name['status'].enum_type = _DEVICE_STATUS
_DEVICE_STATUS.containing_type = _DEVICE
_DEVICECERTIFICATE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEVICEPASSWORD.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DeviceCertificate'] = _DEVICECERTIFICATE
DESCRIPTOR.message_types_by_name['DevicePassword'] = _DEVICEPASSWORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {

  'TopicAliasesEntry' : _reflection.GeneratedProtocolMessageType('TopicAliasesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICE_TOPICALIASESENTRY,
    '__module__' : 'yandex.cloud.iot.devices.v1.device_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.Device.TopicAliasesEntry)
    })
  ,
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.Device)
  })
_sym_db.RegisterMessage(Device)
_sym_db.RegisterMessage(Device.TopicAliasesEntry)

DeviceCertificate = _reflection.GeneratedProtocolMessageType('DeviceCertificate', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECERTIFICATE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeviceCertificate)
  })
_sym_db.RegisterMessage(DeviceCertificate)

DevicePassword = _reflection.GeneratedProtocolMessageType('DevicePassword', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPASSWORD,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DevicePassword)
  })
_sym_db.RegisterMessage(DevicePassword)


DESCRIPTOR._options = None
_DEVICE_TOPICALIASESENTRY._options = None
# @@protoc_insertion_point(module_scope)
