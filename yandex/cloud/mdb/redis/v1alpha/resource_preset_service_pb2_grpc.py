# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.mdb.redis.v1alpha import resource_preset_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2
from yandex.cloud.mdb.redis.v1alpha import resource_preset_service_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2


class ResourcePresetServiceStub(object):
  """A set of methods for working with resource presets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.mdb.redis.v1alpha.ResourcePresetService/Get',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.GetResourcePresetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2.ResourcePreset.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.mdb.redis.v1alpha.ResourcePresetService/List',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.ListResourcePresetsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.ListResourcePresetsResponse.FromString,
        )


class ResourcePresetServiceServicer(object):
  """A set of methods for working with resource presets.
  """

  def Get(self, request, context):
    """Returns the specified resource preset.

    To get the list of available resource presets, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of available resource presets.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ResourcePresetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.GetResourcePresetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2.ResourcePreset.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.ListResourcePresetsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__service__pb2.ListResourcePresetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.mdb.redis.v1alpha.ResourcePresetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))