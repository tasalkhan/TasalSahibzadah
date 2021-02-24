#print("hello world \"how are you\" ")
#print('i\'m harshit')
# print('i am\t tasal')
# print('i \b tasal')
# print("this is backslash\\")
# print("line a\\n")
# print('\\"\\\'')
                    # first exercices

# print("this is\\\\ double backslah")
# print("thes are /\\/\\/\\/\\/\\ mountains")
# print("he is\tawesome")
# print('\\"\\n \\t \\\'')
# print(r"line A\n lineB")  #short way
# print(2/3)
# print(round(6**0.5 , 3))
# print(25/2)
# print(12.5%6)
# print('ahmad'*3)
# print('ahmad'+ '3')
# print('ahmad'+ str(3))
# a= int(input("enter first number"))
# b=int(input("enter second number"))
# total=a+b
# print(total)
# age,name=input("please enter you age  and  name").split()
# print("  ",age ,"  ", name)
# x,y,z="1","2","3"
# print(z)
# a='tasal'
# age=5
# print("hello "+a+  "your age is " + str(age))
# print("hello {} your age is {} ".format(a,age))
# print(f"hello {a} your age is {age+2}")
               ####### chapter 2 exercise 1
# a=int(input("enter first latter"))
# b=int(input("ebter 2nd latter"))
# c=int(input("enter 3rd latter"))
# average=(a+b+c)/3
# print(average)

# a,b,c=input("first number"+"enter 2nd number"+"enter 3rd number").split(",")
# print(f"average of three number: {(int(a)+int(b)+int(c))/3}")
# a="tasal"
# print(a[4])
# a="afghanistan"
# print(a[0:3])
# print(a[-4:-1])
# print("afghanistan"[::-1])
# print("afghanistan"[0::5])
             #####chapter 2 exercise 2
# a=input("Please enter your name: ")
# print(f"revers of your name is: {a[::-1]}")
# a="afghanistan"
# print(len(a))
# print(len("afghanistan"))
# b="Afghanistan Is An Islamic Country I Located"
# print(b.lower())
# print(b.upper())
# print(b.title())
# print(b.count("I"))
# c="tasactl"
# print(len(c))
# print(c.count("t"))
##################33 chapter 2 exrcise 3
# name,letter=input("enter you name and letter: ").split(",")
                          ### c=(name.lower())
# print(f"the length of the name is {len(name)} and the character is repeted {name.lower().count(letter)}")

# user_name,Character=input("please enter user_Name:  and a character that you want to count comma seperated ").split(",")
# print(f"the length of user name is {len(user_name)} and the character is repeted {user_name.lower().count(Character.lower())}")
# a="          afghnistan   "
# b="tasa  l"
# print(a)
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())
# print(b.strip())
# print(b.replace(" ",""))
# name,letter=input("please enter name and letter: ").split(",")
# print(f"lentgh of name is  {len(name.strip())}")
# print(f"character is repeted {name.strip().lower().count(letter.strip().lower())}")
# # # c=name.strip()
# print(c)
# a=(" she is beautiful and she is good dancer")
# print(a.find("is", 4))////Start from the position
# print(a.replace("is","was",1))//////////replcae how many workds
# name="tasal"
# print(name.center(7,"$"))
# name=input("enter your name")
# # c=len(name)
# c=len(name)
# print(name.center(c+4,"*"))
# a="afghanistan"
# print(a[1])
                                      #Chapter 3 video 42
# a=int(input("enter your age"))
# if a>18:
#     pass
#     print("you are above 14")
# user_name=int(input("enter your name: "))
# if user_name >= 14:
#     print("you can play the game")
# else:
#     print("you cant play the game")
####################################chapter 3 exercise1
# winning_number=6
# guess_number=int(input("enter a number between 1 to 10: "))
# if winning_number==guess_number:
#     print("congrotalation you guess correct number")
# else:
#     if guess_number>winning_number:
#         print("please choose low number")
#     else:
#         print("pleaes choose higher number")
#
#
# a=17
# b=16
# if a==17 and b==161:    ####or
#     print("True")
# else:
#     print("False")
################### chapter 3 exercise 2 watch coco#####################
# user_name=input("please enter you name: ")
# age=int(input("enter your age: "))
#
# c=user_name.lower().find("a")
# if c==0 and age>=10:
#     print("you can watch the movie")
# else:
#     print("unfortunally you cannot watch the movie")
# user_name=input("please enter you name: ")
# age=int(input("enter your age: "))
# if age >=10 and (user_name[0]=="a"or user_name[0]=="A"):
#     print("you can watch movie")
# else:
# #     print("u cant watch movie")
# age=int(input("enter your age: "))
# if age==0 or age<0:
#     print("you cant watch")
# elif   0<age<=3:
#     print("ticker price is 2 afg")
# elif 3<age<=10:
#     print("ticker price is 10 afg")
# elif 10<age<=60:
#     print("ticket price is 20 afg")
# elif 60<age<=90:
#     print("price is 50 afg")
# else:
#     print("cost is 200")
# a="afghanistan"
# # if "z" in a:
# #     print("t is here")
# # else:
# #     print("not here")
# name=""
# if name:        #### check that is string empty or not below is use of it
#     print("string is not empty")
# else:
#     print("string is  empty ")
#
a = input("enter your name: ")
if a:
      print(f"your name is {a}")
else:
    print("you didnt type anyting")