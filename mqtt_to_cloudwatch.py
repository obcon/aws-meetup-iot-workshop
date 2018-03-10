import json
import boto3

CLOUDWATCH = boto3.client('cloudwatch')


def lambda_handler(event, context):
    print(json.dumps(event))

    response = CLOUDWATCH.put_metric_data(
        Namespace='iot-ws',
        MetricData=[
            {
                'MetricName': "iot-sample-value",
                'Value': event.get('value', 0),
                'Unit': 'Count'
            },
        ]
    )
