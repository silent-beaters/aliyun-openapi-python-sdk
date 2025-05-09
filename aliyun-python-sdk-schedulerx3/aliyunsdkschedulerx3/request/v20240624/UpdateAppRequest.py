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

class UpdateAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'UpdateApp')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_AccessToken(self): # String
		return self.get_body_params().get('AccessToken')

	def set_AccessToken(self, AccessToken):  # String
		self.add_body_params('AccessToken', AccessToken)
	def get_Title(self): # String
		return self.get_body_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_body_params('Title', Title)
	def get_AppName(self): # String
		return self.get_body_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_body_params('AppName', AppName)
	def get_ClusterId(self): # String
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_body_params('ClusterId', ClusterId)
	def get_EnableLog(self): # Boolean
		return self.get_body_params().get('EnableLog')

	def set_EnableLog(self, EnableLog):  # Boolean
		self.add_body_params('EnableLog', EnableLog)
	def get_MaxConcurrency(self): # Integer
		return self.get_body_params().get('MaxConcurrency')

	def set_MaxConcurrency(self, MaxConcurrency):  # Integer
		self.add_body_params('MaxConcurrency', MaxConcurrency)
