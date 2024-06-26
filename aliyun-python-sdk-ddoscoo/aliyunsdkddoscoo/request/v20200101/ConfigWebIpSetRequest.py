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

class ConfigWebIpSetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddoscoo', '2020-01-01', 'ConfigWebIpSet','ddoscoo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_BlackLists(self): # RepeatList
		return self.get_query_params().get('BlackList')

	def set_BlackLists(self, BlackList):  # RepeatList
		for depth1 in range(len(BlackList)):
			self.add_query_param('BlackList.' + str(depth1 + 1), BlackList[depth1])
	def get_WhiteLists(self): # RepeatList
		return self.get_query_params().get('WhiteList')

	def set_WhiteLists(self, WhiteList):  # RepeatList
		for depth1 in range(len(WhiteList)):
			self.add_query_param('WhiteList.' + str(depth1 + 1), WhiteList[depth1])
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
