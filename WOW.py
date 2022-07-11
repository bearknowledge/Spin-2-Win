import asyncio
import random
import discord
from discord.ext import commands
from config import *



bot = commands.Bot(command_prefix=PREFIX, description = "WOW")

@bot.event
async def on_ready():
  print("live")


userlist = []
dailywinnerlist = []
weeklywinnerlist = []

@bot.command()
async def spin(ctx):
  if ctx.author in userlist:
    await ctx.send('You already spun today')
  else:
    userlist.append(ctx.author)
    await ctx.send("https://tenor.com/view/wheel-of-fortune-wheel-wof-game-show-jeopardy-gif-18038643")
    await asyncio.sleep(1)
    await ctx.send('Loading.', delete_after=.9)
    await asyncio.sleep(1)
    await ctx.send('Loading..', delete_after=.9)
    await asyncio.sleep(1)
    await ctx.send('Loading...', delete_after=.9)
    await asyncio.sleep(1)
    answer_list = ['See you tomorrow 😇', 'Try again tomorrow!', 'Try again tomorrow!', 'Try again tomorrow!','So close, yet so far...','If it was easy everyone would win','Here is a tip for next time, dont cross your fingers', 'See you tomorrow 😇', 'Try again tomorrow!', 'So close, yet so far...','If it was easy everyone would win','Here is a tip for next time, dont cross your fingers', 'See you tomorrow 😇','Gotta be quicker than that!', 'Try again tomorrow!', 'So close, yet so far...','If it was easy everyone would win','Here is a tip for next time, dont cross your fingers','See you tomorrow 😇','Gotta be quicker than that!', 'Try again tomorrow!','It`s your lucky day! You earned another spin','It`s your lucky day! You earned another spin', 'It`s your lucky day! You earned another spin', 'It`s your lucky day! You earned another spin','You just won 1 USDC!','You just won 1 USDC!','You just won 1 USDC!','You just won 1 USDC!','Pop! Goes the weasel. We have 5 USDC with your name on it 😎', 'That spin just earned you 10 USDC💰', 'Take your mom out to eat with the 20 USDC you just won!','Error...   Jk, You just won 30 USDC 🪙']
    answer = random.choice(answer_list)
    await ctx.send(answer)
    if answer in ['You just won 1 USDC!', 'Pop! Goes the weasel. We have 5 USDC with your name on it 😎','That spin just earned you 10 USDC💰','Take your mom out to eat with the 20 USDC you just won!','Error...   Jk, You just won 30 USDC 🪙']:
      dailywinnerlist.append((ctx.author.name)+(ctx.author.discriminator))
      weeklywinnerlist.append((ctx.author.name)+(ctx.author.discriminator))
    if answer == 'It`s your lucky day! You earned another spin':
      userlist.remove(ctx.author)

@bot.command()
async def rules(ctx):
  await ctx.send('Let`s play Wheel of Winners 🕹!\n\nHow to play:\n\n1.) Type "!spin" to spin the Wheel of Winners\n2.) Players are allowed to spin 1 time per day (M-F) unless they earn another spin as a prize\n3.) All winners will be recorded daily and prizes will be sent out on a weekly basis\n4.) There is an ongoing competition for the best submission for a response after a spin. If you are selected, you will receive 3 $POP! Send in your submissions in the "Submissions" Channel\n5.) Have fun and invite whoever you feel would enjoy Wheel of Winners!')

@bot.command()
async def winners(ctx):
  await ctx.send('Today`s winners:')
  await ctx.send(dailywinnerlist)

@bot.command()
async def new(ctx):
  userlist.clear()
  dailywinnerlist.clear()
  await ctx.send('New Game!')

@bot.command()
async def reset(ctx):
  userlist.clear()
  dailywinnerlist.clear()
  weeklywinnerlist.clear()
  await ctx.send('New Week!')



bot.run(TOKEN, bot=True, reconnect=True)