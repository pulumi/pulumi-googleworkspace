# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ChromePolicyArgs', 'ChromePolicy']

@pulumi.input_type
class ChromePolicyArgs:
    def __init__(__self__, *,
                 org_unit_id: pulumi.Input[str],
                 policies: pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]):
        """
        The set of arguments for constructing a ChromePolicy resource.
        :param pulumi.Input[str] org_unit_id: The target org unit on which this policy is applied.
        :param pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]] policies: Policies to set for the org unit
        """
        pulumi.set(__self__, "org_unit_id", org_unit_id)
        pulumi.set(__self__, "policies", policies)

    @property
    @pulumi.getter(name="orgUnitId")
    def org_unit_id(self) -> pulumi.Input[str]:
        """
        The target org unit on which this policy is applied.
        """
        return pulumi.get(self, "org_unit_id")

    @org_unit_id.setter
    def org_unit_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_unit_id", value)

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]:
        """
        Policies to set for the org unit
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]):
        pulumi.set(self, "policies", value)


@pulumi.input_type
class _ChromePolicyState:
    def __init__(__self__, *,
                 org_unit_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]] = None):
        """
        Input properties used for looking up and filtering ChromePolicy resources.
        :param pulumi.Input[str] org_unit_id: The target org unit on which this policy is applied.
        :param pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]] policies: Policies to set for the org unit
        """
        if org_unit_id is not None:
            pulumi.set(__self__, "org_unit_id", org_unit_id)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)

    @property
    @pulumi.getter(name="orgUnitId")
    def org_unit_id(self) -> Optional[pulumi.Input[str]]:
        """
        The target org unit on which this policy is applied.
        """
        return pulumi.get(self, "org_unit_id")

    @org_unit_id.setter
    def org_unit_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_unit_id", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]]:
        """
        Policies to set for the org unit
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChromePolicyPolicyArgs']]]]):
        pulumi.set(self, "policies", value)


class ChromePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 org_unit_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChromePolicyPolicyArgs']]]]] = None,
                 __props__=None):
        """
        Create a ChromePolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] org_unit_id: The target org unit on which this policy is applied.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChromePolicyPolicyArgs']]]] policies: Policies to set for the org unit
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChromePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ChromePolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ChromePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChromePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 org_unit_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChromePolicyPolicyArgs']]]]] = None,
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
            __props__ = ChromePolicyArgs.__new__(ChromePolicyArgs)

            if org_unit_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_unit_id'")
            __props__.__dict__["org_unit_id"] = org_unit_id
            if policies is None and not opts.urn:
                raise TypeError("Missing required property 'policies'")
            __props__.__dict__["policies"] = policies
        super(ChromePolicy, __self__).__init__(
            'googleworkspace:index/chromePolicy:ChromePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            org_unit_id: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChromePolicyPolicyArgs']]]]] = None) -> 'ChromePolicy':
        """
        Get an existing ChromePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] org_unit_id: The target org unit on which this policy is applied.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChromePolicyPolicyArgs']]]] policies: Policies to set for the org unit
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChromePolicyState.__new__(_ChromePolicyState)

        __props__.__dict__["org_unit_id"] = org_unit_id
        __props__.__dict__["policies"] = policies
        return ChromePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="orgUnitId")
    def org_unit_id(self) -> pulumi.Output[str]:
        """
        The target org unit on which this policy is applied.
        """
        return pulumi.get(self, "org_unit_id")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence['outputs.ChromePolicyPolicy']]:
        """
        Policies to set for the org unit
        """
        return pulumi.get(self, "policies")

