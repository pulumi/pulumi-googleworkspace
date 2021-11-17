# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDomainAliasResult',
    'AwaitableGetDomainAliasResult',
    'get_domain_alias',
    'get_domain_alias_output',
]

@pulumi.output_type
class GetDomainAliasResult:
    """
    A collection of values returned by getDomainAlias.
    """
    def __init__(__self__, creation_time=None, domain_alias_name=None, etag=None, id=None, parent_domain_name=None, verified=None):
        if creation_time and not isinstance(creation_time, int):
            raise TypeError("Expected argument 'creation_time' to be a int")
        pulumi.set(__self__, "creation_time", creation_time)
        if domain_alias_name and not isinstance(domain_alias_name, str):
            raise TypeError("Expected argument 'domain_alias_name' to be a str")
        pulumi.set(__self__, "domain_alias_name", domain_alias_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parent_domain_name and not isinstance(parent_domain_name, str):
            raise TypeError("Expected argument 'parent_domain_name' to be a str")
        pulumi.set(__self__, "parent_domain_name", parent_domain_name)
        if verified and not isinstance(verified, bool):
            raise TypeError("Expected argument 'verified' to be a bool")
        pulumi.set(__self__, "verified", verified)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> int:
        """
        Creation time of the domain alias.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="domainAliasName")
    def domain_alias_name(self) -> str:
        """
        The domain alias name.
        """
        return pulumi.get(self, "domain_alias_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentDomainName")
    def parent_domain_name(self) -> str:
        """
        The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        return pulumi.get(self, "parent_domain_name")

    @property
    @pulumi.getter
    def verified(self) -> bool:
        """
        Indicates the verification state of a domain alias.
        """
        return pulumi.get(self, "verified")


class AwaitableGetDomainAliasResult(GetDomainAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainAliasResult(
            creation_time=self.creation_time,
            domain_alias_name=self.domain_alias_name,
            etag=self.etag,
            id=self.id,
            parent_domain_name=self.parent_domain_name,
            verified=self.verified)


def get_domain_alias(domain_alias_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainAliasResult:
    """
    Use this data source to access information about an existing resource.

    :param str domain_alias_name: The domain alias name.
    """
    __args__ = dict()
    __args__['domainAliasName'] = domain_alias_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('googleworkspace:index/getDomainAlias:getDomainAlias', __args__, opts=opts, typ=GetDomainAliasResult).value

    return AwaitableGetDomainAliasResult(
        creation_time=__ret__.creation_time,
        domain_alias_name=__ret__.domain_alias_name,
        etag=__ret__.etag,
        id=__ret__.id,
        parent_domain_name=__ret__.parent_domain_name,
        verified=__ret__.verified)


@_utilities.lift_output_func(get_domain_alias)
def get_domain_alias_output(domain_alias_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainAliasResult]:
    """
    Use this data source to access information about an existing resource.

    :param str domain_alias_name: The domain alias name.
    """
    ...
