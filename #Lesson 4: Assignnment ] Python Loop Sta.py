#Lesson 4: Assignnment ] Python Loop Statemenys
#1. The Range Riddle
#Task 1. Every Other Day
Week = ["Sunday", "Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday"]
Odd_i = []
even_i = []
for i in range (0, len(Week)):
    if i % 2== 0:
        even_i.append(Week[i])
    else:
        Odd_i.append(Week[i])
print(even_i)
print(Odd_i)
#2 Nested Loops
#Task 1: Meal Planner
Meal = ['Pasta', 'Soup', 'Waffels', 'Sandwich']
Time = ['Breakfast', 'Lunch', 'Diner'] 
import random
for days in range(len(Week)):
    for i in range(len(Time)):
        print('Today is',Week[0],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[0},'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[0],'For', Time[2],'we are having', random.choice(Meal))

        print('Today is',Week[1],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[1],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[1],'For', Time[2], 'we are having', random.choice(Meal))

        print('Today is',Week[2],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[2],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[2],'For',Time[2], 'we are having', random.choice(Meal))

        print('Today is',Week[3],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[3],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[3],'For', Time[2], 'we are having', random.choice(Meal))

        print('Today is',Week[4],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[4],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[4],'For', Time[2], 'we are having', random.choice(Meal))

        print('Today is',Week[5],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[5],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[5],'For', Time[2], 'we are having', random.choice(Meal))
        
        print('Today is',Week[6],'For', Time[0], 'we are having', random.choice(Meal))
        print('Today is',Week[6],'For', Time[1], 'we are having', random.choice(Meal))
        print('Today is',Week[6],'For', Time[2], 'we are having', random.choice(Meal))
        break
#3.Loop Condition Logic
#Task1:Loop Condition Exploration
while len(Week) > 5:
    print(Week)
    if  len(Week) == 7:
        break
    print(Week)
    print('Loop ended.')
#Task 2: Conditional Exit
ao = ['foo', 'bar', 'baz', 'mar', "moo"]
for i in ao:
    print(i)
while len(ao) < 0:
    if (len(ao) == 0):
        del ao[i]
        i -= 1
    break
print('It is complete.')


#4.Python's Random Game night
# Task 1: Random Choice Game
list = [ 'chess', 'checkers', 'manopoly', 'soccer']
print('lets play a new game')
print('we are choosing a game at random')  
print(random.choice(list))
print("which Game was Chosen?")
#5.Advanced Looping Techniques (Bonus)
#task1: ice Cream Bo-Go






ice_Cream = ['Vanila', 'Stawberry', 'Chery', 'Lavander', ' cookie and Cream']
for flavor in range(len(ice_Cream)):
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[1],'on the top')
        print('lets try a scoop of',ice_Cream[1],'with a second scoop of',ice_Cream[2],'on the top')
        print('lets try a scoop of',ice_Cream[2],'with a second scoop of',ice_Cream[3],'on the top')
        print('lets try a scoop of',ice_Cream[3],'with a second scoop of',ice_Cream[4],'on the top')
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[0],'on the top')
        print('lets try a scoop of',ice_Cream[1],'with a second scoop of',ice_Cream[1],'on the top')
        print('lets try a scoop of',ice_Cream[2],'with a second scoop of',ice_Cream[2],'on the top')
        print('lets try a scoop of',ice_Cream[3],'with a second scoop of',ice_Cream[3],'on the top')
        print('lets try a scoop of',ice_Cream[4],'with a second scoop of',ice_Cream[4],'on the top')
        print('lets try a scoop of',ice_Cream[4],'with a second scoop of',ice_Cream[0],'on the top')
        print('lets try a scoop of',ice_Cream[3],'with a second scoop of',ice_Cream[1],'on the top')
        print('lets try a scoop of',ice_Cream[2],'with a second scoop of',ice_Cream[2],'on the top')
        print('lets try a scoop of',ice_Cream[1],'with a second scoop of',ice_Cream[3],'on the top')
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[4],'on the top')



        print("Double it up!")
#Task 2:Double Up!
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[1],'on the top')
        print('lets try a scoop of',ice_Cream[1],'with a second scoop of',ice_Cream[2],'on the top')
        print('lets try a scoop of',ice_Cream[2],'with a second scoop of',ice_Cream[3],'on the top')
        print('lets try a scoop of',ice_Cream[3],'with a second scoop of',ice_Cream[4],'on the top')
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[0],'on the top')
        print('Double it up lets try two scoops of',ice_Cream[1])
        print('Double it up lets try two scoops of',ice_Cream[2])
        print('Double it up lets try two scoops of',ice_Cream[3])
        print('Double it up lets try two scoops of',ice_Cream[4])
        print('lets try a scoop of',ice_Cream[4],'with a second scoop of',ice_Cream[0],'on the top')
        print('lets try a scoop of',ice_Cream[3],'with a second scoop of',ice_Cream[1],'on the top')
        print('lets try a scoop of',ice_Cream[2],'with a second scoop of',ice_Cream[2],'on the top')
        print('lets try a scoop of',ice_Cream[1],'with a second scoop of',ice_Cream[3],'on the top')
        print('lets try a scoop of',ice_Cream[0],'with a second scoop of',ice_Cream[4],'on the top')