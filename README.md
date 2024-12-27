# AI Paper Parser

This project is designed to fetch data from an XML API, parse the data to extract specific parameters, including the abstract. Download a PDF of the paper, and summarize its content using ChatGPT. Provide both the paper abstract and ChatGPT Summary to the user. This project utilized VSCode Copilot to explore and learn the capabilities of the tool.

## Project Structure

```
my-python-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── api
│   │   └── xml_api.py   # API call to fetch XML data
│   ├── parsers
│   │   ├── xml_parser.py # Parses XML data to extract parameters
│   │   └── pdf_parser.py # Parses PDF content and summarizes it
│   ├── utils
│   │   └── chatgpt_api.py # Interacts with ChatGPT for summarization
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-python-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Main Functionalities

- **Fetch XML Data**: The application makes an API call to retrieve XML data.
- **Parse XML Data**: Extracts title, id, published date, summary, and URLs from the XML response.
- **Download PDF**: Downloads the PDF of the paper for further analysis.
- **Summarize PDF**: Uses ChatGPT to generate a summary of the PDF content.

## License

This project is licensed under the MIT License.