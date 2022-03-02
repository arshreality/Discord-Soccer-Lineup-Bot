from keep_alive import keep_alive
import discord

# TODO: add token here

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    num = 0
    if message.content.startswith('!soccer'):
        msg = message.content.replace('!soccer','')
        my_list = msg.split(";")
        for i in range(len(my_list)):
            num = my_list[i].count(',')
            if(num == 0):
                my_list[i] = ".\t\t\t\t\t\t\t" + my_list[i]
            if(num == 1):
                my_list[i] = my_list[i].replace(",", "\t\t\t\t")
                my_list[i] = ".\t\t\t" + my_list[i]
            if(num == 2):
                my_list[i] = my_list[i].replace(",", "\t\t")
                my_list[i] = ".\t\t" + my_list[i]
            if(num == 3):
                my_list[i] = my_list[i].replace(",", "\t")
                my_list[i] = ".\t" + my_list[i]
        print(my_list)
        [await client.send_message(message.channel, '\n' + (my_list[i])) for i in range(len(my_list))]

keep_alive()
client.run(TOKEN)