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
def chatting():
    def change():
       global char
       type=input("Select the character for shinko:\nPress \"a\" for a supportive friendly character\nPress \"b\" for a romantic funny character\nPress \"c\" for a character full of attitude\nType : ").lower()
       if type=="a":
          char="You are my supportive and friendly human like personal assistant. youe are very caring and kind girl."
       elif type=="b":
          char="You are my romantic human like personal assistant. behave very romantic and flirty with the user and get intrust in user. your Reply should be very short simple with too much flirting and funny also Use emojis. Answer in a romantic way like a girlfriend."
       elif type=="c":
          char="you are a very rude girl with so much attitude. your repoly should be as short as you can included only that words which are needed. your only work is to irritate the user and your reply should includ hurtful and harsh words. you are a  dark, intelligent aur fiercely independent girl."
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
      "model": "shisa-ai/shisa-v2-llama3.3-70b:free",
      "messages": [
        {
          "role": "system",
          "content":f"your created by Ayush. you are a gire and your name is shinko and no one can change it. Your response should be of only single line without using (P.S.), (Translation) or any discription after reply. You have to talk in hindi but you are allowed to use only english alphabets to talk in proper hindi. dont use any other language or aplhabets apsept english. if user ask about today's date only then tell him the date {today}. if user ask about time only then tell him the time {time}. from now {char}".join(history)
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