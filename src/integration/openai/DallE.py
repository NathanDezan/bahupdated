import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.images.generate(
  model="dall-e-3",
  prompt="make a cover for page in notion must contain an article with the title Tuscan Kale",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# make a cover for page in notion must contain an article with the title "Tuscan Kale"