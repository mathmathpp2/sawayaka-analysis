import os
from datetime import datetime

import boto3
import requests

s3 = boto3.resource("s3")

API_ENDPOINT = os.environ["API_ENDPOINT"]


def fetch(start=1, limit=20):
    return requests.get(
        API_ENDPOINT,
        headers={
            "Accept": "application/json",
        },
        params=(
            ("start", start),
            ("limit", limit),
        ),
    )


def save(response, save_path):
    print(f"Saving to {save_path}")
    with open(save_path, mode="a") as f:
        f.write(response.text + "\n")
    return save_path


def upload(local_path, upload_path):
    print(f"Uploading to {upload_path}")
    s3.meta.client.upload_file(local_path, "my-bucket", upload_path)


def lambda_handler(event, context):
    time = str(datetime.now().strftime("%Y%m%d_%w_%H%M%S"))
    save_path = f"/tmp/sawayaka_response_{time}.jsonl"
    upload_path = os.path.join("data", os.path.basename(save_path))

    start = 1
    try:
        while True:
            response = fetch(start)
            save(response, save_path)
            start += 20
            if start > response.json()["innerDto"]["totalCount"]:
                break
        upload(save_path, upload_path)
    except:
        import traceback

        traceback.print_exc()
