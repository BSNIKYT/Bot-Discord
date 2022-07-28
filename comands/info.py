@bot.command()
@commands.guild_only()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=":flag_ru:",
                          timestamp=datetime.datetime.utcnow(),
                          color=colors['write'])
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    top_role = str(ctx.author.top_role.mention)
    #    region = ("Возможности бота\nограничены\n(>100)")
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    #  if region == Russian
    embed.add_field(name="Server Owner", value=f"{owner}")
    embed.add_field(name="Member Count", value=f"{memberCount}")
    embed.add_field(name="Server Top Role", value=f"{top_role}")
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server ID", value=f"{id}")
    embed.add_field(name="Server Region", value=f"{region}")
    embed.set_thumbnail(url=f"{icon}")
    await ctx.send(embed=embed)
