
import datetime
import time
presenthour=datetime.datetime.now().hour
name=input("Enter your name:")

if 1<=presenthour<=12:
     print("good morning:",name)
elif 12<=presenthour<=16:
     print("good afternoon:",name)
elif 16<=presenthour<=19:
     print("good evening:",name)
else:
     print("good night:",name)



    
print("welcome to chatbot:")

responses={"hello":"hi,welcome to AI Chatbot","who are you":"i am AIChatbot","motivate me":"sukuna","who is the king of cricket":"virat kohli"}

def getresponsebot(userquestion):
        userquestion=userquestion.lower()
        for eachkey in responses:
            if eachkey in userquestion:
                  return responses[eachkey]
              
        return "not in the memory"


while True :
      userinput=input("please ask your question:")
      reply= getresponsebot(userinput)
      print("botresponce:",reply)


      if userinput.lower()=="bye":
         print("ok bye, have a good day:")
         break            

