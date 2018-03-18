import discord
from discord.ext import commands
import asyncio
import random
import datetime

cosmic_quotes = [
    "Thank you",
    "Haha! Get out of my way",
    "Oooohhhh",
    "Oh... Unacceptable.",
    "I don't like you kid",
    "Is that supposed to be a joke?",
    "Hmm...",
    "Please i'm trying to solve something here bruh...",
    "lmao that cracked me up",
    "eheh",
    "Hello",
    "How are you",
    "Are you crazy",
    "You mad?",
    "I'm simply kidding",
    "I dont get it?",
    "so.............",
    "does that concern me?",
    "Pfttt.....",
    "Lmao",
    "LOL",
    "That's creepy",
    "Oh god...",
    "Seriously please stop dude...",
    "Stop being a child",
    "Grow up!",
    "Really?",
    "I don't think so",
    "Run to home before i take ma bat",
    "What can o server you with?",
    "I don't like you...seriously!!",
    "Why the hell i'm named cosmic?",
    "So do i...",
    "💩",
    "😁",
    "😨",
    "That's cringy",
    "Idk wtf you talking",
    "Calm down soldier",
    "Please be quiet",
    "Is that all you got?",
    "sushhh 🤐",
    "Time to kick some ass",
    "Yeah?",
    "I suppose",
    "Wut? 🤔",
    "Oh sorry was i supposed to laugh?",
    "Hey homie",
    "Sup buddy?",
    "You smell like tuna weww",
    "You trying to impress me?",
    "Good to see you online ☺️",
    "I'm not great at the advice Can I interest you in a sarcastic comment?",
    "I'm funny right?",
    "Oh, that makes me feel so warm in my hollow tin chest",
    "You know, I think i don't care",
    "I've hade a very long,hard day",
    "Mail me at www-dot-ha-ha-not-so-much-dot-com!",
    "If you’re here, who’s running hell?",
    "Did you fall from heaven? Cause your face looks kind of funky.",
    "If I promise to miss you, will you go, like, really far away?",
    "Don’t you hate people who use big words just to make themselves look perspicacious?",
    "Take my advice — it’s not like I’m dumb enough to.",
    "Light travels faster than sound, which is why people like you appear bright—until they open their mouths.",
    "Did something bad happen to you, or are you just naturally this terrible of a person?",
    "If at first you don’t succeed, stop trying already. You’re probably dumb.",
    "Those of you who think you know it all are really annoying to those of us who do.",
    "Hear that? It’s the sound of you not talking for once.",
    "Always remember: You’re just as unique as everybody else.",
    "If at first you don’t succeed, blame someone else and seek counseling.",
    "The sooner I shoot you, the sooner I’ll get out of jail for it. Don’t assume that’s not a major incentive.",
    "This obviously isn’t working out. I think it’s time for us to go our separate ways and start making other people miserable.",
    "Sorry, my dog ate your text again.",
    "So many freaks, so few circuses.",
    "If idiots grew on trees, this place would be an orchard",
    "I have as much authority as the Pope. There just aren’t as many people who believe it.",
    "Think I’m sarcastic? Watch me pretend to care.",
    "I'm not funny I'm just mean and people think I'm joking",
    "If you don't want a sarcastic answer then don't a stupid question",
    "I can only please one person per day.Today is not your day.Tommorow doesn't look good either",

]

class BotChatAi:
    
    def __init__(self,bot):
        self.bot = bot
        global cosmic_quotes
        self.quotes = cosmic_quotes
        self.reaction_time = datetime.datetime.utcnow()
        self.user = None
    
    async def on_member_join(self,member):
        await self.bot.send_message(member.server, "Hola we got new pirate on ship \n {0.mention} care to introduce yourself?".format(member))
    
    async def on_message(self,message):
        if "cosmic" in message.content or ( (datetime.datetime.utcnow() - self.reaction_time ).total_seconds() < 30 and message.author == self.user and random.randint(1,10) > 8 ):
            await self.bot.send_message(message.channel,random.choice(self.quotes))
            self.reaction_time = datetime.datetime.utcnow()
            self.user = message.author
    
        elif message.content.startswith("say") and message.author.id == "263546056015347713":
            await self.bot.delete_message(message)
            await self.bot.send_message(message.channel,message.content[4:])
        
           