import random

user_choice = input(''' select your choice(1 or 2 or 3)-->
          1.sissors
          2.paper
          3.rock
                    
        ''')
choices = ('sissors','rock','paper')
comp_choice = random.choice(choices)

print(comp_choice)