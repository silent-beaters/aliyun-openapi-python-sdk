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
from aliyunsdkess.endpoint import endpoint_data

class AttachAlbServerGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'AttachAlbServerGroups','ess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_ForceAttach(self):
		return self.get_query_params().get('ForceAttach')

	def set_ForceAttach(self,ForceAttach):
		self.add_query_param('ForceAttach',ForceAttach)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AlbServerGroups(self):
		return self.get_query_params().get('AlbServerGroup')

	def set_AlbServerGroups(self, AlbServerGroups):
		for depth1 in range(len(AlbServerGroups)):
			if AlbServerGroups[depth1].get('AlbServerGroupId') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.AlbServerGroupId', AlbServerGroups[depth1].get('AlbServerGroupId'))
			if AlbServerGroups[depth1].get('Port') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.Port', AlbServerGroups[depth1].get('Port'))
			if AlbServerGroups[depth1].get('Weight') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.Weight', AlbServerGroups[depth1].get('Weight'))