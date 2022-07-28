@bot.command()
@commands.guild_only()
async def invite(ctx):
    #Creating an invite link
    link = await ctx.channel.create_invite(xkcd=True, max_age=0, max_uses=0)
    #max_age = 0 The invite link will never exipre.
    #max_uses = 0 Infinite users can join throught the link.
    #-----------------------------------------------------#

    #-------Embed Time-----#
    em = discord.Embed(
        title=f"Join The {ctx.guild.name} Discord Server Now!",
        url=link,
        description=
        f"**{ctx.guild.member_count} Members** [**JOIN**]({link})\n\n**Invite link for {ctx.channel.mention} is created.**\nNumber of uses: **Infinite**\nLink Expiry Time: **Never**",
        color=colors['write'])

    #Embed Footer
    em.set_footer(text=f"Made by </iFreaku🔥YT>2.0#0908")

    #Embed Thumbnail Image
    em.set_thumbnail(url=ctx.guild.icon_url)

    #Embed Author
    em.set_author(name="INSTANT SERVER INVITE")
    #-----------------------------------------#
    await ctx.send(f"> {link}", embed=em)
