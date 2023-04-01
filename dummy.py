# Set the constraints for each gender and student-type objectives
# e.g. w_gender[1] = |MSEM[1] - FSEM[1]|
for k in SEMINARS:
    model.addConstr(w_gender[k] >= MSEM[k] - FSEM[k])
    model.addConstr(w_gender[k] >= FSEM[k] - MSEM[k])
for k in SEMINARS:
    model.addConstr(w_citizenship[k] >= US_SEM[k] - NonUS_SEM[k])
    model.addConstr(w_citizenship[k] >= NonUS_SEM[k] - US_SEM[k])
model.setObjective(sum(w_gender), GRB.MINIMIZE)
model.optimize()
