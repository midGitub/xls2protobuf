# Generated by the protocol buffer compiler.  DO NOT EDIT!
#Author: Jumbo 
# source: person_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person_info.proto',
  package='uFramework',
  syntax='proto3',
  serialized_pb=_b('\n\x11person_info.proto\x12\nuFramework\"\x1b\n\x0bPERSON_INFO\x12\x0c\n\x04name\x18\x01 \x01(\x0c\";\n\x11PERSON_INFO_ARRAY\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.uFramework.PERSON_INFOb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSON_INFO = _descriptor.Descriptor(
  name='PERSON_INFO',
  full_name='uFramework.PERSON_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='uFramework.PERSON_INFO.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=60,
)


_PERSON_INFO_ARRAY = _descriptor.Descriptor(
  name='PERSON_INFO_ARRAY',
  full_name='uFramework.PERSON_INFO_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='uFramework.PERSON_INFO_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=121,
)

_PERSON_INFO_ARRAY.fields_by_name['items'].message_type = _PERSON_INFO
DESCRIPTOR.message_types_by_name['PERSON_INFO'] = _PERSON_INFO
DESCRIPTOR.message_types_by_name['PERSON_INFO_ARRAY'] = _PERSON_INFO_ARRAY

PERSON_INFO = _reflection.GeneratedProtocolMessageType('PERSON_INFO', (_message.Message,), dict(
  DESCRIPTOR = _PERSON_INFO,
  __module__ = 'person_info_pb2'
  # @@protoc_insertion_point(class_scope:uFramework.PERSON_INFO)
  ))
_sym_db.RegisterMessage(PERSON_INFO)

PERSON_INFO_ARRAY = _reflection.GeneratedProtocolMessageType('PERSON_INFO_ARRAY', (_message.Message,), dict(
  DESCRIPTOR = _PERSON_INFO_ARRAY,
  __module__ = 'person_info_pb2'
  # @@protoc_insertion_point(class_scope:uFramework.PERSON_INFO_ARRAY)
  ))
_sym_db.RegisterMessage(PERSON_INFO_ARRAY)


# @@protoc_insertion_point(module_scope)
