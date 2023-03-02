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

class ModifyDatabaseInstanceParameterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'ModifyDatabaseInstanceParameter','SWAS-OPEN')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DatabaseInstanceId(self): # String
		return self.get_query_params().get('DatabaseInstanceId')

	def set_DatabaseInstanceId(self, DatabaseInstanceId):  # String
		self.add_query_param('DatabaseInstanceId', DatabaseInstanceId)
	def get_ForceRestart(self): # Boolean
		return self.get_query_params().get('ForceRestart')

	def set_ForceRestart(self, ForceRestart):  # Boolean
		self.add_query_param('ForceRestart', ForceRestart)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)