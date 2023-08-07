
import openai
api_key = ""
openai.api_key = api_key

messages = []
while True:
    content = input("User: (Press 'Q' quit)")
    if content == "Q":
      print(content)
      break
    
    messages.append({"role": "user", "content": content})
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion
    answer = chat_response.choices[0].message.content
  
    print(f"User: {content}")
    print(f'ChatGPT: {answer}')
    with open("answer回答.txt",'a',encoding='utf-8') as file:
      file.write(content+'\n')
      file.write(f'ChatGPT: {answer}'+'\n')
      file.write('*'*150+'\n')
    messages.append({"role": "assistant", "content": answer})
    
