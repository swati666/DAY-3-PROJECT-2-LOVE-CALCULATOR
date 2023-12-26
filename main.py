#LOVE CALCULATOR
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1=name1.lower()
lower_name2=name2.lower()

t_count=lower_name1.count("t")+lower_name2.count("t")
r_count=lower_name1.count("r")+lower_name2.count("r")
u_count=lower_name1.count("u")+lower_name2.count("u")
e_count=lower_name1.count("e")+lower_name2.count("e")
name_true=t_count+r_count+u_count+e_count

# print(f"T occurs {t_count} times\n")
# print(f"R occurs {r_count} times\n")
# print(f"U occurs {u_count} times\n")
# print(f"E occurs {e_count} times\n")
#print(f"Total= {name_true}\n")

l_count=lower_name1.count("l")+lower_name2.count("l")
o_count=lower_name1.count("o")+lower_name2.count("o")
v_count=lower_name1.count("v")+lower_name2.count("v")
e2_count=lower_name1.count("e")+lower_name2.count("e")
name_love=l_count+o_count+v_count+e2_count
# print(f"L occurs {l_count} times\n")
# print(f"O occurs {o_count} times\n")
# print(f"V occurs {v_count} times\n")
# print(f"E occurs {e2_count} times\n")
#print(f"Total= {name_love}\n")
str_name=f"{name_true}{name_love}"
love_score=int(str_name)
if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")

