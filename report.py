@bot.command()
@commands.guild_only()
async def report(ctx, *, text=None):
    try:
        if text != None:
            link = await ctx.channel.create_invite(xkcd=True,
                                                   max_age=0,
                                                   max_uses=0)
            owner = bot.get_user(485085685565620234)
            x = discord.Embed(title='**Report Error!**', color=colors['write'])
            x.add_field(name='Server:', value=ctx.guild.name, inline=False)
            x.add_field(name='ID of the Server:',
                        value=ctx.guild.id,
                        inline=False)
            x.add_field(name='Report:', value=text, inline=False)
            x.add_field(name='INVITE:',
                        value=f"[**JOIN**]({link})",
                        inline=False)

            x.set_thumbnail(url=ctx.guild.icon_url)
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            await owner.send(embed=x)
            #Developer
            net_blet = bot.get_emoji(946362122458234920)
            await ctx.message.add_reaction(net_blet)
            #reaction
            y = discord.Embed(title='**Report отравлен!**')
            y.add_field(name='Сервер:', value=ctx.guild.name, inline=False)
            y.add_field(name='ID сервера:', value=ctx.guild.id, inline=False)
            y.add_field(name='Вы отправили:', value=text, inline=False)
            y.set_thumbnail(url=ctx.guild.icon_url)
            y.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            y.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=y)
            files = []
            for attachment in ctx.message.attachments:
                await attachment.save(attachment.filename)

        else:
            y = discord.Embed(title='Ошибка!')
            y.add_field(name=f'**{ctx.author.display_name}**',
                        value='*Вы должны описать найденную вами ошибку.*')
            y.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=y)
    except AttributeError:
        y = discord.Embed(title='Ошибка!')
        y.add_field(
            name=f'**{ctx.author.display_name}**',
            value=
            '*Эту команду нужно прописывать на одном из серверов, где находится наш бот.*'
        )
        y.timestamp = datetime.datetime.utcnow()
        await ctx.author.reply(embed=y)
