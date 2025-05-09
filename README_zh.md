# 阿里云开发者 Python 工具套件

[![PyPI version](https://badge.fury.io/py/aliyun-python-sdk-core.svg)](https://badge.fury.io/py/aliyun-python-sdk-core)
[![Python test](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/graph/badge.svg?token=qmWxah6dPs)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)
[![python](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)

阿里云 V1.0 SDK 即将进入基础安全维护阶段，不再建议使用，建议使用 V2.0 SDK。

## 使用诊断

[Troubleshoot](https://api.aliyun.com/troubleshoot?source=github_sdk) 提供 OpenAPI 使用诊断服务，通过 `RequestID` 或 `报错信息` ，帮助开发者快速定位，为开发者提供解决方案。

## 在线示例

**[开发者门户](https://api.aliyun.com)** 提供在线调用云产品 OpenAPI、并动态生成 SDK Example 代码和快速检索接口等能力，能显著降低使用云 API 的难度，强烈推荐使用

<a href="https://api.aliyun.com" target="api_explorer">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

## 重要的更新

- 阿里云 Python SDK 核心库 `aliyun-python-sdk-core` 版本从 2.16.0 开始，仅支持 Python 3.7 及以上的环境。

## 文档

- [环境要求](./docs/0-Requirement-CN.md)
- [安装](./docs/1-Installation-CN.md)
- [客户端与凭证](./docs/2-Client-CN.md)
- [超时机制](./docs/3-Timeout-CN.md)
- [代理配置](./docs/4-Proxy-CN.md)
- [日志](./docs/5-Log-CN.md)
- [域名](./docs/6-Endpoint-CN.md)
- [Https配置](./docs/7-Https-CN.md)
- [调试](./docs/8-Debug-CN.md)
- [异常](./docs/9-Exception-CN.md)


## 环境准备

1. 要使用阿里云 Python SDK ，您需要一个云账号以及一对`Access Key ID`和`Access Key Secret`。 请在阿里云控制台中的 [AccessKey管理页面](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak) 上创建和查看您的 Access Key，或者联系您的系统管理员
2. 要使用阿里云 SDK 访问某个产品的 API，您需要事先在 [阿里云控制台](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w) 中开通这个产品。

## SDK 获取和安装

### 使用 pip 安装(推荐)

```bash
pip install aliyun-python-sdk-core # 安装阿里云 SDK 核心库
pip install aliyun-python-sdk-ecs # 安装管理 ECS SDK
```

## 开始调用

以下这个代码示例向您展示了调用阿里云 Python SDK 的3个主要步骤：

1. 创建 Client 实例
2. 创建 API 请求并设置参数
3. 发起请求并处理异常


```python
# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# 创建 AcsClient 实例
client = AcsClient(
   "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>"
);
# 创建 request，并设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
# 发起 API 请求并打印返回
response = client.do_action_with_exception(request)
print response
```

在创建 Client 实例时，您需要填写 3 个参数：Region ID、Access Key ID 和 Access Key Secret。Access Key ID 和 Access Key Secret 可以从控制台获得；而 Region ID 可以从 [地域列表](https://help.aliyun.com/document_detail/40654.html) 中获得

## HTTP DEBUG
要使用 HTTP DEBUG 功能，需要在您的环境变量配置`DEBUG`，其对应的值可以为`sdk`或`SDK`。

**HTTP DEBUG**展现如下信息，帮助您调试代码：

```
> GET /databases?RegionId=cn-hangzhou HTTP/1.1
> Host : ads.cn-hangzhou.aliyuncs.com
> User-Agent : AlibabaCloud (Windows 10;AMD64) Python/3.7.1 Core/2.13.1 python-requests/2.18.1
> accept-encoding : *
> Accept : application/json
> Connection : keep-alive
> x-sdk-invoke-type : normal
> x-acs-version : 2019-01-22
> x-acs-region-id : cn-hangzhou
> Date : Thu, 21 Feb 2019 08:00:50 GMT
> x-acs-signature-method : HMAC-SHA1
> x-acs-signature-version : 1.0
> Authorization : acs ...
> x-sdk-client : python/2.0.0

< HTTP/1.1 503 SERVICE_UNAVAILABLE
< Date : Thu, 21 Feb 2019 08:00:50 GMT
< Content-Type : application/json; charset=UTF-8
< Content-Length : 297
< Connection : keep-alive
< Access-Control-Allow-Origin : *
< Access-Control-Allow-Methods : POST, GET, OPTIONS
< Access-Control-Allow-Headers : X-Requested-With, X-Sequence, _aop_secret, _aop_signature
< Access-Control-Max-Age : 172800
< x-acs-request-id : 670F3D09-F8E7-4144-83C3-B56C35DA35ED
< Server : Jetty(7.2.2.v20101205)
```
