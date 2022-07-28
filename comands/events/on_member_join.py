@bot.event
async def on_member_join(member):
    global welch
    global logch
    try:
      await member.send(f'Здравствуй,{member.mention}!')
    except HTTPError as e:
        if e.code == 403:
          print("Пользователь запретил отправлять сообщения ему в ЛС")
    msg = await member.send(embed=discord.Embed(
        color=colors['write'],
        title=
        f'Здравствуй, {member.mention} Ты попал, на наш сервер {member.guild.name}',
        description=
        f"```Пока этот текст нельзя изменить...```\n\n\n「:books:」Правила ➤ Лол, обязательно их прочти, чтобы тебя не выгнали или забанили.\n「📰」Информация ➤ Я хз, есть ли она здесь, но прочитай на всякий случай.",
        set_thumbnail=member.guild.icon),
                            components=[
                                Button(style=ButtonStyle.red,
                                       label=
                                       f"Отправленно из ▶{member.guild.name}◀",
                                       emoji="📃",
                                       disabled=True),
                            ])
    responce = await bot.wait_for(
        'button_click', check=lambda message: message.author == ctx.author)
    if responce.component.label == 'Да':
        await responce.respond(content='Деньги успешно переведены!')
    else:
        await responce.respond(content='Вы отменили перевод.')
