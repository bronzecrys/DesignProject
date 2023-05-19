import os
import openai
# try out openAI by downloading it via pip install openai

openai.api_key = "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"
print(openai.__version__)
response = openai.Completion.create(
  engine='davinci',
  prompt='Could you tell me what version of the API I am using?',
  temperature = 0.4,
  max_tokens=50
)

print(response)
image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")