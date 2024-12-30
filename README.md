# AI Paper Parser

This project is designed to fetch data from an XML API, parse the data to extract specific parameters, including the abstract. Download a PDF of the paper, and summarize its content using ChatGPT. Provide both the paper abstract and ChatGPT Summary to the user. This project utilized VSCode Copilot to explore and learn the capabilities of the tool.

## Project Structure

```
ai_paper_parser
├── src
│   ├── main.py              # Entry point of the application
│   ├── api
│   │   └── xml_api.py       # API call to fetch XML data
│   ├── parsers
│   │   ├── xml_parser.py    # Parses XML data to extract parameters
│   ├── utils
│   │   ├── chatgpt_api.py   # Interacts with ChatGPT for summarization
│   │   ├── download_pdf.py  # Downloads PDF files
│   │   └── pdf_parser.py    # Parses PDF content and extracts text
├── requirements.txt         # Project dependencies
├── config.json              # Configuration file for API keys
└── README.md                # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai_paper_parser
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to the `config.json` file:
   ```json
   {
       "open_ai_key": "YOUR_API_KEY"
   }
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
- **Parse PDF**: Extracts text content from the downloaded PDF.
- **Summarize PDF**: Uses ChatGPT to generate a summary of the PDF content.

## License

This project is licensed under the MIT License.

## Example Run
```
$ python src/main.py
[{'id': 'http://arxiv.org/abs/2412.18601v1',
  'published_date': '2024-12-24T18:56:00Z',
  'summary': '  In the rapidly evolving landscape of GameFi, a fusion of '
             'gaming and\n'
             'decentralized finance (DeFi), there exists a critical need to '
             'enhance player\n'
             'engagement and economic interaction within gaming ecosystems. '
             'Our GameFi\n'
             'ecosystem aims to fundamentally transform this landscape by '
             'integrating\n'
             'advanced embodied AI agents into GameFi platforms. These AI '
             'agents, developed\n'
             'using cutting-edge large language models (LLMs), such as GPT-4 '
             'and Claude AI,\n'
             'are capable of proactive, adaptive, and contextually rich '
             'interactions with\n'
             'players. By going beyond traditional scripted responses, these '
             'agents become\n'
             "integral participants in the game's narrative and economic "
             'systems, directly\n'
             'influencing player strategies and in-game economies. We address '
             'the limitations\n'
             'of current GameFi platforms, which often lack immersive AI '
             'interactions and\n'
             'mechanisms for community engagement or creator monetization. '
             'Through the deep\n'
             'integration of AI agents with blockchain technology, we '
             'establish a\n'
             'consensus-driven, decentralized GameFi ecosystem. This ecosystem '
             'empowers\n'
             'creators to monetize their contributions and fosters democratic '
             'collaboration\n'
             'among players and creators. Furthermore, by embedding DeFi '
             'mechanisms into the\n'
             'gaming experience, we enhance economic participation and provide '
             'new\n'
             'opportunities for financial interactions within the game. Our '
             'approach enhances\n'
             'player immersion and retention and advances the GameFi ecosystem '
             'by bridging\n'
             'traditional gaming with Web3 technologies. By integrating '
             'sophisticated AI and\n'
             'DeFi elements, we contribute to the development of more '
             'engaging, economically\n'
             'robust, and community-centric gaming environments. This project '
             'represents a\n'
             'significant advancement in the state-of-the-art in GameFi, '
             'offering insights\n'
             'and methodologies that can be applied throughout the gaming '
             'industry.\n',
  'title': 'Decentralized Intelligence in GameFi: Embodied AI Agents and the\n'
           '  Convergence of DeFi and Virtual Ecosystems',
  'url': 'http://arxiv.org/pdf/2412.18601v1'}]
  
ChatGPT Summary: The text discusses the integration of advanced embodied AI agents in the GameFi sector, merging gaming with decentralized finance (DeFi). The proposed system addresses the limitations of current GameFi platforms, such as lack of immersive AI interactions and insufficient community engagement. By utilizing large language models (like GPT-4), the AI agents provide adaptive and personalized gameplay experiences while enhancing economic participation through deeper DeFi mechanisms. The project aims to foster collaboration among creators and players while overcoming technical challenges of scalability and decentralization in blockchain environments. Overall, it aims to create more engaging and economically viable gaming ecosystems.
```