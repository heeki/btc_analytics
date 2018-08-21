#!/bin/bash

################################################################################
# variables
################################################################################
PROFILE=1527


################################################################################
# pipeline
################################################################################
TEMPLATE=templates/pipeline.yaml
STACK=btc-analytics-pipeline
PARAMS=ParameterKey=ParamName,ParameterValue=btc-analytics
VERB=create-stack
aws --profile $PROFILE cloudformation $VERB \
--stack-name $STACK \
--template-body file://$TEMPLATE \
--parameters $PARAMS \
--capabilities CAPABILITY_IAM

aws --profile $PROFILE cloudformation describe-stack-resources --stack-name $STACK | jq -c '.["StackResources"][] | {type:.ResourceType, id:.PhysicalResourceId}'
#DDBROLE=$(aws --profile $PROFILE cloudformation describe-stacks --stack-name $STACK | jq -c '.["Stacks"][]["Outputs"][]  | select(.OutputKey == "OutDDBRole") | .OutputValue' | tr -d '"')
