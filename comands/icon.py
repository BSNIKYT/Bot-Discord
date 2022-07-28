@bot.command()
async def icon(ctx, member: discord.Member):
    embed = discord.Embed(color=colors['write'], title='Иконка участника')
    embed.set_image(url=member.avatar_url)
    await ctx.reply(embed=embed)
