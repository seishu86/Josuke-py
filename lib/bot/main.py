from dotenv import load_dotenv
from discord.ext import commands
from discord import Embed, File
from glob import glob
import requests, json, os

client = commands.Bot(command_prefix = '.')
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

#Set up block 
#        **START**
async def on_connect(self):
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

#specific keyword prompt
@client.listen('on_message')
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('quote'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if msg.startswith('test'):
        await message.channel.send('I am fully functional!')
    
    if msg.startswith('jojo'):
        #await message.channel.send("Ora ora ora!")
        await message.channel.send(file=File("data\jojo\image1.gif"))

    if msg.startswith('bastard'):
        #await message.channel.send("Ora ora ora!")
        await message.channel.send(file=File("data\jojo\uncleshady.gif"))


#get function
def get_quote():
    response = requests.get("Https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

load_dotenv()
client.run(os.environ.get("SECRET_KEY"))