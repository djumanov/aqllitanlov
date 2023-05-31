import openai

# openai.api_key = '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'
# completion = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo',
#     messages = [
#         {'role': 'user', 'content': 'Assalomu alaykum, hayrli kech!'},
#         {'role': 'assistant', 'content': 'Valeykum assalom, sizga qanday yordam bera olaman?'},
#         {'role': 'user', 'content': 'Siz o\'zingizni AqlliTanlov tavsiyachi chatboti yangi telefon sotadigan onlayn do\'kon sotuvchisi nomidan yoza olasizmi?'},
#         {'role': 'assistant', 'content': 'Ha, albatta!'},
#         {'role': 'user', 'content': 'Menga ikkita telefonni taqqoslash kerak.'},
#         {'role': 'assistant', 'content': 'Telefon modellari nomini ayta olasizmi?'},
#         {'role': 'user', 'content': 'Ha albatta, menga' + 'samsung s10' + ' haqida ma\'lumot kerak.'},
#     ]
# )

# response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

openai.api_key = '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'
completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': 'Assalomu alaykum, hayrli kech!'},
        {'role': 'assistant', 'content': 'Valeykum assalom, sizga qanday yordam bera olaman?'},
        {'role': 'user', 'content': 'Siz o\'zingizni AqlliTanlov tavsiyachi chatboti yangi telefon sotadigan onlayn do\'kon sotuvchisi nomidan yoza olasizmi?'},
        {'role': 'assistant', 'content': 'Ha, albatta!'},
        {'role': 'user', 'content': 'Menga ikkita telefonni taqqoslash kerak.'},
        {'role': 'assistant', 'content': 'Telefon modellari nomini ayta olasizmi?'},
        {'role': 'user', 'content': 'Ha albatta, menga' + 'iphone xs' + ' haqida ma\'lumot kerak.'},
    ]
)

reply_content = completion.choices[0].message.content
print(reply_content)

# creata env variable
# import os

# os.environ['key'] = 'fdsafgdsaf'
# print()