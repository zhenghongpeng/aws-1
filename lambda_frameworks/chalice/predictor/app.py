from chalice import Chalice
from chalice import BadRequestError
import base64, os, boto3, ast
import numpy as np
import json

app = Chalice(app_name='predictor')
app.debug=True

@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body

    if 'data' not in body:
        raise BadRequestError('Missing image data')
    if 'ENDPOINT_NAME' not in os.environ:
        raise BadRequestError('Missing endpoint')

    text = body['data'] 
    endpoint = os.environ['ENDPOINT_NAME']

    payload = {
    "text_inputs": f"what is 'Product Name' and company name {text}",
    "max_length": 50,
    "max_time": 50,
    "num_return_sequences": 1,
    "top_k": 1,
    "top_p": 1,
    "do_sample": True,
    }


    endpoint_name = 'jumpstart-example-huggingface-text2text-2023-05-09-16-58-04-093'
    runtime = boto3.Session().client(service_name='runtime.sagemaker',region_name='us-east-1')

    def query_endpoint_with_json_payload(encoded_json, endpoint_name):
        client = boto3.client("runtime.sagemaker")
        response = client.invoke_endpoint(
            EndpointName=endpoint_name, ContentType="application/json", Body=encoded_json
        )
        return response


    query_response = query_endpoint_with_json_payload(
        json.dumps(payload).encode("utf-8"), endpoint_name=endpoint_name
    )


    def parse_response_multiple_texts(query_response):
        model_predictions = json.loads(query_response["Body"].read())
        generated_text = model_predictions["generated_texts"]
        return generated_text


    # response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=payload)
    # print(response['Body'].read())

    generated_texts = parse_response_multiple_texts(query_response)
    print(generated_texts)
    return generated_texts

