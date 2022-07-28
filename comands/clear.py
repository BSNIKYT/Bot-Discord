@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    if amount == None:
        amount = 5
        await ctx.channel.purge(limit =  amount)
    else:
        await ctx.channel.purge(limit = amount)
    emb = discord.Embed(title='Удаление сообщений', color=0xff0300)
    emb.add_field(name='Ошибка:', value=f"Было удалено {amount} сообщений")
    await ctx.reply(embed=emb)
    net_blet = bot.get_emoji(946362147355627530)
    await ctx.message.add_reaction(net_blet)
