import boto3
import json
import numpy as np

# Input must be a json
json_object = {
"Product Name": "Paracnnol 100 mg tablets",
"Company Name": "Johnson, Johnsohn solutions Pvt ltd",
"Standard": "IH, Pharmocopoeis reference, USDP?PH.Eur/IH",
"Market": "US and Europe",
"Specification No.": "QCD/SL/33000001/RO",
"Shelf life": "33 month",
"STP No.": "QCD/FP STP/660000001/RO",
"Effective Date": "Jan-2013",
"Supersedes": "--"
}
text= json.dumps(json_object)

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
