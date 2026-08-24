import os
import requests


DIFY_BASE_URL = "https://api.dify.ai/v1"
KNOWLEDGE_BASE_NAME = "portfolio"

DIFY_API_KEY = os.environ["DIFY_API_KEY"]


def get_datasets():
    url = f"{DIFY_BASE_URL}/datasets"

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()


def find_dataset_id(datasets):
    for dataset in datasets["data"]:
        if dataset["name"].lower() == KNOWLEDGE_BASE_NAME.lower():
            return dataset["id"]

    return None


datasets = get_datasets()
dataset_id = find_dataset_id(datasets)

if dataset_id is None:
    print(f'Could not find knowledge base "{KNOWLEDGE_BASE_NAME}"')
else:
    print(f'Found knowledge base "{KNOWLEDGE_BASE_NAME}"')
    print(f"Dataset ID: {dataset_id}")