# -*- coding: utf-8 -*-
import os
import json
import boto3




class AwsLambdaModule(object):



    def __init__(self):
        self.client = boto3.client('lambda')
        self.function_name = os.environ.get('AWS_LAMBDA_FUNCTION_NAME')



    def invoke_async(self, data):
        """
        lambdaを非同期呼び出し
        """
        if self.function_name is None:
            return

        print('### Asynchronous execution ###')
        self.client.invoke(
            FunctionName=self.function_name,
            InvocationType="Event",
            Payload=json.dumps(data)
        )


