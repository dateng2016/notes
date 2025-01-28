Most of the information in this doc come from this website: https://dev.to/nodeshiftcloud/a-step-by-step-guide-to-install-deepseek-r1-locally-with-ollama-vllm-or-transformers-44a1

# Ollama

Ollama is a user-friendly option for quickly running DeepSeek-R1 locally with minimal configuration. It's best suited for individuals or small-scale projects that don't require extensive optimization or scaling.

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Download the model that you want

To download the selected model, run the following command.

```bash
ollama pull <Your Preferred Model Name>
```

Model Names -> Number of parameters

deepseek-r1 -> 7b \
deepseek-r1:1.5b -> 1.5b \
deepseek-r1:7b -> 7b \
deepseek-r1:8b -> 8b \
deepseek-r1:14b -> 14b \
deepseek-r1:32b -> 32b \
deepseek-r1:70b -> 70b \
deepseek-r1:14b -> 671b

## Running DeepSeek in your terminal

If you want to run your model in your terminal, execute the following command. It will give you an interactive shell where you can chat with your model. This will also automatically download the model for you if you do not have it on your local machine already.

```bash
ollama run <Your Preferred Model Name>
```

## Interacting with your model with Python

Below are some simple code to interact with your local model with python requests. You can also interact with your local model through other python modules such as `openai`, `ollama`, etc. Check the official documentation for more details.

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
    ## Parse the response
    response_data = response.json()
    print("Response from DeepSeek:", response_data.get("response"))
else:
    print(f"Failed to get response. Status code: {response.status_code}")
    print("Response:", response.text)

```

---

# I have not been able to install models through the vLLM

# vLLM

vLLM is designed for efficient inference with optimized memory usage and high throughput, which makes it ideal for production environments. Choose this if you need to serve large-scale applications with performance and cost efficiency in mind.

## Install Rust and Cargo packages as dependencies for vLLM using rustup.

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

After running the command, start a new terminal to test if they are installed properly

## Install vLLM

Before install this, activate a virtual env if you'd like.

```bash
pip install vllm
```

## Install the DeepSeek model

```bash
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" --max_model 4096
```

The possible model names are:

deepseek-ai/DeepSeek-R1 \
deepseek-ai/DeepSeek-R1-Zero \
deepseek-ai/DeepSeek-R1-Distill-Llama-70B \
deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \
deepseek-ai/DeepSeek-R1-Distill-Llama-8B \
deepseek-ai/DeepSeek-R1-Distill-Qwen-7B \
deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

## Use terminal to test out your model

```bash
curl -X POST "http://localhost:8000/v1/chat/completions" \
    -H "Content-Type: application/json" \
    --data '{
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "user",
                "content": "Tell me the recipe for tea"
            }
        ]
    }'
```

# Transformers

Transformers offers maximum flexibility and control for fine-tuning and experimenting with DeepSeek-R1. It's the best choice for developers and researchers who need to customize models for their specific use cases and experiment with various training or inference configurations

## Install the dependencies

```bash
pip install transformers accelerate
```

## test

```python
# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "How can you help me?"},
]
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
pipe(messages)
```
