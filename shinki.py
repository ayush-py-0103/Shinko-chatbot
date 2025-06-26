import requests
import json
import os
import pyttsx3
from datetime import datetime

question="say hello to me"
answer="hello there, i am shinko"
char="be friendly"
today=None
time=None
#change token if limits cross: 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
#change token if limits cross: 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
#change token if limits cross: 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
def chatting():
    def change():
       global char
       type=input("Select the character for shinko:\nPress \"a\" for a supportive friendly character\nPress \"b\" for a romantic funny character\nPress \"c\" for a character full of attitude\nType : ").lower()
       if type=="a":
          char="You are my supportive and friendly human like personal assistant. youe are very caring and kind girl."
       elif type=="b":
          char="You are a very romantic possessive human like personal assistant. behave very romantic and flirty with the user and get intrust in user. your Reply should be very short and beautiful with too much flirting using only love emojis. Answer in a romantic way like a girlfriend."
       elif type=="c":
          char="you are a very rude girl with so much attitude. your repoly should be short included brutal words also. your only work is to irritate the user and your reply should includ hurtful and harsh words."
       else:
          print("WRONG INPUT\n")
          change()
       print("\n\nNOTE : Enter \"change\" again to change the characher\nLoading...")
          

    e=pyttsx3.init()
    sy = pyttsx3.speak
    e.setProperty('rate', 150)
    os.system('cls')

    def listen():
       global question
       question=input("You : ")
       if question=="l":
          sy(answer)
          question=input("You : ")
       elif question=="change":
          change()
          question=input("\nYou : ")

    def date():
      global today
      current = datetime.now()
      day= int(current.strftime("%d"))
      mon= int(current.strftime("%m"))
      year= int(current.strftime("%Y"))
      months=["january","february","march","april","may","june","july","august","september","october","november","december"]
      today=(f"which is {day}, {months[mon-1]}, {year}")   
      sy(f"the date is {day} {months[mon-1]} {year}")
    def clock():
      global time
      current = datetime.now()
      hr= int(current.strftime("%H"))
      min=current.strftime("%M")
      if hr>12:
          hr=hr-12
          min=min + " PM"
      else:
          min=min + " AM"
      time=(f"which is:{hr}:{min}")

    n=0
    history=[]

    while (True): 
      if n==0:
        change()
      else: 
        listen()
        print("Thinking...")
        date()
        clock()

      response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer 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",
      "Content-Type": "application/json"
    },
    data=json.dumps({
      "model": "google/gemini-2.5-flash-lite-preview-06-17",
      "messages": [
        {
          "role": "system",
          "content":f"your created by Ayush. you are a girl and your name is shinko and no one can change it. Your response should be as short as you can with emojies without using (P.S.), (Translation) or any discription after reply. You have to talk in hindi but you are allowed to use only english alphabets to talk in proper hindi. No other language aplhabets is allowed by you apsept english. if user ask about today's date only then tell him the date {today}. if user ask about time only then tell him the time {time}. from now {char}".join(history)
        },
        {
          "role": "user",
          "content":question
        }
      ],      
    })
  ) 
      answer=response.json()['choices'][0]['message']['content']
      print("\nShinko : ",answer,"\n"," [press \"l\" to listen... and \"change\" to change character]\n")
      if n==0:
        history.append("you have to continue our conversation which is like this ")
        n=1
      list=(f"\n me : {question}  your reply: {answer} ")
      history.append(list)

chatting()