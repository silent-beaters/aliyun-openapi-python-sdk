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
from aliyunsdkcloudapi.endpoint import endpoint_data

class CreateBackendRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateBackend','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_BackendName(self): # String
		return self.get_query_params().get('BackendName')

	def set_BackendName(self, BackendName):  # String
		self.add_query_param('BackendName', BackendName)
	def get_CreateEventBridgeServiceLinkedRole(self): # Boolean
		return self.get_query_params().get('CreateEventBridgeServiceLinkedRole')

	def set_CreateEventBridgeServiceLinkedRole(self, CreateEventBridgeServiceLinkedRole):  # Boolean
		self.add_query_param('CreateEventBridgeServiceLinkedRole', CreateEventBridgeServiceLinkedRole)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_BackendType(self): # String
		return self.get_query_params().get('BackendType')

	def set_BackendType(self, BackendType):  # String
		self.add_query_param('BackendType', BackendType)
