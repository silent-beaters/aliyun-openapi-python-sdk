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
from aliyunsdkvod.endpoint import endpoint_data

class ListLetterSendJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'ListLetterSendJob','vod')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ToAddress(self):
		return self.get_query_params().get('ToAddress')

	def set_ToAddress(self,ToAddress):
		self.add_query_param('ToAddress',ToAddress)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_DetectionId(self):
		return self.get_query_params().get('DetectionId')

	def set_DetectionId(self,DetectionId):
		self.add_query_param('DetectionId',DetectionId)