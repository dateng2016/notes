# Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

# Download the model that you want

To download the selected model, run the following command.

```bash
ollama pull <Your Preferred Model Name>
```

Model Names -> Number of parameters

deepseek-r1 -> 7b \
deepseek-r1:1.5b -> 1.5b \
deepseek-r1:8b -> 8b \
deepseek-r1:14b -> 14b \
deepseek-r1:32b -> 32b \
deepseek-r1:70b -> 70b \
deepseek-r1:14b -> 671b

# Running DeepSeek in your terminal

If you want to run your model in your terminal, execute the following command. It will give you an interactive shell where you can chat with your model.

```bash
ollama run <Your Preferred Model Name>
```

# Interacting with your model with Python

Below are some simple code to interact with your local model with python requests. You can also interact with your local model through ollama python module. Check the official documentation for more details.

```python

import requests

# Define the Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Define the payload for the request
payload = {
    "model": "deepseek-r1:1.5b",  # Name of the model
    "prompt": "What is the capital of France?",  # Your input prompt
    "stream": False,  # Set to True for streaming responses
}

# Send the request to Ollama
response = requests.post(OLLAMA_API_URL, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    response_data = response.json()
    print("Response from DeepSeek:", response_data.get("response"))
else:
    print(f"Failed to get response. Status code: {response.status_code}")
    print("Response:", response.text)

```
