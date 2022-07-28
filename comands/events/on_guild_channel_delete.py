@bot.event
async def on_guild_channel_delete(channel):
    try:
        global logch
        z = bot.get_channel(logch)
        embed = discord.Embed(title=f"{channel.name} был удален",
                              timestamp=datetime.datetime.now(),
                              color=discord.Colour.red())
        await z.send(embed=embed)
    except:
        pass
