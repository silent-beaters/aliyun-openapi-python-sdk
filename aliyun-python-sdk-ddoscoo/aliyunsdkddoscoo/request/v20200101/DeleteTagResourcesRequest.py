# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkddoscoo.endpoint import endpoint_data

class DeleteTagResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddoscoo', '2020-01-01', 'DeleteTagResources','ddoscoo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_All(self): # Boolean
		return self.get_query_params().get('All')

	def set_All(self, All):  # Boolean
		self.add_query_param('All', All)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_TagKeys(self): # RepeatList
		return self.get_query_params().get('TagKey')

	def set_TagKeys(self, TagKey):  # RepeatList
		for depth1 in range(len(TagKey)):
			self.add_query_param('TagKey.' + str(depth1 + 1), TagKey[depth1])
	def get_ResourceIdss(self): # RepeatList
		return self.get_query_params().get('ResourceIds')

	def set_ResourceIdss(self, ResourceIds):  # RepeatList
		for depth1 in range(len(ResourceIds)):
			self.add_query_param('ResourceIds.' + str(depth1 + 1), ResourceIds[depth1])
