def summarize_pdf_with_chatgpt(pdf_path):
    import requests

    api_url = "https://api.openai.com/v1/files"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY",
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
