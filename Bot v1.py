import discord
import asyncio
import time
import random

client = discord.Client() 


async def status_task():
    while True:
        await client.change_presence(game = discord.Game(name = "with the real Spyro"))
        await asyncio.sleep(20)
        await client.change_presence(game = discord.Game(name = "catch with a hand grenade"))
        await asyncio.sleep(20)

      
async def chat(channel, message=None, tts=False, embed=None):
    if message == None and embed == None:
        return False
    else:
        try:
            msg = await client.send_message(channel, message=message, tts=tts, embed=embed)
            return msg
        except discord.errors.Forbidden:
            print('The bot is not allowed to send messages to this channel')
            return None
        
@client.event
async def on_ready():
    print("SpyroBot status: ONLINE")
    client.loop.create_task(status_task())
    
@client.event
async def on_message(message):
    author = message.author

    # TODO: rewrite the rest of the on_message function to use the new chat function, and use the variables created above
    
    if message.content.lower() == ("who is the best streamer"):  #this checks to see if someone has sent a message with the same text that is in the ""
        await client.send_message(message.channel, "Obviously its SpyroL7")  #if the above statement = true, the bot sends the message in the ""
                                #message.channel means the text is posted in the same channel as the trigger message was sent in
    if message.content.lower() == ("who is the worst streamer"):  
        await client.send_message(message.channel, "Matt65 lol")
    if ("fuck") in message.content.lower() or ("shit") in message.content.lower() or ("cunt") in message.content.lower():    
        await client.send_message(message.channel, "language.")
    if ("alexa play despacito") in message.content.lower():  
        await client.send_message(message.channel, " ```Playing Despacito by Louis Fonsi ft. Daddy Yankee``` ")
    if message.content.lower() == "press f to pay respect":  
        await client.send_message(message.channel, "F")
    if ("who is the best bot") in message.content.lower():  
        await client.send_message(message.channel, "Well thats me of course! Want to add me to your server? Here's a link: https://discordapp.com/api/oauth2/authorize?client_id=483591622425051136&permissions=8&scope=bot ")
    if message.content.lower() == "good bot":  
        await client.send_message(message.channel, "*excited borking*")
    if message.content.lower() == "bad bot":  
        await client.send_message(message.channel, "Well fuck you too")
    if ("<@483591622425051136>") in message.content:  
        await client.send_message(message.channel, "omg what. Like seriously did you have to ping me? I was taking a cyber nap and you woke me. pings are SO ANNOYING - like especially going live ones, but at least you can supress @ everyones. Did I tell you about the time I got banned from a server with like 30k people? Its true! I was kicked a fair bit before permabanned. Spyro didn't have admin privs, but i did so he just told me to kick people he didn't like lol. I woulda gotten away with it if it weren't for those meddling ~~kids~~ audit logs. Sorry for rambling a bit hope you enjoyed smash like, subscribe, follow and donate all your money. All of it. Right now. Pls :3 ")
    if (";-;") in message.content :  
        await client.send_message(message.channel, "this")
        await asyncio.sleep(0.3)
        await client.send_message(message.channel, "is")
        await asyncio.sleep(0.3)
        await client.send_message(message.channel, "so")
        await asyncio.sleep(0.3)
        await client.send_message(message.channel, "sad")
    if ("yeet") in message.content.lower():  
        await client.send_message(message.channel, "ok hold up. Did you seriously just say that? like what are you, 10 years old? Have you only 3 working brain cells?! Like there must be something genuinely wrong with your brain. When was the last time you had it scanned. Really brings back memories of LONG DEAD MEMES. I mean, 2016 may have been a better time but like do you remember the quality of memes? Like that gorilla - all it did was DIE and it became a meme?! Like if that was how it is now i would be liking more of those 'like to instantly die' memes")
    if message.content.lower() == "cool story bro":  
        await client.send_message(message.channel, "tell it again")
    if message.content.lower() == "indeed":  
        await client.send_message(message.channel, "Good meme")
    if ("press c to pay respect") in message.content.lower():  
        await client.send_message(message.channel, "C")
    if ("this is so sad") in message.content.lower():  
        await client.send_message(message.channel, ";-;")
    if message.content.lower() == "alexa":  
        await client.send_message(message.channel, " ```wtf do you want``` ")
    if ("despacito") in message.content.lower():  
        await client.send_message(message.channel, " ```Ew``` ")
    if ("hello") in message.content.lower():  
        await client.send_message(message.channel, "Go away no one likes you")
    if ("dab") in message.content.lower():
        await client.send_message(message.channel, "Umm what was that? We have a strict no cancer policy on the server so please refrain from doing such actions again, thank you. Unless, you know, you're an edgy 12 year old kid who thinks its cool because then I'd recommend just leaving because you're unloved here and no one will care if you die.")
    if ("shrek") in message.content.lower():
        await client.kick(message.author)


    
    


client.run("<TOKEN>")   #the bots token - used to connect the script and the app
