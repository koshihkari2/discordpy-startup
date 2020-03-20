from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def play(ctx):
    await ctx.send('!p only my railgun\n!p sister’s noise\n!p Level5judgelight\n
                    !p no buts\n!p dear my friend とある\n!p PSI missing\n
                    !p final phase\n!p future gazer\n!p eternal reality fripside')


bot.run(token)
