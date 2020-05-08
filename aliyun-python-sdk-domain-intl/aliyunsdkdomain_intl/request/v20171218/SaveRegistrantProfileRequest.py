# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SaveRegistrantProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain-intl', '2017-12-18', 'SaveRegistrantProfile','domain')

	def get_Country(self):
		return self.get_query_params().get('Country')

	def set_Country(self,Country):
		self.add_query_param('Country',Country)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_TelArea(self):
		return self.get_query_params().get('TelArea')

	def set_TelArea(self,TelArea):
		self.add_query_param('TelArea',TelArea)

	def get_City(self):
		return self.get_query_params().get('City')

	def set_City(self,City):
		self.add_query_param('City',City)

	def get_RegistrantProfileId(self):
		return self.get_query_params().get('RegistrantProfileId')

	def set_RegistrantProfileId(self,RegistrantProfileId):
		self.add_query_param('RegistrantProfileId',RegistrantProfileId)

	def get_RegistrantType(self):
		return self.get_query_params().get('RegistrantType')

	def set_RegistrantType(self,RegistrantType):
		self.add_query_param('RegistrantType',RegistrantType)

	def get_RegistrantProfileType(self):
		return self.get_query_params().get('RegistrantProfileType')

	def set_RegistrantProfileType(self,RegistrantProfileType):
		self.add_query_param('RegistrantProfileType',RegistrantProfileType)

	def get_Telephone(self):
		return self.get_query_params().get('Telephone')

	def set_Telephone(self,Telephone):
		self.add_query_param('Telephone',Telephone)

	def get_DefaultRegistrantProfile(self):
		return self.get_query_params().get('DefaultRegistrantProfile')

	def set_DefaultRegistrantProfile(self,DefaultRegistrantProfile):
		self.add_query_param('DefaultRegistrantProfile',DefaultRegistrantProfile)

	def get_RegistrantOrganization(self):
		return self.get_query_params().get('RegistrantOrganization')

	def set_RegistrantOrganization(self,RegistrantOrganization):
		self.add_query_param('RegistrantOrganization',RegistrantOrganization)

	def get_TelExt(self):
		return self.get_query_params().get('TelExt')

	def set_TelExt(self,TelExt):
		self.add_query_param('TelExt',TelExt)

	def get_Province(self):
		return self.get_query_params().get('Province')

	def set_Province(self,Province):
		self.add_query_param('Province',Province)

	def get_PostalCode(self):
		return self.get_query_params().get('PostalCode')

	def set_PostalCode(self,PostalCode):
		self.add_query_param('PostalCode',PostalCode)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)

	def get_RegistrantName(self):
		return self.get_query_params().get('RegistrantName')

	def set_RegistrantName(self,RegistrantName):
		self.add_query_param('RegistrantName',RegistrantName)