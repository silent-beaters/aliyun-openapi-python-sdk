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
class MoPenAddGroupMemberRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'MoPen', '2018-02-11', 'MoPenAddGroupMember','mopen')
		self.set_protocol_type('https');
		self.set_method('POST')

	def get_GroupId(self):
		return self.get_body_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_body_params('GroupId', GroupId)

	def get_DeviceName(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_body_params('DeviceName', DeviceName)