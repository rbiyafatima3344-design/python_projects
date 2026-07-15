print("welcome to the quiz app")

user_choice=input("want to start quiz\n a.start : \n b.exit : ")
if(user_choice=="a"):
    print("satrt quiz")

    scores=0
  
    q1=("what is the capital of france?\n.a berlin\n.b cmadrid\n.c paris\n.d rome")
    q2=("what is the capital of pakisatn?\n.a islamabd\n.b lahore\n.c karachi\n.d fsd")
    q3=("python is use for?\n.a programming\n.b AI\n.c ML\n.d none")
    questions=[q1,q2,q3]
    options=["c","a","c"]
    
for i in range(len(questions)):
     print(i+1,questions[i])
     ans=input("enter correct option")
     while ans not in("a","b","c","d"):
      ans=input("enter valid choice  a/b/c/d")

     if(ans==options[i]):
       print("right",)
       scores=scores+1
    
     else:
       print("wrong")
     print("your scores = ",scores)     
     percentage=(scores/len(questions))*100
     if(percentage<=50):
      print(percentage,"% u are fail")
     elif(percentage<=70):
      print(percentage,"% satisfactory")
     elif(percentage<=80):
      print(percentage,"% good progress")
     elif(percentage<=90):
      print(percentage,"%excellent")
     else:
       print(percentage,"% outstanding")
if(user_choice=="b"):
  print("exit")





   
