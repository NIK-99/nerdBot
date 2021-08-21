from pyrogram import Client, filters
import re
import pymongo


def initMongo(user, password, db):
    connectionString = f"mongodb+srv://{user}:{password}@assigment.zdwxt.mongodb.net/{db}?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connectionString)
    db = client.test
    return client


def insertMongo(dataToInsert):
    client = initMongo('test', 'test', 'Assigment')
    mydb = client["Assigment"]
    mycol = mydb['Users']
    return mycol.insert_one(dataToInsert)


def loadUser(userId):
    client = initMongo('test', 'test', 'Assigment')
    mydb = client["Assigment"]
    mycol = mydb['Users']
    return mycol.find_one({"userId": userId})


def delUser(userId):
    client = initMongo('test', 'test', 'Assigment')
    mydb = client["Assigment"]
    mycol = mydb['Users']
    return mycol.delete_one({"userId": userId})


ques = [
    """Hey! I’m Nerd - your budgeting assistant. I’ll help setup budget, weekly targets and keep you on track. Select a goal to begin 🔥

Type option number👇
1. New Gadget, vacation etc
2. Investing money
3. Building emergency fund
4. Paying off debt
5. Just saving""",
    """👍 Awesome! I’ve a few more questions to ask. Note: Answers can’t be edited. To restart setup, type restart""",
    """🤑 Your Income & Pay date?
👉 Type (eg): 15000, 27

👉 Income is salary/ allowance/ stipend etc per month""",
    """🌲 Monthly Investments (SIP etc)

👉 Enter total amount""", """👽 Expenses every month?

Home: Rent, Maids, Cook etc.
Bills: Electricity, Water, DTH, Landline, Mobile, Wifi, Gas etc.
EMI: Loans, Insurance etc.

👉 Enter total amount

(Don't include credit card bill payment, grocery)""", """"🤑  income : {income}
🔥 Pay date : {pay date}
🌲 Monthly Investments : {monthly investments} 
👽 Expenses : {expenses}

type Y for contunue type N for input again.""",
    """Your information exists on server, reply yes to this message to delete it""",
    """Your expense + Monthly Investments is greater than monthly pay, reply yes to continue or type restart to reset"""
]
ans = {
    "userId": None,
    "q1": None,
    "q2": None,
    "q3": None,
    "q4": None,
    "q5": "z",
}

i=[0]

@Client.on_message(filters.command(['ping']))
async def ping(bot, message):
    await message.reply_text("pong", quote=True)
    i[0]=0


@Client.on_message(filters.command(['start', 'chat', 'help']))
async def chat(bot, message):
  await bot.send_message(chat_id=message.chat.id, text=ques[0])


async def reset(bot, message):
    ans["q1"] = None
    ans["q2"] = None
    ans["q3"] = None
    ans["q4"] = None
    ans["q5"] = None
    i[0] = 0
    await message.reply_text("User data was reset successfully", quote=True)
    await bot.send_message(chat_id=message.chat.id, text=ques[0])


@Client.on_message(filters.command(['resetdata']))
async def resetUserData(bot, message):
    await reset(bot, message)


@Client.on_message()
async def msg2(bot, message):
    reseted = 0
    if message.text.lower() == "restart":
        reseted = 1
        await reset(bot, message)

    replied = ques[i[0]]

    if replied:
        text = replied

        if text == ques[6]:
            delUser(message.from_user.id)

        elif text == ques[0]:
            ans["userId"] = message.from_user.id,
            if message.text in ['1', '2', '3', '4', '5'] and ans["q1"] == None:
                ans["q1"] = message.text
                await bot.send_message(chat_id=message.chat.id, text=ques[1])
                await bot.send_message(chat_id=message.chat.id, text=ques[2])
            else:
                await bot.send_message(chat_id=message.chat.id,
                                       text="Please enter correct option")
                i[0]-=1  

        elif text == ques[2]:
            try:
              a = message.text.split(",")
            except:
              await bot.send_message(chat_id=message.chat.id, text="invalid option")
              i[0]-=1  
            if re.match('^(0?[1-9]|[12][0-9]|3[01])$', a[1].replace(" ", "")) and re.match(
                    '^[0-9]+$', a[0].replace(" ", "")) and ans["q2"] == None:
                ans["q2"] = message.text
                await bot.send_message(chat_id=message.chat.id, text=ques[3])
            else:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=
                    "Please enter correct answer, don't insert space and recheck the format"
                )
                i[0]-=1  

        elif text == ques[3]:
            if re.match('^[0-9]+$', message.text):
                ans["q3"] = message.text
                if int(ans["q3"]) >int(ans["q2"].split(',')[0].replace(" ", "")) :
                  await bot.send_message(chat_id=message.chat.id,
                                           text="Your investment cannot be greater than your income please re-enter")
                  i[0]-=1
                else:
                  await bot.send_message(chat_id=message.chat.id, text=ques[4])
            else:
                await bot.send_message(chat_id=message.chat.id,
                                       text="please insert correct answer")
                i[0]-=1  

        elif text == ques[4] or text == ques[7]:
            if re.match('^[0-9]+$', message.text[0]):
                ans["q4"] = message.text
                if (int(ans["q4"]) + int(ans["q3"])) > int(ans["q2"].split(',')[0].replace(" ", "")):
                    await bot.send_message(chat_id=message.chat.id,
                                           text=ques[7])
                    i[0]-=1
                    await bot.send_message(chat_id=message.chat.id,
                                           text=ques[3])
                    i[0]-=1
                elif int(ans["q4"]) >int(ans["q2"].split(',')[0].replace(" ", "")):
                  await bot.send_message(chat_id=message.chat.id,
                                           text="Your expense cannot be greater than your income please re-enter")
                  i[0] -= 1
                else:
                    ques[5] = f""" 🤑  income : {ans["q1"]}
  🔥 Pay date : {ans["q2"].split(',')[0]}
  🌲 Monthly Investments : {ans["q3"]} 
  👽 Expenses : {ans["q4"]}

  type Y for continue type N for input again."""
                    await bot.send_message(chat_id=message.chat.id,
                                           text=ques[5])
            elif message.text.lower() == 'no':
                await reset(bot, message)
                i[0] = 0
                await bot.send_message(chat_id=message.chat.id, text=ques[0])
            elif message.text.lower() == 'yes':
                ques[5] = f""" 🤑  income : {ans["q1"]}
  🔥 Pay date : {ans["q2"].split(',')[0]}
  🌲 Monthly Investments : {ans["q3"]} 
  👽 Expenses : {ans["q4"]}

  type Y for continue type N for input again."""
                await bot.send_message(chat_id=message.chat.id, text=ques[5])
            elif ans["q4"] != None:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=
                    "Answer once written cannot be changed, so to reset your all previous selection, type restart"
                )
            else:
                await bot.send_message(chat_id=message.chat.id,
                                       text="Please insert correct option")
                i[0]-=1  

        elif text == ques[5]:
            if message.text.lower() == "y":
                ans["q5"] = message.text
                insertMongo(ans)
                await bot.send_message(chat_id=message.chat.id,
                                       text="😍 Awesome")
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=
                    "Your answer are stored in the database, contact administrator for any update in answer"
                )

            elif message.text.lower() == "n" and ans["q5"] == "z":
                ans["q1"] = None
                ans["q2"] = None
                ans["q3"] = None
                ans["q4"] = None
                ans["q5"] = None
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="The previous ans has been reseted")
                await bot.send_message(chat_id=message.chat.id, text=ques[0])
            else:
                await bot.send_message(chat_id=message.chat.id,
                                       text="invalid option")
        else:
            await bot.send_message(chat_id=message.chat.id, text=message)


    elif reseted == 0:
        await bot.send_message(chat_id=message.chat.id,
                               text="Please reply to last bot message")

    i[0]+=1
    if i[0] == 1:
      i[0]+=1      