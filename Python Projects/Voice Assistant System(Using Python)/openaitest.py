import openai
# import os
# from openai import Completion

from config import apikey

# print(apikey)

openai.api_key=apikey


response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write a e-mail to my boss for resigniation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)