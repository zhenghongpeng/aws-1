## Flan model endpoint can be updated in PREDICTOR lambda env name.


```
curl --location 'https://zq1h8b61i7.execute-api.us-east-1.amazonaws.com/api/' \
--header 'Content-Type: application/json' \
--data '{"data": {
"Product Name": "Paracnnol 100 mg tablets",
"Company Name": "Johnson, Johnsohn solutions Pvt ltd",
"Standard": "IH, Pharmocopoeis reference, USDP?PH.Eur/IH",
"Market": "US and Europe",
"Specification No.": "QCD/SL/33000001/RO",
"Shelf life": "33 month",
"STP No.": "QCD/FP STP/660000001/RO",
"Effective Date": "Jan-2013",
"Supersedes": "--"
}}'

```

response:

```
[
    "Paracnnol 100 mg tablets are manufactured by Johnson, Johnsohn solutions Pvt ltd."
]

```