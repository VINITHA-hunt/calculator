def cal():
 from cal.add import add
 from cal.mul import mul
 from cal.sub import sub
 from cal.div import div
 from cal.exp import exp
 from cal.mod import mod
 from inpu.get import inpu
 print("welcome ")
 print("1.addition")
 print("2.subtraction")
 print("3.multiplication")
 print("4.division")
 print("5.exponentiate")
 print("6.modulus")
 choice =int(input("enter your choice:"))
 val1,val2=inpu ()
 if choice==1:
  add (val1,val2)
 elif choice==2:
  sub (val1,val2)
 elif choice==3:
  mul (val1,val2)
 elif choice==4:
  div (val1,val2)
 elif choice==5:
  exp (val1,val2)
 elif choice==6:
  mod (val1,val2)
 else:
  print("not valid")
def calculator():
 while True:
  again=int(input("enter 1 or 0"))
  if again==1:
   cal()
  else:
   break
calculator()
 
  
  



   

  
 
             