// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleWorkspace.Outputs
{

    [OutputType]
    public sealed class GetUserRelationResult
    {
        public readonly string CustomType;
        public readonly string Type;
        public readonly string Value;

        [OutputConstructor]
        private GetUserRelationResult(
            string customType,

            string type,

            string value)
        {
            CustomType = customType;
            Type = type;
            Value = value;
        }
    }
}
