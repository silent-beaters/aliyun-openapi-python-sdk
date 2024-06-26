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
from aliyunsdklive.endpoint import endpoint_data

class GetTranscodeTaskStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'GetTranscodeTaskStatus','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TranscodingTemplate(self): # String
		return self.get_query_params().get('TranscodingTemplate')

	def set_TranscodingTemplate(self, TranscodingTemplate):  # String
		self.add_query_param('TranscodingTemplate', TranscodingTemplate)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_PushDomain(self): # String
		return self.get_query_params().get('PushDomain')

	def set_PushDomain(self, PushDomain):  # String
		self.add_query_param('PushDomain', PushDomain)
	def get_StreamName(self): # String
		return self.get_query_params().get('StreamName')

	def set_StreamName(self, StreamName):  # String
		self.add_query_param('StreamName', StreamName)
	def get_App(self): # String
		return self.get_query_params().get('App')

	def set_App(self, App):  # String
		self.add_query_param('App', App)
