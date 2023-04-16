# Minimize the imbalances in gender and number of international students.
for k in SEMINARS:
    model.addConstr(w_gender[k] >= MSEM[k] - FSEM[k])
    model.addConstr(w_gender[k] >= FSEM[k] - MSEM[k])
    model.addConstr(w_citizenship[k] >= US_SEM[k] - NonUS_SEM[k])
    model.addConstr(w_citizenship[k] >= NonUS_SEM[k] - US_SEM[k])
    model.addConstr(w_gender[k] <= GP_threshold)
    model.addConstr(NonUS_SEM[k] <= CP_threshold)
