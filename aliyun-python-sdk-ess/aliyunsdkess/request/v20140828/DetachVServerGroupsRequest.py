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

class DetachVServerGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DetachVServerGroups','ess')
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

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ForceDetach(self):
		return self.get_query_params().get('ForceDetach')

	def set_ForceDetach(self,ForceDetach):
		self.add_query_param('ForceDetach',ForceDetach)

	def get_VServerGroups(self):
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroups(self, VServerGroups):
		for depth1 in range(len(VServerGroups)):
			if VServerGroups[depth1].get('LoadBalancerId') is not None:
				self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.LoadBalancerId', VServerGroups[depth1].get('LoadBalancerId'))
			if VServerGroups[depth1].get('VServerGroupAttribute') is not None:
				for depth2 in range(len(VServerGroups[depth1].get('VServerGroupAttribute'))):
					if VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.' + str(depth2 + 1) + '.VServerGroupId', VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId'))
					if VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Port') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.' + str(depth2 + 1) + '.Port', VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Port'))