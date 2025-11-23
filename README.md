# Path Finder MCP Server

This project hosts an MCP (Model Context Protocol) server designed to ingest remote GitHub repositories and generate an LLM-friendly version of the repository's content.

## Features
- Asynchronous ingestion of GitHub repositories.
- Generates summaries, directory trees, and content for repositories.
- Built using `FastMCP`.

## Prerequisites
- Python 3.11
- `uv` (Python package manager)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Path Finder
   ```

2. Install the required dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the MCP Server
To start the MCP server, run the following command:

```bash
uv run main.py
```

The server will start on `http://0.0.0.0:5000/sse` by default.

## Usage
The server provides an asynchronous tool to ingest GitHub repositories. Use the `async_ingest` endpoint to fetch summaries, directory trees, and content for a given repository URL.

### Example
```python
import requests

url = "http://0.0.0.0:5000/sse"
response = requests.post(url, json={"source": "https://github.com/example/repo"})

print(response.json())
```

## Project Structure
- `src/mcp/server.py`: Main server implementation.
- `requirements.txt`: Python dependencies.

## License
This project is licensed under the MIT License.
