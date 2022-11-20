# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:46:08 2022

@author: 
"""


from gurobipy import Model
from gurobipy import GRB
from gurobipy import LinExpr
import pandas as pd
import time
import gurobipy as gp

model = Model('Student Assignment Problem')

# Time Checking
start = time.time()

# Loading in the excel file
student_choices_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name='seminar')
citizenship_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'citizenship')
gender_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'gender')
obj_coef_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'obj_coef')
rank_df = pd.read_excel('Dickinson First Year Seminar.xlsx', sheet_name = 'rank_weights')

end = time.time()
print("The time of Loading the excel data into the data frame is :",
      (end-start) * 1, "seconds")


# Time Checking
start = time.time()

# initalizing student lists
STUDENTS = gender_df['stu_id'].tolist()


SEMINARS = [1,2,3, 4,5,6,9,10,11,
		        12,13,14,15,16,17,18,19,20,21,22,
		        23,24,25,26,28,29,30,31,32,33,34,35,36,37,
		        39,41,42,44,45,46,47]

# initializing seminar pick lists from each student
SEMINAR_PICK = student_choices_df['rank'].tolist()
print(SEMINAR_PICK)
end = time.time()
print("The time of execution of initializing lists is :",
      (end-start) * 10**3, "ms")



# Time Checking
start = time.time()

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


end = time.time()
print("The time of execution of initializing variables is :",
      (end-start) * 1, "seconds")

# Load in data
start = time.time()
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

end = time.time()
print("The time of execution of loading helper data is :",
      (end-start) * 1, "seconds")

start = time.time()

for j in range(len(STUDENTS)):
    citizenship[STUDENTS[j]] = stu_citizen[j]    
    gender[STUDENTS[j]] = stu_gender[j]


for i in range(len(obj_coef_key)):
    obj_coef[obj_coef_key[i]] = obj_coef_val[i]

for j in range(len(rank_idx)):
    rank_weights[rank_idx[j]] = rank_coef[j]

for i in range(len(students)):
    StudentChoice[(students[i], SEMINAR_PICK[i])] = seminar_courses[i]

end = time.time()

print("The time of execution of loading helper data is :",
      (end-start) * 1, "seconds")


start = time.time()


# Create binary variables in x dictionary

for i in range(len(STUDENTS)):
    for j in range(len([1,2,3,4,5,6])):
        x[STUDENTS[i],SEMINAR_PICK[j]] = model.addVar(0.0, 1.0, 1.0, GRB.BINARY, 'x('+str(STUDENTS[i]) + ','+str([1,2,3,4,5,6][j]) +')')   
        


model.write('dea.lp')



# Create the variables for number of males, females, US, and NonUS Students in course k
for k in SEMINARS:
    FSEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='FSEM('+str(k)+')')
    MSEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='MSEM('+str(k)+')')
    US_SEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='US_SEM('+str(k)+')')
    NonUS_SEM[k] = model.addVar(0.0, float('inf'), 1.0, GRB.CONTINUOUS, name='NonUS_SEM('+str(k)+')')
    
#FSEM = model.addVars(50,lb=0,vtype=GRB.CONTINUOUS)

end = time.time()
print("The time of execution of adding variables to the model is :",
      (end-start) * 1, "seconds")


# Update Variables and constraints
# model.update()


# Ensure every student is assigned to one of their seminars (NOT SURE)
start = time.time()


# Add the constraint
for i in STUDENTS:
    val = 0
    for j in [1,2,3,4,5,6]:
        val += x[i,j]
    model.addConstr(val == 1, 'AssignCost('+str(i) + ')') 

model.write('Assignment.lp')    
                        

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
model.write('capacity.lp')    
  
end = time.time()

print("The time of setting constraints is :",
      (end-start) * 1, "seconds")



val = 0
for i in STUDENTS:
    for j in [1,2,3,4,5,6]:
        val+=rank_weights[j]*x[i,j]

model.setObjective(val, GRB.MINIMIZE)


model.setParam('TimeLimit', 120)


# Optimize  

model.optimize()

zU_Rank = model.getObjective().getValue()
print('utopian rank ' + str(zU_Rank))
total = 0
for j in SEMINARS:
    total += (MSEM[j] - FSEM[j])*(MSEM[j] - FSEM[j])


model.setObjective(total, GRB.MINIMIZE)


model.optimize()

zU_Gender = model.getObjective().getValue()
print('Gender penalty: ' + str(zU_Gender))
#if model.status == GRB.INFEASIBLE:
#    model.feasRelaxS(1, False, False, True)
#    start = time.time()

    # Optimize  
#    model.optimize()
#    end = time.time()
#    print("Time execution of optimizing (releaxation) the model is : ", (end-start) * 1, "seconds")
   

#zU_Rank = model.objVal 
#print(zU_Rank)

# Relaxation
#if model.status == GRB.INFEASIBLE:
#    vars = model.getVars()
#    ubpen = [1.0]*model.numVars
#    model.feasRelax(1, False, vars, None, ubpen, None, None)
#    model.optimize()


