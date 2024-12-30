import os
import requests
import json


def summarize_pdf_with_chatgpt(pdf_text: str) -> str:
    """
    Summarizes the content of a PDF file using ChatGPT.

    Args:
        pdf_text (str): The path to the PDF file.

    Returns:
        str: The summary of the PDF content.
    """
    config_path = os.path.join(os.path.dirname(__file__), "../../config.json")
    with open(config_path) as f:
        config = json.load(f)
        api_key = config["open_ai_key"]

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": f"Please summarize the following text 150 tokens or lower:\n\n{pdf_text}",
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
