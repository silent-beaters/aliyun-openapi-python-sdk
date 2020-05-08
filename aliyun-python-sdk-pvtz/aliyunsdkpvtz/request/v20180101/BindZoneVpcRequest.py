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
from aliyunsdkpvtz.endpoint import endpoint_data

class BindZoneVpcRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'pvtz', '2018-01-01', 'BindZoneVpc','pvtz')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Vpcss(self):
		return self.get_query_params().get('Vpcss')

	def set_Vpcss(self,Vpcss):
		for i in range(len(Vpcss)):	
			if Vpcss[i].get('RegionId') is not None:
				self.add_query_param('Vpcs.' + str(i + 1) + '.RegionId' , Vpcss[i].get('RegionId'))
			if Vpcss[i].get('VpcId') is not None:
				self.add_query_param('Vpcs.' + str(i + 1) + '.VpcId' , Vpcss[i].get('VpcId'))
