# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GroupMembersArgs', 'GroupMembers']

@pulumi.input_type
class GroupMembersArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 members: Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]] = None):
        """
        The set of arguments for constructing a GroupMembers resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        :param pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]] members: The members of the group
        """
        pulumi.set(__self__, "group_id", group_id)
        if members is not None:
            pulumi.set(__self__, "members", members)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]]:
        """
        The members of the group
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]]):
        pulumi.set(self, "members", value)


@pulumi.input_type
class _GroupMembersState:
    def __init__(__self__, *,
                 etag: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]] = None):
        """
        Input properties used for looking up and filtering GroupMembers resources.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]] members: The members of the group
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if members is not None:
            pulumi.set(__self__, "members", members)

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
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

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
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]]:
        """
        The members of the group
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupMembersMemberArgs']]]]):
        pulumi.set(self, "members", value)


class GroupMembers(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupMembersMemberArgs']]]]] = None,
                 __props__=None):
        """
        Group Members resource manages Google Workspace Groups Members. Group Members resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleWorkspace as googleWorkspace

        sales_group = google_workspace.group.Group("salesGroup", email="sales@example.com")
        michael = google_workspace.User("michael",
            primary_email="michael.scott@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=google_workspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        frank = google_workspace.User("frank",
            primary_email="frank.scott@example.com",
            password="2095312189753de6ad47dfe20cbe97ec",
            hash_function="MD5",
            name=google_workspace.UserNameArgs(
                family_name="Scott",
                given_name="Frank",
            ))
        sales_group_members = google_workspace.group.GroupMembers("salesGroupMembers",
            group_id=sales_group.id,
            members=[
                google_workspace.group.GroupMembersMemberArgs(
                    email=michael.primary_email,
                    role="MANAGER",
                ),
                google_workspace.group.GroupMembersMemberArgs(
                    email=frank.primary_email,
                    role="MEMBER",
                ),
            ])
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:group/groupMembers:GroupMembers sales groups/01abcde23fg4h5i
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupMembersMemberArgs']]]] members: The members of the group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupMembersArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Group Members resource manages Google Workspace Groups Members. Group Members resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleWorkspace as googleWorkspace

        sales_group = google_workspace.group.Group("salesGroup", email="sales@example.com")
        michael = google_workspace.User("michael",
            primary_email="michael.scott@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=google_workspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        frank = google_workspace.User("frank",
            primary_email="frank.scott@example.com",
            password="2095312189753de6ad47dfe20cbe97ec",
            hash_function="MD5",
            name=google_workspace.UserNameArgs(
                family_name="Scott",
                given_name="Frank",
            ))
        sales_group_members = google_workspace.group.GroupMembers("salesGroupMembers",
            group_id=sales_group.id,
            members=[
                google_workspace.group.GroupMembersMemberArgs(
                    email=michael.primary_email,
                    role="MANAGER",
                ),
                google_workspace.group.GroupMembersMemberArgs(
                    email=frank.primary_email,
                    role="MEMBER",
                ),
            ])
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:group/groupMembers:GroupMembers sales groups/01abcde23fg4h5i
        ```

        :param str resource_name: The name of the resource.
        :param GroupMembersArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupMembersArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupMembersMemberArgs']]]]] = None,
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
            __props__ = GroupMembersArgs.__new__(GroupMembersArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["members"] = members
            __props__.__dict__["etag"] = None
            __props__.__dict__["id"] = None
        super(GroupMembers, __self__).__init__(
            'googleworkspace:group/groupMembers:GroupMembers',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            id: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupMembersMemberArgs']]]]] = None) -> 'GroupMembers':
        """
        Get an existing GroupMembers resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupMembersMemberArgs']]]] members: The members of the group
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupMembersState.__new__(_GroupMembersState)

        __props__.__dict__["etag"] = etag
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["id"] = id
        __props__.__dict__["members"] = members
        return GroupMembers(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence['outputs.GroupMembersMember']]]:
        """
        The members of the group
        """
        return pulumi.get(self, "members")

