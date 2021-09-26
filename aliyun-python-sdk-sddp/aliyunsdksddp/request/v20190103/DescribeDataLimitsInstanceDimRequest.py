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
from aliyunsdksddp.endpoint import endpoint_data

class DescribeDataLimitsInstanceDimRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeDataLimitsInstanceDim')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ParentId(self):
		return self.get_query_params().get('ParentId')

	def set_ParentId(self,ParentId):
		self.add_query_param('ParentId',ParentId)

	def get_Enable(self):
		return self.get_query_params().get('Enable')

	def set_Enable(self,Enable):
		self.add_query_param('Enable',Enable)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CheckStatus(self):
		return self.get_query_params().get('CheckStatus')

	def set_CheckStatus(self,CheckStatus):
		self.add_query_param('CheckStatus',CheckStatus)

	def get_DatamaskStatus(self):
		return self.get_query_params().get('DatamaskStatus')

	def set_DatamaskStatus(self,DatamaskStatus):
		self.add_query_param('DatamaskStatus',DatamaskStatus)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ServiceRegionId(self):
		return self.get_query_params().get('ServiceRegionId')

	def set_ServiceRegionId(self,ServiceRegionId):
		self.add_query_param('ServiceRegionId',ServiceRegionId)

	def get_EngineType(self):
		return self.get_query_params().get('EngineType')

	def set_EngineType(self,EngineType):
		self.add_query_param('EngineType',EngineType)

	def get_AuditStatus(self):
		return self.get_query_params().get('AuditStatus')

	def set_AuditStatus(self,AuditStatus):
		self.add_query_param('AuditStatus',AuditStatus)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)