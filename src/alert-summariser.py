import requests
import datetime

def log_response(prompt, response, path="./logs"):
    ct = datetime.datetime.now()
    ts = ct.timestamp()

    file_path=f"{path}/{ts}.md"
    text_response = ''
    if response.status_code == 200:
        text_response += response.json()["choices"][0]["message"]["content"]
    text_response = text_response

    with open(file_path, 'w') as text_file:
        text_file.write(f"# LOG\n\n## PROMPT\n{prompt}\n## RESPONSE\n### TEXT\n{text_response}\n### JSON\n```{response.json()}```\n ")

def call_gpt_api(prompt, api_key):

    # GPT 3 language model
    # url = "https://api.openai.com/v1/completions"
        # data = {
    #   "model": "text-davinci-003",
    #   "prompt": prompt,
    #   "max_tokens": 1000,
    #   "temperature": 0,
    #   "n": 1,
    #   "stream": False,
    #   "stop": None
    # }4

    # GPT 3.5 turbo
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
      "model": "gpt-3.5-turbo",
      "messages": [{"role": "user", "content": prompt}],
    #   "max_tokens": 4097,
      "temperature": 0,
      "n": 1,
    #   "stream": False,
    #   "stop": None
    }

    response = requests.post(url, json=data, headers=headers)
    log_response(prompt, response)

    print(f"RESPONSE: {separator}{response.json()}{separator}")
    if response.status_code == 200:
        # return response.json()["choices"][0]["text"] # GPT 3
        return response.json()["choices"][0]["message"]["content"] # GPT 3.5
    else:
        print(f"Error: API call failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    sep_char = "-"
    separator = f"\n{sep_char*70}\n"
    api_key = ""
    
    # read alert file
    with open('./inputs/pricing-alert.json', 'r') as file:
        alert = file.read().replace('\n', '').replace(' ', '')
    
    # read example cdk
    with open('./inputs/cdk-example2.ts', 'r') as file:
        cdk = file.read()
    
    prompt = f"""
Acting as a Senior DevOps Engineer, I want you to analyse this cloudwatch alarm:\n```\n{alert}\n```\n
and this typescript CDK code that defines the failing lambda\n```\n{cdk}\n```
and write a typescript code change to the lambda definition.
"""

    print(f"PROMPT:{separator}{prompt}{separator}")

    result = call_gpt_api(prompt, api_key)
    if result:
        print(f"GENERATED TEXT:{separator}{result}{separator}")
