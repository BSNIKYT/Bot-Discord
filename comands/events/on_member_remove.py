@bot.event
async def on_member_remove(member):
    try:
      await member.send(f'Здравствуй,{member.mention}!')
    except HTTPError as e:
        if e.code == 403:
          print("Пользователь запретил отправлять сообщения ему в ЛС")
    try:
        msg = await member.send(embed=discord.Embed(
            color=colors['write'],
            title=
            f'Ты покинул(а) сервер {member.guild.name}\n\n ```Возможно тебя забанили, но проверь на всякий случай^^```',
            set_thumbnail=member.guild.icon),
                                components=[
                                    Button(style=ButtonStyle.blue,
                                           label=
                                           f"Send from ▶{member.guild.name}◀",
                                           emoji="📃",
                                           disabled=True),
                                ])
        responce = await bot.wait_for(
            'button_click', check=lambda message: message.author == ctx.author)
        if responce.component.label == 'Да':
            await responce.respond(content='Деньги успешно переведены!')
        else:
            await responce.respond(content='Вы отменили перевод.')
    except:
        embed = discord.Embed(
            color=colors['write'],
            title=
            f'Ты покинул(а) сервер {member.guild.name}\n\n ```Возможно тебя забанили, но проверь на всякий случай^^```',
            set_thumbnail=member.guild.icon)
        await member.send(embed=embed)
