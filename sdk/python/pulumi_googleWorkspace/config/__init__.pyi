# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

accessToken: Optional[str]
"""
A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the `Authorization: Bearer`
token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores
the `scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
"""

credentials: Optional[str]
"""
Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud
Console). If not provided, the application default credentials will be used.
"""

customerId: Optional[str]
"""
The customer id provided with your Google Workspace subscription. It is found in the admin console under Account
Settings.
"""

impersonatedUserEmail: Optional[str]
"""
The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.
`impersonated_user_email` is required for all services except group and user management.
"""

oauthScopes: Optional[str]
"""
The list of the scopes required for your application (for a list of possible scopes, see [Authorize
requests](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing))
"""

serviceAccount: Optional[str]
"""
The service account used to create the provided `access_token` if authenticating using the `access_token` method and
needing to impersonate a user. This service account will require the GCP role `Service Account Token Creator` if needing
to impersonate a user.
"""

