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
from aliyunsdkmts.endpoint import endpoint_data

class QuerySmarttagJobListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'QuerySmarttagJobList','mts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_NextPageToken(self):
		return self.get_query_params().get('NextPageToken')

	def set_NextPageToken(self,NextPageToken):
		self.add_query_param('NextPageToken',NextPageToken)

	def get_StartOfJobCreatedTimeRange(self):
		return self.get_query_params().get('StartOfJobCreatedTimeRange')

	def set_StartOfJobCreatedTimeRange(self,StartOfJobCreatedTimeRange):
		self.add_query_param('StartOfJobCreatedTimeRange',StartOfJobCreatedTimeRange)

	def get_EndOfJobCreatedTimeRange(self):
		return self.get_query_params().get('EndOfJobCreatedTimeRange')

	def set_EndOfJobCreatedTimeRange(self,EndOfJobCreatedTimeRange):
		self.add_query_param('EndOfJobCreatedTimeRange',EndOfJobCreatedTimeRange)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_MaximumPageSize(self):
		return self.get_query_params().get('MaximumPageSize')

	def set_MaximumPageSize(self,MaximumPageSize):
		self.add_query_param('MaximumPageSize',MaximumPageSize)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PipelineId(self):
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_query_param('PipelineId',PipelineId)

	def get_JobIds(self):
		return self.get_query_params().get('JobIds')

	def set_JobIds(self,JobIds):
		self.add_query_param('JobIds',JobIds)