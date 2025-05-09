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

class ModifyDBClusterConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'selectdb', '2023-05-22', 'ModifyDBClusterConfig')
		self.set_method('POST')

	def get_ConfigKey(self): # String
		return self.get_query_params().get('ConfigKey')

	def set_ConfigKey(self, ConfigKey):  # String
		self.add_query_param('ConfigKey', ConfigKey)
	def get_SwitchTimeMode(self): # String
		return self.get_query_params().get('SwitchTimeMode')

	def set_SwitchTimeMode(self, SwitchTimeMode):  # String
		self.add_query_param('SwitchTimeMode', SwitchTimeMode)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
