# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:46:08 2022
@author: John Chu, Prof. Dick Forrester
"""


from gurobipy import Model
from gurobipy import GRB
from gurobipy import quicksum
import gurobipy as gp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

model = Model('Student Assignment Problem')


# Loading in the excel file
student_choices_df = pd.read_excel('parsed.xlsx', sheet_name='seminar',engine='openpyxl')
citizenship_df = pd.read_excel('parsed.xlsx', sheet_name = 'citizenship',engine='openpyxl')
gender_df = pd.read_excel('parsed.xlsx', sheet_name = 'gender',engine='openpyxl')
obj_coef_df = pd.read_excel('parsed.xlsx', sheet_name = 'obj_coef',engine='openpyxl')
rank_df = pd.read_excel('parsed.xlsx', sheet_name = 'rank_weights',engine='openpyxl')
course_df = pd.read_excel('parsed.xlsx', sheet_name = 'course_num',engine='openpyxl')


# initalizing student lists
STUDENTS = gender_df['stu_id'].tolist()


SEMINARS = course_df['seminar_no'].tolist()



# initializing seminar pick lists from each student
SEMINAR_PICK = student_choices_df['rank'].tolist()



# Parameters
StudentChoice = dict()
gender = dict()
citizenship = dict()
rank_weights = dict()
obj_coef = dict()

# array(STUDENTS, SEMINAR_PICK) of mpvar
x = dict() 

# array(SEMINARS) of mpvar
MSEM = dict()
FSEM = dict()
US_SEM = dict()
NonUS_SEM = dict()

## Variables for the Linearizing Gender and Citizenships objectives
w_gender = dict()
w_citizenship = dict()

# Utopian points
zU_Rank = 0
zU_Gender = 0
zU_Citizen = 0
zU_Ethnicity = 0

# array(SEMINARS) of real
MSEMU_Rank = dict()
FSEMU_Rank = dict()
US_SEMU_Rank = dict()
NonUS_SEMU_Rank = dict()


# bookkeeping variables used to help keep track of statistics of optimal assignments
numFirstChoice = 0
numSecondChoice =0 
numThirdChoice = 0 
numFourthChoice = 0
numFifthChoice = 0
numSixthChoice = 0

num16 = 0
num15 = 0
num14 = 0
num13 = 0 
num12 = 0 
num11 = 0
num10 = 0
num9 = 0
num8 = 0
num7 = 0
num6 = 0
num5 = 0 




# Load in data

# seminar.dat
seminar_courses = student_choices_df['seminar']

# citizenship.dat
stu_citizen = citizenship_df['citizen']

# gender.dat
stu_gender = gender_df['gender']

# obj_coef.dat (1: 69, 2: 20, 3: 40)
obj_coef_key = obj_coef_df['obj_coef_key']
obj_coef_val = obj_coef_df['obj_coef'] 

# rank.dat 
rank_idx =  rank_df['rank_index']
rank_coef = rank_df['rank_weights']



# The following variables are used to store the Utopia Points
# which we will use to compute the Nadir points
#############################################################
## Variables for the Gender Utopia Point
W_G_Star = dict()
x_G_Star = dict()

## Variables for the Citizenship Utopia Point
W_C_Star = dict()
x_C_Star = dict()

## Variables for the Rank Utopia Point
W_R_Star = dict()
x_R_Star = dict()


idx = 0
for i in range(len(STUDENTS)):
    citizenship[STUDENTS[i]] = stu_citizen[i]    
    gender[STUDENTS[i]] = stu_gender[i]
    # Create binary variables in x dictionary & Student choices in StudentChoice dictionary
    for j in range(len([1,2,3,4,5,6])):
            x[STUDENTS[i],SEMINAR_PICK[j]] = model.addVar(0.0, 1.0, 1.0, GRB.BINARY, 'x('+str(STUDENTS[i]) + ','+str([1,2,3,4,5,6][j]) +')')
            StudentChoice[STUDENTS[i], SEMINAR_PICK[j]] = seminar_courses[idx]
            idx+=1

# They are just 9 operations in-total
for i in range(len(obj_coef_key)):
    obj_coef[obj_coef_key[i]] = obj_coef_val[i]

for j in range(len(rank_idx)):
    rank_weights[rank_idx[j]] = rank_coef[j]


# Create the variables for number of males, females, US, and NonUS Students in course k
for k in SEMINARS:
    FSEM[k] = model.addVar(lb = 0.0, ub = float('inf'), vtype= GRB.CONTINUOUS, name='FSEM('+str(k)+')')
    MSEM[k] = model.addVar(lb = 0.0, ub = float('inf'), vtype= GRB.CONTINUOUS, name='MSEM('+str(k)+')')
    US_SEM[k] = model.addVar(lb= 0.0, ub = float('inf'), vtype= GRB.CONTINUOUS, name='US_SEM('+str(k)+')')
    NonUS_SEM[k] = model.addVar(lb = 0.0, ub = float('inf'), vtype = GRB.CONTINUOUS, name='NonUS_SEM('+str(k)+')')
    w_gender[k] = model.addVar(lb = -float('inf'), ub = float('inf'), vtype = GRB.CONTINUOUS, name='w_gender('+str(k)+')')
    w_citizenship[k] = model.addVar(lb = -float('inf'), ub = float('inf'), vtype = GRB.CONTINUOUS, name='w_citizenship('+str(k)+')')


# Add the constraint
for i in STUDENTS:
    val = 0
    for j in [1,2,3,4,5,6]:
        val += x[i,j]
    model.addConstr(val == 1, 'AssignCost('+str(i) + ')') 




# Prompt the user for general lower and upper bounds for course capacities
general_lower_bound = int(input("What is the general lower bound for course capacities? "))
general_upper_bound = int(input("What is the general upper bound for course capacities? "))

# Ask for seminars with specific capacities
specific_seminars = input("Do you have any seminars that you want to set with different upper bound and lower bound capacities? (Y/N) ")

bounds = {}

seminar_ids = []

if specific_seminars == "Y":
    sem_ids = input("Please enter the seminar IDs separated by commas (e.g. 11, 12, 13): ").split(",")
    seminar_ids = sem_ids
    for sem_id in sem_ids:
        lower = int(input(f"What is the lower bound for seminar {sem_id.strip()}? "))
        upper = int(input(f"What is the upper bound for seminar {sem_id.strip()}? "))
        bounds[int(sem_id.strip())] = (lower, upper)

for i in range(len(seminar_ids)):
    seminar_ids[i] = int(seminar_ids[i])


for k in SEMINARS: 
    
    exprMale = 0
    exprFemale = 0
    exprUS = 0
    exprNonUS = 0
    
 
    # Build them back out 
    for i in STUDENTS:
        for j in [1,2,3,4,5,6]:
        
            if StudentChoice[i,j] == k:
                # male = 1, female = 0
                if gender[i] == 1:
                    exprMale += x[i,j]
                   
                else:
                   exprFemale += x[i,j]
    		# US citizen = 1, international students = 0    
                if citizenship[i] == 1:
                    
                    exprUS += x[i,j]
                    
                else:
                    exprNonUS += x[i,j]
			

       

    model.addConstr(MSEM[k] == exprMale, 'NumberMale('+str(k) +')')
    model.addConstr(FSEM[k] == exprFemale, 'NumberFemale('+str(k) +')')
    model.addConstr(US_SEM[k] == exprUS, 'NumberUS('+str(k) +')')
    model.addConstr(NonUS_SEM[k] == exprNonUS, 'NumberNonUS('+str(k) +')')
     
    
    # Set seminar lower bound capacity
    if k in seminar_ids: 
        print(k)
        model.addConstr(MSEM[k] + FSEM[k] >= bounds[k][0], 'LowerCapacity('+str(k)+')')
        model.addConstr(MSEM[k] + FSEM[k] <= bounds[k][1], 'UpperCapacity('+str(k)+')')
    else: 
        model.addConstr(MSEM[k] + FSEM[k] >= general_lower_bound, 'LowerCapacity('+str(k)+')')
        model.addConstr(MSEM[k] + FSEM[k] <= general_upper_bound, 'UpperCapacity('+str(k)+')')

# Set the constraints for each w_gender and w_citizenship 
for k in SEMINARS:
    model.addConstr(w_gender[k] >= MSEM[k] - FSEM[k])
    model.addConstr(w_gender[k] >= FSEM[k] - MSEM[k])
    model.addConstr(w_gender[k] <= 6)


    
for k in SEMINARS:
    model.addConstr(w_citizenship[k] >= US_SEM[k] - NonUS_SEM[k])
    model.addConstr(w_citizenship[k] >= NonUS_SEM[k] - US_SEM[k])
    model.addConstr(NonUS_SEM[k] <= 3)

# Define the rank objective 
rank_val = 0
for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        rank_val += rank_weights[j]*x[i,j]

model.setObjective(rank_val, GRB.MINIMIZE)

model.optimize()

zU_Rank = model.getObjective().getValue()

# Record the Utopia Point for Rank
for k in SEMINARS:
    W_R_Star[k] = [w_gender[k].X, w_citizenship[k].X]


for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        x_R_Star[i,j] = x[i,j].X
		
# Find Utopia Point for Gender
############################
model.setObjective(sum(w_gender.values()), GRB.MINIMIZE)
model.optimize()

zU_Gender = model.getObjective().getValue()

# Record the Utopia Point for Gender
for k in SEMINARS:
	W_G_Star[k] = [w_gender[k].X ,w_citizenship[k].X]
	
for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        x_G_Star[i,j] = x[i,j].X

# Find Utopia Point for Citizenship
###################################

model.setObjective(sum(w_citizenship.values()), GRB.MINIMIZE)

model.optimize()

zU_Citizen = model.getObjective().getValue()

# Record the Utopia Point for Citizenship
for k in SEMINARS:
	W_C_Star[k] = [w_gender[k].X, w_citizenship[k].X]

for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        x_C_Star[i,j] = x[i,j].X

## Find Nadir Point for Rank
############################
f1 = 0
f2 = 0
f3 = 0
for i in STUDENTS:
	for j in [1,2,3,4,5,6]:
		f1 += rank_weights[j]*x_R_Star[i,j]
		f2 += rank_weights[j]*x_G_Star[i,j]
		f3 += rank_weights[j]*x_C_Star[i,j]			

zN_Rank = max(f1, f2, f3)

## Find Nadir Point for Gender
##############################
f1 = 0
f2 = 0
f3 = 0
for j in SEMINARS:
    f1 += W_R_Star[j][0]
    f2 += W_G_Star[j][0]
    f3 += W_C_Star[j][0]
    
zN_Gender = max(f1, f2, f3)


## Find Nadir Point for Citizenship
###################################
f1 = 0
f2 = 0
f3 = 0

for j in SEMINARS:
    f1 += W_R_Star[j][1]
    f2 += W_G_Star[j][1]
    f3 += W_C_Star[j][1]
    
zN_Citizen = max(f1, f2, f3)


## Solve the multiobjective assignment problem
##############################################
# Normalize the rank objective function 
f_rank = (rank_val - zU_Rank) / (zN_Rank - zU_Rank)

# Normalize gender objective function
f_gender = (sum(w_gender.values()) - zU_Gender) / (zN_Gender - zU_Gender)

# Normalize ctizienship objective function
f_citizenship = (sum(w_citizenship.values()) - zU_Citizen) / (zN_Citizen - zU_Citizen + 1)

obj_functions = [f_rank, f_gender, f_citizenship]

obj_names = ["rank", "gender", "citizenship"]

obj_priority = [1,2,3]

# Set and configure objectives
for i in range(len(obj_functions)):
    obj_function = obj_functions[i]
    model.setObjectiveN(expr = obj_function, index = i, priority = obj_priority[i], weight = obj_coef[i+1], abstol = 0, reltol=0.05, name = obj_names[i])


model.optimize()


# Print out the solution

print("The total number of first-year students: " + str(len(STUDENTS)))
print("The total number of seminars: " + str(len(SEMINARS)))
print("")

tot_female = 0
tot_male = 0
tot_US = 0
tot_NonUS = 0

for k in SEMINARS:
    tot_female += FSEM[k].X
    
    tot_male += MSEM[k].X
    tot_US += US_SEM[k].X
    tot_NonUS += NonUS_SEM[k].X
    
    
print("Number of female students: " + str(tot_female))
print("Number of male students: " + str(tot_male))
print("")
print("Number of US Citizens: " + str(tot_US))
print("Number of Non US Citizens: " + str(tot_NonUS))
print("")
print("  Rank weight 1: ", rank_weights[1])
print("  Rank weight 2: ", rank_weights[2])
print("  Rank weight 3: ", rank_weights[3])
print("  Rank weight 4: ", rank_weights[4])
print("  Rank weight 5: ", rank_weights[5])
print("  Rank weight 6: ", rank_weights[6])
print("")
print("  Objective Coefficient 1: ", obj_coef[1])
print("  Objective Coefficient 2: ", obj_coef[2])
print("  Objective Coefficient 3: ", obj_coef[3])
print("")
print("================================================")

if (tot_male + tot_female) >= (len(STUDENTS)-0.5):
    print("All students were assigned")
else:
    print("Not all students were assigned!")
    print("")
    print("Num assigned: " + str(tot_male + tot_female))
    print("Num students: ", len(STUDENTS))
 
print("")
print("================================================")

for i in STUDENTS:
    if x[i,1].X== 1:
        numFirstChoice+=1
    
    if x[i,2].X == 1:
        numSecondChoice +=1
    
    if x[i,3].X == 1:
        numThirdChoice += 1
    
    if x[i,4].X == 1:
        numFourthChoice += 1
    
    if x[i,5].X == 1:
        numFifthChoice += 1
    
    if x[i,6].X == 1:
        numSixthChoice += 1

for k in SEMINARS:
    if FSEM[k].X + MSEM[k].X >= 15.5:
        num16 += 1
    elif FSEM[k].X + MSEM[k].X >= 14.5:
        num15 += 1
    elif FSEM[k].X + MSEM[k].X >= 13.5:
        num14 += 1
    elif FSEM[k].X + MSEM[k].X >= 12.5:
        num13 += 1
    elif FSEM[k].X + MSEM[k].X >= 11.5:
        num12 += 1
    elif FSEM[k].X + MSEM[k].X >= 10.5:
        num11 += 1
    elif FSEM[k].X + MSEM[k].X >= 9.5:
        num10 += 1
    elif FSEM[k].X + MSEM[k].X >= 8.5:
        num9 += 1
    elif FSEM[k].X + MSEM[k].X >= 7.5:
        num8 += 1
    elif FSEM[k].X + MSEM[k].X >= 6.5:
        num7 += 1
    elif FSEM[k].X + MSEM[k].X >= 5.5:
        num6 += 1
    elif FSEM[k].X + MSEM[k].X >= 4.5:
        num5 += 1

print("" + str(numFirstChoice) + " (" + str(numFirstChoice/len(STUDENTS)*100) + "%) students were assigned their first-choice.")
print("" + str(numSecondChoice) + " (" + str(numSecondChoice/len(STUDENTS)*100) + "%) students were assigned their second-choice.")
print("" + str(numThirdChoice) + " (" + str(numThirdChoice/len(STUDENTS)*100) + "%) students were assigned their third-choice.")
print("" + str(numFourthChoice) + " (" + str(numFourthChoice/len(STUDENTS)*100) + "%) students were assigned their fourth-choice.")
print("" + str(numFifthChoice) + " (" + str(numFifthChoice/len(STUDENTS)*100) + "%) students were assigned their fifth-choice.")
print("" + str(numSixthChoice) + " (" + str(numSixthChoice/len(STUDENTS)*100) + "%) students were assigned their sixth-choice.")
print("")
print("================================================")
print("")


if num16 > 0:
  print("" + str(num16) + " seminars have 16 students")

if num15 > 0:
  print("", num15, " seminars have 15 students")


if num14 > 0:
  print("" + str(num14) + " seminars have 14 students")


if (num13 > 0):
  print("" + str(num13) + " seminars have 13 students")


if num12 > 0:
  print("" + str(num12) + " seminars have 12 students")


if (num11 > 0):
  print("" + str(num11) + " seminars have 11 students")


if num10 > 0:
  print("" + str(num10) + " seminars have 10 students")


if num9 > 0:
  print("" + str(num9) + " seminars have 9 students")


if num8 > 0:
  print("" + str(num8) + " seminars have 8 students")


if num7 > 0:
  print("" + str(num7) + " seminars have 7 students")


if num6 > 0:
  print(""+ str(num6) + " seminars have 6 students")


if num5 > 0:
  print("" + str(num5) + " seminars have 5 students")

print("")
print("================================================")
print("")



utopian_rank = 0
utopian_gender = 0
utopian_citizen = 0

for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        utopian_rank += rank_weights[j]*x[i,j].X

for j in SEMINARS:
    utopian_gender += (MSEM[j].X - FSEM[j].X)* (MSEM[j].X - FSEM[j].X)
    utopian_citizen += (US_SEM[j].X - NonUS_SEM[j].X) * (US_SEM[j].X - NonUS_SEM[j].X)

print("Rank Utopia is: " + str(int(zU_Rank)))
print("Gender Utopia is: " + str(int(zU_Gender)))
print("Citizen Utopia is: " + str(int(zU_Citizen)))
print("Ethnic Utopia is: " + str(int(zU_Citizen)))
print("")
print("Rank Value is: " + str(int(utopian_rank)))
print("Gender Penalty is: " + str(int(utopian_gender)))
print("Citizenship Penalty is: " + str(int(utopian_citizen)))
print("")
print("================================================")

################ Compute Variance #########################

for k in SEMINARS:
     print("Seminar " + str(k) + " has " + str(int(FSEM[k].X + MSEM[k].X)) + 
        " students with " + str(int(MSEM[k].X)) + " males and " + str(int(FSEM[k].X)) + " females; " +
        str(int(US_SEM[k].X)) + " US and " + str(int(NonUS_SEM[k].X)) + " non-US; ")
   


gen_list = [abs(MSEM[k].x - FSEM[k].X) for k in SEMINARS]
stu_list = [abs(US_SEM[k].x - NonUS_SEM[k].X) for k in SEMINARS]

print('Gender variance: ' + str(statistics.pvariance(gen_list)))
print('stu-type variance: ' + str(statistics.pvariance(stu_list)))

f = open("fysAssignmentNonLinear.txt", "w")

for i in STUDENTS:
    for j in [1,2,3,4,5,6]: 
        if x[i,j].X > 0.99:
            f.write("" + str(i) + "\t" + str(StudentChoice[i,j]) + "\n")
    

f.close()


##################################################################
######################### Plot the result ########################

x = np.arange(len(SEMINARS))
y1 = [0 for i in range(len(SEMINARS))]
y2 = [0 for i in range(len(SEMINARS))]
y3 = [0 for i in range(len(SEMINARS))]
y4 = [0 for i in range(len(SEMINARS))]

j = 0
for k in SEMINARS:
    y1[j] = MSEM[k].X
    y2[j] = FSEM[k].X
    y3[j] = US_SEM[k].X
    y4[j] = NonUS_SEM[k].X
    j+=1
    
width = 0.25


fig, axs = plt.subplots()
fig = plt.figure(figsize=(17, 6)) # Create matplotlib figure
axs.set_title('Dickinson First-Year Seminar Assignment')

# plot data in grouped manner of bar type
plt.bar(x-0.3, y1, width, color='cyan')
plt.bar(x-0.1, y2, width, color='orange')
plt.bar(x+0.1, y3, width, color='green')
plt.bar(x+0.3, y4, width, color='red')
plt.xticks(x, SEMINARS)
plt.xlabel("Seminars")
plt.ylabel("Students")
plt.legend(["Male", "Female", "US", "International"])
plt.show()
