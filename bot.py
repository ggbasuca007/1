import discord # Não esquece do: pip install discord (nota pessoal do criador)

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

@client.event
async def joined(ctx, member: discord.Member):
    await ctx.channel.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

client.run("SEU TOKEN DO BOT DEVE FICAR AQUI!")
