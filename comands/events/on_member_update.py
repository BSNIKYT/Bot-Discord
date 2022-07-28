@bot.event
async def on_member_update(before, after):
    try:
        global logch
        z = bot.get_channel(logch)
        if len(before.roles) > len(after.roles):
            role = next(role for role in before.roles
                        if role not in after.roles)
            embed = discord.Embed(
                title=f"{before}'s Role has Been Removed",
                description=f"{role.name} was removed from {before.mention}.",
                timestamp=datetime.datetime.now(),
                color=discord.Colour.red())
        elif len(after.roles) > len(before.roles):
            role = next(role for role in after.roles
                        if role not in before.roles)
            embed = discord.Embed(
                title=f"{before} Got a New Role",
                description=f"{role.name} was added to {before.mention}.",
                timestamp=datetime.datetime.now(),
                color=discord.Colour.green())
        elif before.nick != after.nick:
            embed = discord.Embed(
                title=f"{before}'s Nickname Changed",
                description=f"Before: {before.nick}\nAfter: {after.nick}",
                timestamp=datetime.datetime.now(),
                color=discord.Colour.blue())
        else:
            return
        embed.set_author(name=after.name, icon_url=after.display_avatar)
        await z.send(embed=embed)
    except:
        pass

