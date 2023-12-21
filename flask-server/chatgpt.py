import requests

# Set up API endpoint and parameters
url = 'https://api.chatgpt.com/gpt'
params = {
    'model': 'gpt2-medium',
    'prompt': 'Hello, how are you?',
    'length': 50
}

# Send API request and get response
response = requests.get(url, params=params)

# Print response
print(response.json()['text'])
