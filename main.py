from fastapi import FastAPI
import requests
import json

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.get("/fetchEsConfig")
def getEsStats():
    url = "https://localhost:9200/"

    payload = {}
    headers = {
        'Authorization': 'Basic ZWxhc3RpYzpFVC1SZHh4WFl4eHQqQzhZVGRyMw=='
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload, verify=False)

    return json.loads(response.text)


@app.get("/fetchEsData")
def fetchEsData():
    url = "https://localhost:9200/test_index/_search"

    payload = json.dumps({
    })
    headers = {
        'Authorization': 'Basic ZWxhc3RpYzpFVC1SZHh4WFl4eHQqQzhZVGRyMw==',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    return json.loads(response.text)['hits']['hits']
