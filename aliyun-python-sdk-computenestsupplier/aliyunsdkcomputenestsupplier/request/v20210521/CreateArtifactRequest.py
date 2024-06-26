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
from aliyunsdkcomputenestsupplier.endpoint import endpoint_data

class CreateArtifactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNestSupplier', '2021-05-21', 'CreateArtifact')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_SupportRegionIdss(self): # RepeatList
		return self.get_query_params().get('SupportRegionIds')

	def set_SupportRegionIdss(self, SupportRegionIds):  # RepeatList
		for depth1 in range(len(SupportRegionIds)):
			self.add_query_param('SupportRegionIds.' + str(depth1 + 1), SupportRegionIds[depth1])
	def get_ArtifactType(self): # String
		return self.get_query_params().get('ArtifactType')

	def set_ArtifactType(self, ArtifactType):  # String
		self.add_query_param('ArtifactType', ArtifactType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ArtifactId(self): # String
		return self.get_query_params().get('ArtifactId')

	def set_ArtifactId(self, ArtifactId):  # String
		self.add_query_param('ArtifactId', ArtifactId)
	def get_ArtifactProperty(self): # String
		return self.get_query_params().get('ArtifactProperty')

	def set_ArtifactProperty(self, ArtifactProperty):  # String
		self.add_query_param('ArtifactProperty', ArtifactProperty)
	def get_VersionName(self): # String
		return self.get_query_params().get('VersionName')

	def set_VersionName(self, VersionName):  # String
		self.add_query_param('VersionName', VersionName)
