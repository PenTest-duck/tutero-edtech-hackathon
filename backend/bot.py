import discord
from discord.ext import commands
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

groq_client = Groq()

# Intents (required for bots to receive specific events)
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

user_contexts = {}

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

def send_to_groq(message):
    completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": message,
            },
            {
                "role": "assistant",
                "content": "Learning to play the guitar can be a fun and rewarding experience, but it requires practice and patience. Here's a step-by-step guide to get you started:\n\n**Equipment Needed:**\n\n* A guitar (acoustic or electric)\n* Guitar tuner\n* Picks (if you prefer to use them)\n* Music stand or tablet with guitar tabs\n* A chair or stool to sit comfortably\n\n**Basic Guitar Hold:**\n\n1. Hold the guitar by resting it on your left leg, if you're right-handed. Rest the body of the guitar on the upper leg, and the neck of the guitar on your left leg. This is known as a \"leg rest\" or \"lap rest.\"\n2. Place the guitar strap (if you have one) around your neck and shoulder, and adjust it so the guitar is at a comfortable height.\n\n**Hand Positions:**\n\n1. Left Hand: Place your left hand on the neck of the guitar, with your index and middle fingers forming a \"V\" shape on the first fret of the sixteenth fret. This is the foundation of chords.\n2. Right Hand: Hold your right hand in a relaxed position, with your fingers curled gently over the fretboard. You can use your fingers to strum the strings or a pick to play chords.\n\n**Chords:**\n\n1. Familiarize yourself with basic chords, such as A, C, D, E, and G.\n2. Start with simple chords and gradually move on to more complex ones.\n3. Use chord charts or online resources to learn chord shapes and finger positions.\n4. Practice changing between chords smoothly, using a metronome to help you with timing.\n\n**Strumming and Picking:**\n\n1. Learn basic strumming patterns, such as downstrokes and upstrokes.\n2. Experiment with different rhythms and patterns to create your own style.\n3. If you're using a pick, hold it between your thumb and index finger, with your other fingers curled over the guitar.\n4. Practice picking and strumming in different directions (e.g., horizontally, vertically, or diagonally).\n\n**Scales and Arpeggios:**\n\n1. Familiarize yourself with basic scales, such as the pentatonic scale or major scale.\n2. Learn arpeggios (broken chord patterns played in a smooth, flowing manner).\n3. Practice playing scales and arpeggios in different positions on the guitar neck.\n\n**Practice Routine:**\n\n1. Set aside 15-30 minutes each day to practice.\n2. Start with simple exercises and gradually move on to more complex ones.\n3. Practice chord changes, scales, and arpeggios in different positions and rhythms.\n4. Record yourself to track your progress and identify areas for improvement.\n\n**Tips and Tricks:**\n\n1. Use a guitar tuner to ensure you're playing in tune.\n2. Use a metronome to improve your timing and coordination.\n3. Practice with a pick or fingerstyle to develop different playing techniques.\n4. Experiment with different genres and styles to find your own voice.\n\nRemember, learning to play the guitar takes time, effort, and patience. Don't be discouraged if you don't see progress immediately. With consistent practice and dedication, you'll become a skilled guitarist in no time!"
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Command: Report
@bot.command()
async def report(ctx, *, message):
    if ctx.author.id not in user_contexts.keys():
        user_contexts[ctx.author.id] = []

    user_contexts[ctx.author.id].append(message)
    await ctx.send(f"Reported by user {ctx.author.id}: {message}")

# Command: ask
@bot.command()
async def ask(ctx, *, question):
    response = send_to_groq(question)
    await ctx.send(response)

# Run the bot
bot.run(os.environ.get("DISCORD_TOKEN"))
