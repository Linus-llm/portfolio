import os
import re
from pathlib import Path

import requests


# --------------------------------------------------
# Configuration
# --------------------------------------------------

DIFY_BASE_URL = "https://api.dify.ai/v1"
KNOWLEDGE_BASE_NAME = "portfolio"

CONTENT_FOLDER = Path("content")

DIFY_API_KEY = os.environ["DIFY_API_KEY"]

HEADERS = {
    "Authorization": f"Bearer {DIFY_API_KEY}"
}


# --------------------------------------------------
# Dify API
# --------------------------------------------------

def get_datasets():
    url = f"{DIFY_BASE_URL}/datasets"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def find_dataset_id():
    datasets = get_datasets()

    for dataset in datasets["data"]:
        if dataset["name"].lower() == KNOWLEDGE_BASE_NAME.lower():
            return dataset["id"]

    raise RuntimeError(
        f'Could not find knowledge base "{KNOWLEDGE_BASE_NAME}"'
    )


def get_documents(dataset_id):
    url = f"{DIFY_BASE_URL}/datasets/{dataset_id}/documents"

    response = requests.get(
        url,
        headers=HEADERS,
        params={
            "limit": 100
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]


def create_document(dataset_id, name, text):
    url = (
        f"{DIFY_BASE_URL}/datasets/"
        f"{dataset_id}/document/create-by-text"
    )

    body = {
        "name": name,
        "text": text,
        "indexing_technique": "high_quality",
        "process_rule": {
            "mode": "automatic"
        }
    }

    response = requests.post(
        url,
        headers={
            **HEADERS,
            "Content-Type": "application/json"
        },
        json=body,
        timeout=60
    )

    if not response.ok:
        print()
        print("DIFY ERROR")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        print()

    response.raise_for_status()

    return response.json()


def update_document(dataset_id, document_id, name, text):
    url = (
        f"{DIFY_BASE_URL}/datasets/"
        f"{dataset_id}/documents/"
        f"{document_id}/update-by-text"
    )

    body = {
        "name": name,
        "text": text
    }

    response = requests.post(
        url,
        headers={
            **HEADERS,
            "Content-Type": "application/json"
        },
        json=body,
        timeout=60
    )

    if not response.ok:
        print()
        print("DIFY ERROR")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        print()

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# Markdown
# --------------------------------------------------

def get_markdown_files():
    return list(CONTENT_FOLDER.rglob("*.md"))


def get_document_name(file_path):
    relative_path = file_path.relative_to(CONTENT_FOLDER)

    return relative_path.as_posix()


def clean_markdown(text):
    # Remove YAML front matter
    text = re.sub(
        r"\A---\s*\n.*?\n---\s*\n",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove TOML front matter
    text = re.sub(
        r"\A\+\+\+\s*\n.*?\n\+\+\+\s*\n",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove self-contained Hugo shortcodes
    # Example: {{< youtube abc123 >}}
    text = re.sub(
        r"{{[<%].*?[>%]}}",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def read_markdown(file_path):
    text = file_path.read_text(encoding="utf-8")

    return clean_markdown(text)


# --------------------------------------------------
# Synchronization
# --------------------------------------------------

def sync():
    print("Finding Dify knowledge base...")

    dataset_id = find_dataset_id()

    print(f'Found "{KNOWLEDGE_BASE_NAME}"')
    print(f"Dataset ID: {dataset_id}")
    print()

    print("Getting existing Dify documents...")

    dify_documents = get_documents(dataset_id)

    documents_by_name = {
        document["name"]: document
        for document in dify_documents
    }

    print(f"Found {len(dify_documents)} existing Dify documents.")
    print()

    markdown_files = get_markdown_files()

    print(f"Found {len(markdown_files)} Markdown files.")
    print()

    created = 0
    updated = 0
    skipped = 0

    for file_path in markdown_files:

        document_name = get_document_name(file_path)
        text = read_markdown(file_path)

        print(f"Processing: {document_name}")

        if not text:
            print("  -> Skipped: document is empty")
            skipped += 1
            continue

        existing_document = documents_by_name.get(document_name)

        if existing_document is None:

            print("  -> Creating new document")

            create_document(
                dataset_id,
                document_name,
                text
            
            )

            created += 1

        else:

            print("  -> Updating existing document")

            update_document(
                dataset_id,
                existing_document["id"],
                document_name,
                text
            
            )

            updated += 1

    print()
    print("--------------------------------")
    print("Sync complete")
    print("--------------------------------")
    print(f"Created: {created}")
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")


# --------------------------------------------------
# Start
# --------------------------------------------------

if __name__ == "__main__":
    sync()