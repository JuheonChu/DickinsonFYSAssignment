# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:46:08 2022

@author: John Chu & Professor Forrester
"""


from gurobipy import Model
from gurobipy import GRB
from gurobipy import LinExpr
import pandas as pd
import time


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
STUDENTS = gender_df['stu_id']


SEMINARS = [1,2,3, 4,5,6,9,10,11,
		        12,13,14,15,16,17,18,19,20,21,22,
		        23,24,25,26,28,29,30,31,32,33,34,35,36,37,
		        39,41,42,44,45,46,47]

# initializing seminar pick lists from each student
SEMINAR_PICK = student_choices_df['rank']

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
# Create variables
for s in STUDENTS:
   for r in SEMINAR_PICK:
       x[(s,r)] = model.addVar(0.0, 1.0, 0.0, GRB.BINARY,'x_{0}_{1}'.format(s,r)) 
       #x[(s,r)] = model.addVar(vtype=GRB., name='x_{0}_{1}'.format(s,r))
       
# Model.add
for k in SEMINARS:
    FSEM[k] = model.addVar(name='FSEM_{0}'.format(k) )
    MSEM[k] = model.addVar(name='MSEM_{0}'.format(k))
    US_SEM[k] = model.addVar(name='US_SEM_{0}'.format(k))
    NonUS_SEM[k] = model.addVar(name='NonUS_SEM_{0}'.format(k))



end = time.time()
print("The time of execution of adding variables to the model is :",
      (end-start) * 1, "seconds")




# Ensure every student is assigned to one of their seminars (NOT SURE)
start = time.time()
value = LinExpr()

for i in STUDENTS: 
    value = 0
    for j in SEMINAR_PICK:
        value += x[(i,j)]
    model.addConstr(value == 1)

                        

# Create a blank linear expression
exprMale = LinExpr()
exprFemale = LinExpr()
exprUS = LinExpr()
exprNonUS = LinExpr()
  
    
for k in SEMINARS: 
    
    # Reset the expression for every k
    exprMale = 0
    exprFemale = 0
    exprUS = 0
    exprNonUS = 0
    #MSEM[k] = 0
    #FSEM[k] = 0
    #US_SEM[k] = 0
    #NonUS_SEM[k] = 0
    
    model.addVar(name='FSEM_{0}'.format(k))
    model.addVar(name='MSEM_{0}'.format(k))
    model.addVar(name='US_SEM_{0}'.format(k))
    model.addVar(name='NonUS_SEM_{0}'.format(k))
    
    # Build them back out 
    for i in STUDENTS:
        for j in SEMINAR_PICK:
        
            if StudentChoice[i,j] == k:
                if gender[i] == 1:
                    exprMale += 1
                else:
                    exprFemale += 1
    		
                if citizenship[i] == 1:
                    exprUS += 1
                else:
                    exprNonUS += 1
				
    model.addConstr(MSEM[k] == exprMale)
    model.addConstr(FSEM[k] == exprFemale)
    model.addConstr(US_SEM[k] == exprUS)
    model.addConstr(NonUS_SEM[k] == exprNonUS)
    
    # Set seminar capacity (Upper bound)
    model.addConstr(MSEM[k] + FSEM[k] <= 15)
    
    # Set seminar lower bound capacity
    if k != 30: 
        model.addConstr(MSEM[k] + FSEM[k] >= 10)
    
  
end = time.time()

print("The time of setting constraints is :",
      (end-start) * 1, "seconds")



val = LinExpr()
val = 0
for i in STUDENTS:
    for j in SEMINAR_PICK:
        val+=rank_weights[j]*x[i,j]


model.setObjective(val, GRB.MINIMIZE)

# Update Variables and constraints
model.update()

model.setParam('TimeLimit', 2*60)


start = time.time()

# Optimize  
model.optimize()
end = time.time()
print("Time execution of optimizing the model is : ", (end-start) * 1, "seconds")
# Compute an Irreducible Inconsistent Subsystem (IIS)
model.computeIIS()
model.write("model1.ilp")

if model.status == GRB.INFEASIBLE:
    model.feasRelaxS(1, False, False, True)
    start = time.time()

    # Optimize  
    model.optimize()
    end = time.time()
    print("Time execution of optimizing (releaxation) the model is : ", (end-start) * 1, "seconds")
   

#zU_Rank = model.objVal 
#print(zU_Rank)

# Relaxation
#if model.status == GRB.INFEASIBLE:
#    vars = model.getVars()
#    ubpen = [1.0]*model.numVars
#    model.feasRelax(1, False, vars, None, ubpen, None, None)
#    model.optimize()

end = time.time()
print("The time of execution of computing utopian points is :",
      (end-start) * 1, "seconds")





# Solve using Gurobi solver
#opt = SolverFactory('gurobi')
# Make sure to run in 2 minutes
#opt.options['TimeLimit'] = 120
#results = opt.solve(model, tee = True)


# Print the solution
#print('x= ', x.X)
#print('y= ', y.X)