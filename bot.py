import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Create a bot instance
intents = disnake.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run(TOKEN)
