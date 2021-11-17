// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package googleWorkspace

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetRole(ctx *pulumi.Context, args *GetRoleArgs, opts ...pulumi.InvokeOption) (*GetRoleResult, error) {
	var rv GetRoleResult
	err := ctx.Invoke("googleworkspace:index/getRole:getRole", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRole.
type GetRoleArgs struct {
	// Name of the role.
	Name string `pulumi:"name"`
}

// A collection of values returned by getRole.
type GetRoleResult struct {
	// A short description of the role.
	Description string `pulumi:"description"`
	// ETag of the resource.
	Etag string `pulumi:"etag"`
	// ID of the role.
	Id string `pulumi:"id"`
	// Returns true if the role is a super admin role.
	IsSuperAdminRole bool `pulumi:"isSuperAdminRole"`
	// Returns true if this is a pre-defined system role.
	IsSystemRole bool `pulumi:"isSystemRole"`
	// Name of the role.
	Name string `pulumi:"name"`
	// The set of privileges that are granted to this role.
	Privileges []GetRolePrivilege `pulumi:"privileges"`
}

func GetRoleOutput(ctx *pulumi.Context, args GetRoleOutputArgs, opts ...pulumi.InvokeOption) GetRoleResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetRoleResult, error) {
			args := v.(GetRoleArgs)
			r, err := GetRole(ctx, &args, opts...)
			return *r, err
		}).(GetRoleResultOutput)
}

// A collection of arguments for invoking getRole.
type GetRoleOutputArgs struct {
	// Name of the role.
	Name pulumi.StringInput `pulumi:"name"`
}

func (GetRoleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRoleArgs)(nil)).Elem()
}

// A collection of values returned by getRole.
type GetRoleResultOutput struct{ *pulumi.OutputState }

func (GetRoleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRoleResult)(nil)).Elem()
}

func (o GetRoleResultOutput) ToGetRoleResultOutput() GetRoleResultOutput {
	return o
}

func (o GetRoleResultOutput) ToGetRoleResultOutputWithContext(ctx context.Context) GetRoleResultOutput {
	return o
}

// A short description of the role.
func (o GetRoleResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetRoleResult) string { return v.Description }).(pulumi.StringOutput)
}

// ETag of the resource.
func (o GetRoleResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v GetRoleResult) string { return v.Etag }).(pulumi.StringOutput)
}

// ID of the role.
func (o GetRoleResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRoleResult) string { return v.Id }).(pulumi.StringOutput)
}

// Returns true if the role is a super admin role.
func (o GetRoleResultOutput) IsSuperAdminRole() pulumi.BoolOutput {
	return o.ApplyT(func(v GetRoleResult) bool { return v.IsSuperAdminRole }).(pulumi.BoolOutput)
}

// Returns true if this is a pre-defined system role.
func (o GetRoleResultOutput) IsSystemRole() pulumi.BoolOutput {
	return o.ApplyT(func(v GetRoleResult) bool { return v.IsSystemRole }).(pulumi.BoolOutput)
}

// Name of the role.
func (o GetRoleResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetRoleResult) string { return v.Name }).(pulumi.StringOutput)
}

// The set of privileges that are granted to this role.
func (o GetRoleResultOutput) Privileges() GetRolePrivilegeArrayOutput {
	return o.ApplyT(func(v GetRoleResult) []GetRolePrivilege { return v.Privileges }).(GetRolePrivilegeArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRoleResultOutput{})
}
