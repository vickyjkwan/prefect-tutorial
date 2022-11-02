import requests
from prefect import flow, task
import os

@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@task
def parse_fact(response):
    fact = response["fact"]
    return fact

@flow(name="test flow",
    # version=os.getenv("GIT_COMMIT_SHA"))
    version="tutorial_02")
def api_flow(url):
    fact_json = call_api(url)
    fact_text = parse_fact(fact_json)
    return fact_text

print(api_flow("https://catfact.ninja/fact"))


