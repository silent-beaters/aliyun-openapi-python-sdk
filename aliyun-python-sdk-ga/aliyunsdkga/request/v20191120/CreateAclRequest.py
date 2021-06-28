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
from aliyunsdkga.endpoint import endpoint_data

class CreateAclRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateAcl','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_AclName(self):
		return self.get_query_params().get('AclName')

	def set_AclName(self,AclName):
		self.add_query_param('AclName',AclName)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_AclEntriess(self):
		return self.get_query_params().get('AclEntries')

	def set_AclEntriess(self, AclEntriess):
		for depth1 in range(len(AclEntriess)):
			if AclEntriess[depth1].get('Entry') is not None:
				self.add_query_param('AclEntries.' + str(depth1 + 1) + '.Entry', AclEntriess[depth1].get('Entry'))
			if AclEntriess[depth1].get('EntryDescription') is not None:
				self.add_query_param('AclEntries.' + str(depth1 + 1) + '.EntryDescription', AclEntriess[depth1].get('EntryDescription'))

	def get_AddressIPVersion(self):
		return self.get_query_params().get('AddressIPVersion')

	def set_AddressIPVersion(self,AddressIPVersion):
		self.add_query_param('AddressIPVersion',AddressIPVersion)