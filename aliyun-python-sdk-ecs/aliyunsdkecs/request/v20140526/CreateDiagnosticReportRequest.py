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
from aliyunsdkecs.endpoint import endpoint_data

class CreateDiagnosticReportRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateDiagnosticReport','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_SourceSystem(self): # String
		return self.get_query_params().get('SourceSystem')

	def set_SourceSystem(self, SourceSystem):  # String
		self.add_query_param('SourceSystem', SourceSystem)
	def get_PluginVersion(self): # String
		return self.get_query_params().get('PluginVersion')

	def set_PluginVersion(self, PluginVersion):  # String
		self.add_query_param('PluginVersion', PluginVersion)
	def get_ResourceIds(self): # RepeatList
		return self.get_query_params().get('ResourceId')

	def set_ResourceIds(self, ResourceId):  # RepeatList
		for depth1 in range(len(ResourceId)):
			self.add_query_param('ResourceId.' + str(depth1 + 1), ResourceId[depth1])
	def get_CommandNames(self): # RepeatList
		return self.get_query_params().get('CommandName')

	def set_CommandNames(self, CommandName):  # RepeatList
		for depth1 in range(len(CommandName)):
			self.add_query_param('CommandName.' + str(depth1 + 1), CommandName[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_CommandType(self): # String
		return self.get_query_params().get('CommandType')

	def set_CommandType(self, CommandType):  # String
		self.add_query_param('CommandType', CommandType)
	def get_DiagnosticCategory(self): # String
		return self.get_query_params().get('DiagnosticCategory')

	def set_DiagnosticCategory(self, DiagnosticCategory):  # String
		self.add_query_param('DiagnosticCategory', DiagnosticCategory)