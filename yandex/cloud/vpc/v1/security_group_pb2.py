# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/security_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/vpc/v1/security_group.proto',
  package='yandex.cloud.vpc.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(yandex/cloud/vpc/v1/security_group.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xeb\x03\n\rSecurityGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry\x12\x12\n\nnetwork_id\x18\x07 \x01(\t\x12\x39\n\x06status\x18\x08 \x01(\x0e\x32).yandex.cloud.vpc.v1.SecurityGroup.Status\x12\x35\n\x05rules\x18\t \x03(\x0b\x32&.yandex.cloud.vpc.v1.SecurityGroupRule\x12\x1b\n\x13\x64\x65\x66\x61ult_for_network\x18\n \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"V\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\"\x94\x04\n\x11SecurityGroupRule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x42\n\x06labels\x18\x03 \x03(\x0b\x32\x32.yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry\x12I\n\tdirection\x18\x04 \x01(\x0e\x32\x30.yandex.cloud.vpc.v1.SecurityGroupRule.DirectionB\x04\xe8\xc7\x31\x01\x12-\n\x05ports\x18\x05 \x01(\x0b\x32\x1e.yandex.cloud.vpc.v1.PortRange\x12\x15\n\rprotocol_name\x18\x06 \x01(\t\x12\x17\n\x0fprotocol_number\x18\x07 \x01(\x03\x12\x36\n\x0b\x63idr_blocks\x18\x08 \x01(\x0b\x32\x1f.yandex.cloud.vpc.v1.CidrBlocksH\x00\x12\x1b\n\x11security_group_id\x18\t \x01(\tH\x00\x12\x1b\n\x11predefined_target\x18\n \x01(\tH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"?\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07INGRESS\x10\x01\x12\n\n\x06\x45GRESS\x10\x02\x42\x0e\n\x06target\x12\x04\xc0\xc1\x31\x01\"I\n\tPortRange\x12\x1e\n\tfrom_port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12\x1c\n\x07to_port\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\"<\n\nCidrBlocks\x12\x16\n\x0ev4_cidr_blocks\x18\x01 \x03(\t\x12\x16\n\x0ev6_cidr_blocks\x18\x02 \x03(\tBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_SECURITYGROUP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.vpc.v1.SecurityGroup.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=535,
  serialized_end=621,
)
_sym_db.RegisterEnumDescriptor(_SECURITYGROUP_STATUS)

_SECURITYGROUPRULE_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='yandex.cloud.vpc.v1.SecurityGroupRule.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INGRESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EGRESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1077,
  serialized_end=1140,
)
_sym_db.RegisterEnumDescriptor(_SECURITYGROUPRULE_DIRECTION)


_SECURITYGROUP_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=488,
  serialized_end=533,
)

_SECURITYGROUP = _descriptor.Descriptor(
  name='SecurityGroup',
  full_name='yandex.cloud.vpc.v1.SecurityGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.vpc.v1.SecurityGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.vpc.v1.SecurityGroup.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.vpc.v1.SecurityGroup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.vpc.v1.SecurityGroup.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.vpc.v1.SecurityGroup.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.SecurityGroup.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_id', full_name='yandex.cloud.vpc.v1.SecurityGroup.network_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.vpc.v1.SecurityGroup.status', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rules', full_name='yandex.cloud.vpc.v1.SecurityGroup.rules', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_for_network', full_name='yandex.cloud.vpc.v1.SecurityGroup.default_for_network', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SECURITYGROUP_LABELSENTRY, ],
  enum_types=[
    _SECURITYGROUP_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=621,
)


_SECURITYGROUPRULE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=488,
  serialized_end=533,
)

_SECURITYGROUPRULE = _descriptor.Descriptor(
  name='SecurityGroupRule',
  full_name='yandex.cloud.vpc.v1.SecurityGroupRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ports', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.ports', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol_name', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.protocol_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol_number', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.protocol_number', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cidr_blocks', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.cidr_blocks', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_group_id', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.security_group_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='predefined_target', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.predefined_target', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SECURITYGROUPRULE_LABELSENTRY, ],
  enum_types=[
    _SECURITYGROUPRULE_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='target', full_name='yandex.cloud.vpc.v1.SecurityGroupRule.target',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=624,
  serialized_end=1156,
)


_PORTRANGE = _descriptor.Descriptor(
  name='PortRange',
  full_name='yandex.cloud.vpc.v1.PortRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_port', full_name='yandex.cloud.vpc.v1.PortRange.from_port', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0070-65535', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_port', full_name='yandex.cloud.vpc.v1.PortRange.to_port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0070-65535', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1158,
  serialized_end=1231,
)


_CIDRBLOCKS = _descriptor.Descriptor(
  name='CidrBlocks',
  full_name='yandex.cloud.vpc.v1.CidrBlocks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v4_cidr_blocks', full_name='yandex.cloud.vpc.v1.CidrBlocks.v4_cidr_blocks', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v6_cidr_blocks', full_name='yandex.cloud.vpc.v1.CidrBlocks.v6_cidr_blocks', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1233,
  serialized_end=1293,
)

_SECURITYGROUP_LABELSENTRY.containing_type = _SECURITYGROUP
_SECURITYGROUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECURITYGROUP.fields_by_name['labels'].message_type = _SECURITYGROUP_LABELSENTRY
_SECURITYGROUP.fields_by_name['status'].enum_type = _SECURITYGROUP_STATUS
_SECURITYGROUP.fields_by_name['rules'].message_type = _SECURITYGROUPRULE
_SECURITYGROUP_STATUS.containing_type = _SECURITYGROUP
_SECURITYGROUPRULE_LABELSENTRY.containing_type = _SECURITYGROUPRULE
_SECURITYGROUPRULE.fields_by_name['labels'].message_type = _SECURITYGROUPRULE_LABELSENTRY
_SECURITYGROUPRULE.fields_by_name['direction'].enum_type = _SECURITYGROUPRULE_DIRECTION
_SECURITYGROUPRULE.fields_by_name['ports'].message_type = _PORTRANGE
_SECURITYGROUPRULE.fields_by_name['cidr_blocks'].message_type = _CIDRBLOCKS
_SECURITYGROUPRULE_DIRECTION.containing_type = _SECURITYGROUPRULE
_SECURITYGROUPRULE.oneofs_by_name['target'].fields.append(
  _SECURITYGROUPRULE.fields_by_name['cidr_blocks'])
_SECURITYGROUPRULE.fields_by_name['cidr_blocks'].containing_oneof = _SECURITYGROUPRULE.oneofs_by_name['target']
_SECURITYGROUPRULE.oneofs_by_name['target'].fields.append(
  _SECURITYGROUPRULE.fields_by_name['security_group_id'])
_SECURITYGROUPRULE.fields_by_name['security_group_id'].containing_oneof = _SECURITYGROUPRULE.oneofs_by_name['target']
_SECURITYGROUPRULE.oneofs_by_name['target'].fields.append(
  _SECURITYGROUPRULE.fields_by_name['predefined_target'])
_SECURITYGROUPRULE.fields_by_name['predefined_target'].containing_oneof = _SECURITYGROUPRULE.oneofs_by_name['target']
DESCRIPTOR.message_types_by_name['SecurityGroup'] = _SECURITYGROUP
DESCRIPTOR.message_types_by_name['SecurityGroupRule'] = _SECURITYGROUPRULE
DESCRIPTOR.message_types_by_name['PortRange'] = _PORTRANGE
DESCRIPTOR.message_types_by_name['CidrBlocks'] = _CIDRBLOCKS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecurityGroup = _reflection.GeneratedProtocolMessageType('SecurityGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYGROUP,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroup)
  })
_sym_db.RegisterMessage(SecurityGroup)
_sym_db.RegisterMessage(SecurityGroup.LabelsEntry)

SecurityGroupRule = _reflection.GeneratedProtocolMessageType('SecurityGroupRule', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYGROUPRULE_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYGROUPRULE,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroupRule)
  })
_sym_db.RegisterMessage(SecurityGroupRule)
_sym_db.RegisterMessage(SecurityGroupRule.LabelsEntry)

PortRange = _reflection.GeneratedProtocolMessageType('PortRange', (_message.Message,), {
  'DESCRIPTOR' : _PORTRANGE,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.PortRange)
  })
_sym_db.RegisterMessage(PortRange)

CidrBlocks = _reflection.GeneratedProtocolMessageType('CidrBlocks', (_message.Message,), {
  'DESCRIPTOR' : _CIDRBLOCKS,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.CidrBlocks)
  })
_sym_db.RegisterMessage(CidrBlocks)


DESCRIPTOR._options = None
_SECURITYGROUP_LABELSENTRY._options = None
_SECURITYGROUPRULE_LABELSENTRY._options = None
_SECURITYGROUPRULE.oneofs_by_name['target']._options = None
_SECURITYGROUPRULE.fields_by_name['direction']._options = None
_PORTRANGE.fields_by_name['from_port']._options = None
_PORTRANGE.fields_by_name['to_port']._options = None
# @@protoc_insertion_point(module_scope)
