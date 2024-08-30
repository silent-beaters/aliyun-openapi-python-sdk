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
from aliyunsdkdomain.endpoint import endpoint_data

class QueryTaskDetailHistoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryTaskDetailHistory','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_TaskStatus(self): # Integer
		return self.get_query_params().get('TaskStatus')

	def set_TaskStatus(self, TaskStatus):  # Integer
		self.add_query_param('TaskStatus', TaskStatus)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_TaskNo(self): # String
		return self.get_query_params().get('TaskNo')

	def set_TaskNo(self, TaskNo):  # String
		self.add_query_param('TaskNo', TaskNo)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TaskDetailNoCursor(self): # String
		return self.get_query_params().get('TaskDetailNoCursor')

	def set_TaskDetailNoCursor(self, TaskDetailNoCursor):  # String
		self.add_query_param('TaskDetailNoCursor', TaskDetailNoCursor)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_DomainNameCursor(self): # String
		return self.get_query_params().get('DomainNameCursor')

	def set_DomainNameCursor(self, DomainNameCursor):  # String
		self.add_query_param('DomainNameCursor', DomainNameCursor)
