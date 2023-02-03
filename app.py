#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_pipeline.cdk_pipeline_stack import CdkPipelineStack


app = cdk.App()
CdkPipelineStack(app, "cdk-pipeline")

app.synth()
