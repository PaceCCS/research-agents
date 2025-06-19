# Browser Use Demo

A simple demo application using Browser Use to automate web browsing tasks with AI.

## Setup

### Secrets

Make a .env

OPENAI_API_KEY= <get the key from [here](https://portal.azure.com/#@paceflowassurance.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Secret/https://pacesecrets.vault.azure.net/secrets/OpenAiApiKey)>

### Prerequisites
- Python 3.11 or higher
- uv package manager (recommended) or pip

### Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   # Using uv (recommended)
   uv venv --python 3.11
   source .venv/bin/activate  # Mac/Linux
   # or
   .venv\Scripts\activate     # Windows

   # Or using pip
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   # Using uv
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   # Using uv
   uv run playwright install

   playwright install
   ```

5. Set up environment variables:
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

Run the demo:
```bash
python main.py
```

The agent will search for Pace CCS office addresses and display the results.

## Configuration

You can modify the task in `main.py` by changing the `task` parameter in the Agent initialization.
