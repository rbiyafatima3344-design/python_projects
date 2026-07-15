print("welcome to expense tracker\n.1 Add Expense\n.2 View All Expenses\n.3 View total expenses\n.4 search expenses\n.5 delete expenses\n.6Exit ")

exp_category=["food","transport","shopping","education","entertainment","others"]  
exp_description=[]
exp_amount=[]
all_expenses=[]
while True:
 choice=input("select from above").strip()
 if choice not in["1","2","3","4","5","6"]:
    print(" invalid choice\n choose valid option")
    continue
 if(choice=="1"):
   print("expenses categories are : ",exp_category)

   category=input("add expense category")
   exp_category.append(category)  

   description=input("enter expense description")
   exp_description.append(description) 
   
   amount=int(input("enter expense amount"))
   if(amount<=0):
     print("amount must be greater than 0")
   else: 
     display={
     "exp_category":category,
     "exp_description":description,
     "exp_amount" : amount
      }
     all_expenses.append(display)
  
 if(choice=="2"):
    print("View All Expenses")
    for i ,exp in enumerate (all_expenses):
     print(f" {exp['exp_category']} :{exp['exp_description']}: {exp['exp_amount']}")
    if len(all_expenses)==0:
     print("no expenses display yet")
    else:
     print("recorded expenses are above")
    
 if(choice=="3"): 
   print("View Total Expenses")
   calculate=0
   for exp in all_expenses:
    calculate=calculate+int(exp["exp_amount"])
   print("display all expense amounts",calculate)

 if(choice=="4"):
   print("search by category")
   search=input("enter category")
   for i,exp in enumerate (all_expenses):
    if(exp["exp_category"]==search):
      print("ur category is here")
      print(f"{exp['exp_category']} :{exp['exp_description']}: {exp['exp_amount']}")

 if(choice=="5"):
    print("delete expenses")
    if(len(all_expenses)==0):
      print("no expense to delete")
    else:
      for i ,exp in enumerate (all_expenses):
       print(f" {i+1}:{exp['exp_category']} :{exp['exp_description']}: {exp['exp_amount']}")
       serial=int(input("enter serial number to delete expense"))
    
       if(i+1==serial):
        all_expenses.pop(i)
      print("expense deleted sucessfully")
      break
     
 if(choice=="6"):
   print("Exit")
   print("thank you for using Expense Tracker")
   break
       
