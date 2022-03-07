import json
import requests
import uuid
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def poster():
    url = "https://localhost:9200/uuid_index/_doc"

    toAdd = str(uuid.uuid4())

    payload = json.dumps({
        "value" : toAdd
    })
    headers = {
        'Authorization': 'Basic ZWxhc3RpYzpFVC1SZHh4WFl4eHQqQzhZVGRyMw==',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,verify = False)
    print(toAdd,end= " : ")
    print(response.status_code)

for x in range(20000):
    print(x,end=" : ")
    poster()
