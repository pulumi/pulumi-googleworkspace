# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DomainAliasArgs', 'DomainAlias']

@pulumi.input_type
class DomainAliasArgs:
    def __init__(__self__, *,
                 domain_alias_name: pulumi.Input[str],
                 parent_domain_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DomainAlias resource.
        :param pulumi.Input[str] domain_alias_name: The domain alias name.
        :param pulumi.Input[str] parent_domain_name: The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        pulumi.set(__self__, "domain_alias_name", domain_alias_name)
        if parent_domain_name is not None:
            pulumi.set(__self__, "parent_domain_name", parent_domain_name)

    @property
    @pulumi.getter(name="domainAliasName")
    def domain_alias_name(self) -> pulumi.Input[str]:
        """
        The domain alias name.
        """
        return pulumi.get(self, "domain_alias_name")

    @domain_alias_name.setter
    def domain_alias_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_alias_name", value)

    @property
    @pulumi.getter(name="parentDomainName")
    def parent_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        return pulumi.get(self, "parent_domain_name")

    @parent_domain_name.setter
    def parent_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_domain_name", value)


@pulumi.input_type
class _DomainAliasState:
    def __init__(__self__, *,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 domain_alias_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 parent_domain_name: Optional[pulumi.Input[str]] = None,
                 verified: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering DomainAlias resources.
        :param pulumi.Input[int] creation_time: Creation time of the domain alias.
        :param pulumi.Input[str] domain_alias_name: The domain alias name.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] parent_domain_name: The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        :param pulumi.Input[bool] verified: Indicates the verification state of a domain alias.
        """
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if domain_alias_name is not None:
            pulumi.set(__self__, "domain_alias_name", domain_alias_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if parent_domain_name is not None:
            pulumi.set(__self__, "parent_domain_name", parent_domain_name)
        if verified is not None:
            pulumi.set(__self__, "verified", verified)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        Creation time of the domain alias.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="domainAliasName")
    def domain_alias_name(self) -> Optional[pulumi.Input[str]]:
        """
        The domain alias name.
        """
        return pulumi.get(self, "domain_alias_name")

    @domain_alias_name.setter
    def domain_alias_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_alias_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="parentDomainName")
    def parent_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        return pulumi.get(self, "parent_domain_name")

    @parent_domain_name.setter
    def parent_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_domain_name", value)

    @property
    @pulumi.getter
    def verified(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates the verification state of a domain alias.
        """
        return pulumi.get(self, "verified")

    @verified.setter
    def verified(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verified", value)


class DomainAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_alias_name: Optional[pulumi.Input[str]] = None,
                 parent_domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Domain Alias resource manages Google Workspace Domain Aliases. Domain Alias resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleWorkspace as googleWorkspace

        example = google_workspace.domain.DomainAlias("example",
            domain_alias_name="alias-example.com",
            parent_domain_name="example.com")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:domain/domainAlias:DomainAlias example alias-example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_alias_name: The domain alias name.
        :param pulumi.Input[str] parent_domain_name: The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Domain Alias resource manages Google Workspace Domain Aliases. Domain Alias resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleWorkspace as googleWorkspace

        example = google_workspace.domain.DomainAlias("example",
            domain_alias_name="alias-example.com",
            parent_domain_name="example.com")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:domain/domainAlias:DomainAlias example alias-example.com
        ```

        :param str resource_name: The name of the resource.
        :param DomainAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_alias_name: Optional[pulumi.Input[str]] = None,
                 parent_domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainAliasArgs.__new__(DomainAliasArgs)

            if domain_alias_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_alias_name'")
            __props__.__dict__["domain_alias_name"] = domain_alias_name
            __props__.__dict__["parent_domain_name"] = parent_domain_name
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["id"] = None
            __props__.__dict__["verified"] = None
        super(DomainAlias, __self__).__init__(
            'googleworkspace:domain/domainAlias:DomainAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            domain_alias_name: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            id: Optional[pulumi.Input[str]] = None,
            parent_domain_name: Optional[pulumi.Input[str]] = None,
            verified: Optional[pulumi.Input[bool]] = None) -> 'DomainAlias':
        """
        Get an existing DomainAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] creation_time: Creation time of the domain alias.
        :param pulumi.Input[str] domain_alias_name: The domain alias name.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] parent_domain_name: The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        :param pulumi.Input[bool] verified: Indicates the verification state of a domain alias.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainAliasState.__new__(_DomainAliasState)

        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["domain_alias_name"] = domain_alias_name
        __props__.__dict__["etag"] = etag
        __props__.__dict__["id"] = id
        __props__.__dict__["parent_domain_name"] = parent_domain_name
        __props__.__dict__["verified"] = verified
        return DomainAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation time of the domain alias.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="domainAliasName")
    def domain_alias_name(self) -> pulumi.Output[str]:
        """
        The domain alias name.
        """
        return pulumi.get(self, "domain_alias_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentDomainName")
    def parent_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
        """
        return pulumi.get(self, "parent_domain_name")

    @property
    @pulumi.getter
    def verified(self) -> pulumi.Output[bool]:
        """
        Indicates the verification state of a domain alias.
        """
        return pulumi.get(self, "verified")

