@bot.event
async def on_message_delete(message):
    try:
        global logch
        z = bot.get_channel(logch)
        embed = discord.Embed(
            title=f"Сообщение {message.author} было удалено!",
            timestamp=datetime.datetime.now(),
            color=discord.Colour.red())
        embed.add_field(name="Автор", value=f"{message.author.mention}")
        embed.add_field(name="Канал сообщения:",
                        value=f"{message.channel.mention}")
        embed.add_field(name="Удалённое сообщение:",
                        value=f"**\n{message.content}**")
        embed.set_author(name=message.author.name,
                         icon_url=message.author.avatar_url)
        webhook2 = DiscordWebhook(
            url= "WEBHOOK_URL"
        )  #LOGS
        webhook2.add_embed(embed)
        webhook2.execute()
        await z.send(embed=embed)
    except:
        pass
