# Minimize the imbalances in gender and number of international students.
for k in SEMINARS:
    model.addConstr(w_gender[k] <= GP_threshold)
    model.addConstr(NonUS_SEM[k] <= CP_threshold)
