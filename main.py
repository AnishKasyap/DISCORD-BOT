import discord
import requests
import json
import random



client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "hate"]

starter_encouragements = ["cheer up","hang in there!", "you are a grt person"]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready() :
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$motivate'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
   await message.channel.send(random.choice(starter_encouragements))

client.run('<your bot's token>')
