import os
import openai


openai.api_key = "Open AI Key Here"
print(openai.__version__)
response = openai.Completion.create(
  engine='davinci',
  prompt='Are Computer Engineers far superior to Electrial Engineers?',
  temperature = 0.4,
  max_tokens=50
)

print(response)
image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")