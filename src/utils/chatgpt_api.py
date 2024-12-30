import os
import requests
import json


def summarize_pdf_with_chatgpt(pdf_path: str) -> str:
    """
    Summarizes the content of a PDF file using ChatGPT.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The summary of the PDF content.
    """
    config_path = os.path.join(os.path.dirname(__file__), "../../config.json")
    with open(config_path) as f:
        config = json.load(f)
        api_key = config["open_ai_key"]

    api_url = "https://api.openai.com/v1/files"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Upload the PDF file
    with open(pdf_path, "rb") as f:
        files = {"file": (pdf_path, f, "application/pdf")}
        response = requests.post(api_url, headers=headers, files=files)

    if response.status_code == 200:
        file_id = response.json()["id"]

        # Request summary using the uploaded file
        api_url = "https://api.openai.com/v1/chat/completions"
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Please summarize the content of the file with ID: {file_id}",
                }
            ],
            "max_tokens": 150,
        }
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            summary = response.json()["choices"][0]["message"]["content"]
            return summary
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
