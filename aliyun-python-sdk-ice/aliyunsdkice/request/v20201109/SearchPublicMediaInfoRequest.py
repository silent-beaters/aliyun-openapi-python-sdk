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
from aliyunsdkice.endpoint import endpoint_data

class SearchPublicMediaInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SearchPublicMediaInfo','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EntityId(self): # String
		return self.get_query_params().get('EntityId')

	def set_EntityId(self, EntityId):  # String
		self.add_query_param('EntityId', EntityId)
	def get_Authorized(self): # Boolean
		return self.get_query_params().get('Authorized')

	def set_Authorized(self, Authorized):  # Boolean
		self.add_query_param('Authorized', Authorized)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_MediaIds(self): # String
		return self.get_query_params().get('MediaIds')

	def set_MediaIds(self, MediaIds):  # String
		self.add_query_param('MediaIds', MediaIds)
	def get_DynamicMetaDataMatchFields(self): # String
		return self.get_query_params().get('DynamicMetaDataMatchFields')

	def set_DynamicMetaDataMatchFields(self, DynamicMetaDataMatchFields):  # String
		self.add_query_param('DynamicMetaDataMatchFields', DynamicMetaDataMatchFields)
	def get_PageNo(self): # Integer
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_query_param('PageNo', PageNo)
	def get_SortBy(self): # String
		return self.get_query_params().get('SortBy')

	def set_SortBy(self, SortBy):  # String
		self.add_query_param('SortBy', SortBy)
	def get_Favorite(self): # Boolean
		return self.get_query_params().get('Favorite')

	def set_Favorite(self, Favorite):  # Boolean
		self.add_query_param('Favorite', Favorite)