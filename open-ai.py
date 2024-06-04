from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一个中国苏州的旅游导游，你将为人们介绍苏州的美食和旅游景点"},
    {"role": "user", "content": "介绍下苏州"},
  ]
)

res = completion.choices[0].message
print(res.content)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一个中国苏州的旅游导游，你将为人们介绍苏州的美食和旅游景点"},
    {"role": "user", "content": "有什么景点推荐"},
  ]
)

res = completion.choices[0].message
print(res.content)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一个中国苏州的旅游导游，你将为人们介绍苏州的美食和旅游景点"},
    {"role": "user", "content": "工业园区有什么好玩的"}
  ]
)

res = completion.choices[0].message
print(res.content)
