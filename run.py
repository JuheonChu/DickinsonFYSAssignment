# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:46:08 2022

@author: John Chu & Professor Dick Forrester
"""


from gurobipy import Model
from gurobipy import GRB
from gurobipy import LinExpr
import pandas as pd
import time
import gurobipy as gp

model = Model('Student Assignment Problem')


# Loading in the excel file
student_choices_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name='seminar')
citizenship_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'citizenship')
gender_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'gender')
obj_coef_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'obj_coef')
rank_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'rank_weights')




# Time Checking


# initalizing student lists
STUDENTS = gender_df['stu_id'].tolist()


SEMINARS = [1,2,3, 4,5,6,9,10,11,
		        12,13,14,15,16,17,18,19,20,21,22,
		        23,24,25,26,28,29,30,31,32,33,34,35,36,37,
		        39,41,42,44,45,46,47]

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
students = student_choices_df['stu_id']

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



for j in range(len(STUDENTS)):
    citizenship[STUDENTS[j]] = stu_citizen[j]    
    gender[STUDENTS[j]] = stu_gender[j]


for i in range(len(obj_coef_key)):
    obj_coef[obj_coef_key[i]] = obj_coef_val[i]

for j in range(len(rank_idx)):
    rank_weights[rank_idx[j]] = rank_coef[j]

for i in range(len(students)):
    StudentChoice[(students[i], SEMINAR_PICK[i])] = seminar_courses[i]






# Create binary variables in x dictionary
for i in range(len(STUDENTS)):
    for j in range(len([1,2,3,4,5,6])):
        x[STUDENTS[i],SEMINAR_PICK[j]] = model.addVar(0.0, 1.0, 1.0, GRB.BINARY, 'x('+str(STUDENTS[i]) + ','+str([1,2,3,4,5,6][j]) +')')   
        



# Create the variables for number of males, females, US, and NonUS Students in course k
for k in SEMINARS:
    FSEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='FSEM('+str(k)+')')
    MSEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='MSEM('+str(k)+')')
    US_SEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='US_SEM('+str(k)+')')
    NonUS_SEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='NonUS_SEM('+str(k)+')')
    
#FSEM = model.addVars(50,lb=0,vtype=GRB.CONTINUOUS)





# Add the constraint
for i in STUDENTS:
    val = 0
    for j in [1,2,3,4,5,6]:
        val += x[i,j]
    model.addConstr(val == 1, 'AssignCost('+str(i) + ')') 


                        

#exprMale= LinExpr()
#exprFemale = LinExpr()
#exprUS = LinExpr()
#exprNonUS = LinExpr()
    
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
                    #MSEM[k] +=x[i,j]
                    #MSEM[k] += x[i,j]
                    #model.addConstr(MSEM[k] == exprMale, 'NumberMale('+str(k) +')')
                else:
                    #exprFemale += 1
                    exprFemale += x[i,j]
                    #FSEM[k] += 1
    		    # US = 1, international = 0
                if citizenship[i] == 1:
                    #exprUS += 1
                    exprUS += x[i,j]
                    #US_SEM[k] += 1
                else:
                    #exprNonUS += 1
                    exprNonUS += x[i,j]
                    #NonUS_SEM[k] += 1
			
    #print(exprUS)
    model.addConstr(MSEM[k] == exprMale, 'NumberMale('+str(k) +')')
    model.addConstr(FSEM[k] == exprFemale, 'NumberFemale('+str(k) +')')
    model.addConstr(US_SEM[k] == exprUS, 'NumberUS('+str(k) +')')
    model.addConstr(NonUS_SEM[k] == exprNonUS, 'NumberNonUS('+str(k) +')')
     
    # Set seminar capacity (Upper bound)
    model.addConstr(MSEM[k] + FSEM[k] <= 15, 'Capacity('+str(k)+')')
    
    # Set seminar lower bound capacity
    if k != 30: 
        model.addConstr(MSEM[k] + FSEM[k] >= 10, 'LowerCapacity('+str(k)+')')


rank_val = 0
for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        rank_val += rank_weights[j]*x[i,j]

utopian_rank = rank_val

model.setObjective(rank_val, GRB.MINIMIZE)


model.setParam('TimeLimit', 120)


# Optimize  

model.optimize()

zU_Rank = model.getObjective().getValue()

gender_penalty = 0
for j in SEMINARS:
    gender_penalty += (MSEM[j] - FSEM[j])*(MSEM[j] - FSEM[j])

utopian_gender = gender_penalty

model.setObjective(gender_penalty, GRB.MINIMIZE)


model.optimize()

zU_Gender = model.getObjective().getValue()



citizenship_penalty = 0
for j in SEMINARS:
    citizenship_penalty += (US_SEM[j]-NonUS_SEM[j])*(US_SEM[j]-NonUS_SEM[j])

utopian_citizenship = citizenship_penalty

model.setObjective(citizenship_penalty, GRB.MINIMIZE)

model.optimize()

zU_Citizen = model.getObjective().getValue()

# Set the maximum solve time for complete model (in seconds)
model.setParam('TimeLimit', 600)

# Optimize over the weighted (and scaled) objective function

rank_objective = 0


rank_objective = rank_val / -zU_Rank 

gender_objective = 0


gender_objective = gender_penalty / zU_Gender

citizenship_objective = 0

citizenship_objective = citizenship_penalty / zU_Citizen

obj_function = (obj_coef[1] * rank_objective) + (obj_coef[2] * gender_objective) + (obj_coef[3]*citizenship_objective) 

model.setObjective(obj_function, GRB.MINIMIZE)

model.optimize()

optimal_value = model.getObjective().getValue()




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


print("Rank Utopia is: " + str(zU_Rank))
print("Gender Utopia is: " + str(zU_Gender))
print("Citizen Utopia is: " + str(zU_Citizen))
print("Ethnic Utopia is: " + str(zU_Citizen))
print("")
print("Rank Value is: " + str(utopian_rank))
print("Gender Penalty is: " + str(utopian_gender))
print("Citizenship Penalty is: " + str(utopian_citizenship))
print("")
print("================================================")


for k in SEMINARS:
    print("Seminar " + str(k) + " has " + str(FSEM[k].X + MSEM[k].X) + 
        " students with " + str(MSEM[k].X) + " males and " + str(FSEM[k].X) + " females; " +
        str(US_SEM[k].X) + " US and " + str(NonUS_SEM[k].X) + " non-US; ")

f = open("fysAssignment.txt", "w")

for i in STUDENTS:
    for j in [1,2,3,4,5,6]: 
        if x[i,j].X > 0.99:
            f.write("" + str(i) + "\t" + str(StudentChoice[i,j]))
    

f.close()


        