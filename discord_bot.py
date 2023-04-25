import discord
from stockx import search, get_sizes
from config import TOKEN, CHANNEL_ID

client = discord.Client()

def size_list(sizes):
    abc = []
    for key in sizes:
        abc.append(f'US:{key} - ${sizes[key]}')
    tester = '\n'.join(abc)
    return tester


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if message.content.split(' ')[0] == '!stockx':
        query = message.content.replace('!stockx ', '')

        item = search(query)
        prod_id = item['id']
        sizes = get_sizes(prod_id)
        finish = size_list(sizes)

        embed = discord.Embed(
            title=item['title'],
            url='https://stockx.com/en-gb/' + item['urlKey']
        )
        embed.set_thumbnail(
            url=item['media']['imageUrl']
        )
        embed.add_field(
            name='Colorway',
            value=item['colorway'],
            inline=False
        )
        embed.add_field(
            name='Style ID',
            value=item['styleId'],
            inline=False
        )
        embed.add_field(
            name='Last Sale',
            value=item['market']['lastSale'],
            inline=False
        )
        embed.add_field(
            name='Last Sale',
            value=item['market']['lastSale'],
            inline=False
        )
        embed.add_field(
            name='Lowest Ask',
            value=finish,
            inline=False
        )
        await message.channel.send(embed=embed)

client.run(TOKEN)

