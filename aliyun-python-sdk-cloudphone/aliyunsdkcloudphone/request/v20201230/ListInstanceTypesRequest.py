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

class ListInstanceTypesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudphone', '2020-12-30', 'ListInstanceTypes')
		self.set_method('POST')

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_InstanceTypes(self): # RepeatList
		return self.get_query_params().get('InstanceType')

	def set_InstanceTypes(self, InstanceType):  # RepeatList
		for depth1 in range(len(InstanceType)):
			self.add_query_param('InstanceType.' + str(depth1 + 1), InstanceType[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_InstanceTypeFamily(self): # String
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self, InstanceTypeFamily):  # String
		self.add_query_param('InstanceTypeFamily', InstanceTypeFamily)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)