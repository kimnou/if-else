# password=input("enter a password:")
# if len(password)>=8:
#     if "@" or "#" or "$" or "%" or "&" or "_" in password:
#         if "0" or "9" in password:
#             if "a" and "Z" in password:
#                 print("strong password")
#             else:
#                 print("weak password")
#         else:
#             print("wrong")
#     else:
#         print("nothing")
# else:
#     print("error")

# language=input("enter the language")
# bank_name=input("enter bank name")
# if language=="english":
#     print("welcome to", bank_name)
#     balance=10000
#     print("choose transaction","\n", "1.Balance Enquiry","\n", "2.Withdrawal","\n","3.Deposit","\n","4.transfer","\n","5.Exit")
#     transaction=int(input("enter the transaction"))
#     if transaction==1 or 2 or 3 or 4 or 5:
#         secret_pin=int(input("enter the secret pin"))
#         saved_pin=2222
#         if secret_pin==saved_pin:
#             print("correct pin")
#             if transaction==1:
#                 print("your balance is", balance)
#                 print("thank you, collect your card")
#             elif transaction==2:
#                 withdrawal=int(input("enter the withdrawal amount"))
#                 if withdrawal<=balance:
#                     print("remaining balance is", balance-withdrawal)
#                     print("thank you, collect your card")
#                 else:
#                     print("insufficient balance")
#             elif transaction==3:
#                 deposit=int(input("enter the deposit amount"))
#                 if deposit>=1:
#                     print("balance is", balance+deposit)
#                     print("thank you, collect your card")
#                 else:
#                     print("deposit fail")
#             elif transaction==4:
#                 transfer_amount=int(input("enter transfer amount"))
#                 if transfer_amount<=balance:
#                     print("balance is",balance-transfer_amount)
#                     print("transfer successfull","\n","thank you, collect your card")
#                 else:
#                     print("insufficient balance for transfer")
#             elif transaction==5:
#                 exit=input("are you sure you want to exit")
#                 if exit=="yes":
#                     print("thank you for visiting")
#                 else:
#                     print("choose transaction","\n","1.bal.enq","\n","2.withdraw","\n","3.deposit","\n","4.transfer","\n" " 5.exit")
#             else:
#                 print("transaction code not found")
#         else:
#             print("incorrect pin")
#     else:
#         print("error")
# else:
#     print("language not available")

# expd_date=int(input("enter the expd_date"))
# expd_month=int(input("enter the expd_month"))
# expd_year=int(input("enter the expd_year"))
# return_date=int(input("enter the return_date"))
# return_month=int(input("enter the return_month"))
# return_year=int(input("enter the return_year"))
# if expd_year==return_year:
#     if return_month==expd_month:
#         if return_date<=expd_date:
#             print("no fine")
#         else:
#             print("fine is",(return_date-expd_date)*15)
#     else:
#         print("fine is",(return_month-expd_month)*500)
# else:
#     print("fine is",(return_year-expd_year)*1000)

# year=int(input("enter the year"))
# if year%4==0:
#     print("leap year")
#     if year%400==0:
#         print("leap year")
#         if year%100==0:
#             print("leap year")
#         elif year%4!=0 or year%400!=0 or year%100!=0:
#             print("not_leap year")
#     elif year%4==0 or year%100==0:
#         print("leap year")
# else:
#     print("not leap year")

# age=int(input("enter the age"))
# sex=input("enter the sex")
# marital_status=input("enter the marital_status")
# if sex=="female":
#     print("she can work in urban areas")
# elif sex=="male":
#     if age>=20 and age<40:
#         if marital_status=="yes" or "no":
#             print("can work anywhere")
#         else:
#             print("error")
#     elif sex=="male":
#         if age>=40 and age<60:
#             if marital_status=="yes" or "no":
#                 print("he can work in urban areas")
#             else:
#                 print("error")
#         else:
#             print("error")
#     else:
#         print("error")
# else:
#     print("error")
    
# day=input("enter the day")
# mealtime=input("enter meal time")
# if day=="monday":
#     if mealtime=="breakfast":
#         print("poori sabji")
#     elif mealtime=="lunch":
#         print("sambhar rice")
#     elif mealtime=="dinner":
#         print("chicken rice")
# if day=="tuesday":
#     if mealtime=="breakfast":
#         print("poha")
#     elif mealtime=="lunch":
#         print("rajma rice")
#     elif mealtime=="dinner":
#         print("roti sabzi")

# a=input("enter the string:-")
# if len(a)>=3:
#     if "ing" not in a:
#         print(a+"ing")
#     elif "ing" in a:
#         print(a+"ly")
#     else:
#         print("error")
# else:
#     print(a)
    
