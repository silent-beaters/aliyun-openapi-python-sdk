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

class CreateDedicatedBlockStorageClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ebs', '2021-07-30', 'CreateDedicatedBlockStorageCluster','ebs')
		self.set_method('POST')

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Capacity(self): # Long
		return self.get_query_params().get('Capacity')

	def set_Capacity(self, Capacity):  # Long
		self.add_query_param('Capacity', Capacity)
	def get_DbscId(self): # String
		return self.get_query_params().get('DbscId')

	def set_DbscId(self, DbscId):  # String
		self.add_query_param('DbscId', DbscId)
	def get_Azone(self): # String
		return self.get_query_params().get('Azone')

	def set_Azone(self, Azone):  # String
		self.add_query_param('Azone', Azone)
	def get_DbscName(self): # String
		return self.get_query_params().get('DbscName')

	def set_DbscName(self, DbscName):  # String
		self.add_query_param('DbscName', DbscName)