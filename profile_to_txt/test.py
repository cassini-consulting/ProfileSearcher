from reader import *
import requests
import json

headers = {"Ocp-Apim-Subscription-Key": "222a089a07714a65bcd309f9a2434ffa",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "cache-control": "no-cache",
    "Postman-Token": "45a3c16d-12a7-445c-8ace-545d219cbff7"
    }

with open("input.json", "r") as f:
    data = json.loads(f.read())

url = "https://profilekeywords.cognitiveservices.azure.com/text/analytics/v2.1/keyPhrases"

eq = requests.Request('POST', url, headers = headers, json = data)
prepared = eq.prepare()

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

pretty_print_POST(prepared)

r = requests.post(url, headers=headers, json = data)
print(r.status_code, r.reason)
print(r.content.decode('utf8'))
