import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # To receive member join events

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Send welcome message in the #welcome channel
    channel = discord.utils.get(member.guild.text_channels, name='welcome')
    if channel:
        await channel.send(f'Hey {member.mention}, welcome to the server! 👋')

    # Send announcement in #announcements channel
    ann_channel = discord.utils.get(member.guild.text_channels, name='announcements')
    if ann_channel:
        await ann_channel.send(f'{member.mention} just joined the server! 🎉')

bot.run('MTM3NzY1MjA2MDM0NTg2NDM2NQ.GKLZ1h.voQ1nu5oiT6mUIKJnDpeGKIeQK5oKOxfUymnms')
