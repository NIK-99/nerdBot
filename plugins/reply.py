# from pyrogram import Client, filters


# @Client.on_message()
# async def allmessage(bot,message):
#   mess_2 ="""👍 Awesome! I’ve a few more questions to ask. Note: Answers can’t be edited. To restart setup, type restart"""
#   mess_3 = """🤑 Your Income & Pay date?
# 👉 Type (eg): 15000, 27

# 👉 Income is salary/ allowance/ stipend etc per month"""
#   start_message = """Hey! I’m Nerd - your budgeting assistant. I’ll help setup budget, weekly targets and keep you on track. Select a goal to begin 🔥

# Type option number👇
# 1. New Gadget, vacation etc
# 2. Investing money
# 3. Building emergency fund
# 4. Paying off debt
# 5. Just saving"""
#   # print(type(message))
#   # print(message)
#   try:
#     z=int(message.text)
#     if z in [1,2,3,4,5]:
#       try:
#         message.reply_to_message.text == start_message
#         await bot.send_message(
#           chat_id=message.chat.id,
#           text=mess_2)
#         await bot.send_message(
#           chat_id=message.chat.id,
#           text=mess_3)
#       except:
#         await bot.send_message(
#           chat_id=message.chat.id,
#           text="Please reply to previous message")
#     else:
#       await bot.send_message(
#         chat_id=message.chat.id,
#         text="incorrect")
#   except:
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="incorrect")

# di = {
#   """Hey! I’m Nerd - your budgeting assistant. I’ll help setup budget, weekly targets and keep you on track. Select a goal to begin 🔥

# Type option number👇
# 1. New Gadget, vacation etc
# 2. Investing money
# 3. Building emergency fund
# 4. Paying off debt
# 5. Just saving""":None,
# """👍 Awesome! I’ve a few more questions to ask. Note: Answers can’t be edited. To restart setup, type restart""":None,
# """🤑 Your Income & Pay date?
# 👉 Type (eg): 15000, 27

# 👉 Income is salary/ allowance/ stipend etc per month""":None,
# """🌲 Monthly Investments (SIP etc)

# 👉 Enter total amount""":None,
# """👽 Expenses every month?

# Home: Rent, Maids, Cook etc.
# Bills: Electricity, Water, DTH, Landline, Mobile, Wifi, Gas etc.
# EMI: Loans, Insurance etc.

# 👉 Enter total amount

# (Don't include credit card bill payment, grocery)""":None,
# """🤑  income : {income}
# 🔥 Pay date : {pay date}
# 🌲 Monthly Investments : {monthly investments} 
# 👽 Expenses : {expenses}

# type Y for contunue type N for input again.""":None,
# """😍 Awesome""":None,
# }
# for i in di:
#   print(i)