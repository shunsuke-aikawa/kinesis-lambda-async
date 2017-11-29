# -*- coding: utf-8 -*-
import json
import base64
import time
from aws_lambda import AwsLambdaModule



def run(event, context):

    data_dict = {}
    data_dict['async_flag'] = True
    data_dict['data'] = []


    if 'async_flag' in event:
        # 非同期で呼び出される場合
        main(event['data'])

    else:
        # 非同期で呼び出す場合
        # キネシスストリームから起動した場合
        for record in event['Records']:

            # kinesisのデータを戻す
            kinesis_data = load_kinesis_data(record['kinesis']['data'])
            # 詰め替える
            data_dict['data'].append(kinesis_data)


        # 非同期で再帰呼び出し
        lambda_function = AwsLambdaModule()
        lambda_function.invoke_async(data_dict)





def main(data_):
    for data in data_:
        time.sleep(2)
        print(data)




def load_kinesis_data(data):
    """
    kinesisから受け取ったデータはエンコードされているため
    """
    payload = base64.b64decode(data)
    return json.loads(payload)
