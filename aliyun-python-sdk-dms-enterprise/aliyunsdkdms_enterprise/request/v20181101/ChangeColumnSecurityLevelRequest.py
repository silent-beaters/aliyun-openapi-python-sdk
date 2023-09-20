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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class ChangeColumnSecurityLevelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'ChangeColumnSecurityLevel','dms-enterprise')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NewSensitivityLevel(self): # String
		return self.get_query_params().get('NewSensitivityLevel')

	def set_NewSensitivityLevel(self, NewSensitivityLevel):  # String
		self.add_query_param('NewSensitivityLevel', NewSensitivityLevel)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_SchemaName(self): # String
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_query_param('SchemaName', SchemaName)
	def get_IsLogic(self): # Boolean
		return self.get_query_params().get('IsLogic')

	def set_IsLogic(self, IsLogic):  # Boolean
		self.add_query_param('IsLogic', IsLogic)
	def get_ColumnName(self): # String
		return self.get_query_params().get('ColumnName')

	def set_ColumnName(self, ColumnName):  # String
		self.add_query_param('ColumnName', ColumnName)
	def get_DbId(self): # Long
		return self.get_query_params().get('DbId')

	def set_DbId(self, DbId):  # Long
		self.add_query_param('DbId', DbId)
