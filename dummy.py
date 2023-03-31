# Add constraints for the imbalances and largest gender imbalance
for k in MSEM:
    model.addConstr(imbalance_vars[k] >= MSEM[k] - FSEM[k], name=f"imbalance_constraint_1_{k}")
    model.addConstr(imbalance_vars[k] >= FSEM[k] - MSEM[k], name=f"imbalance_constraint_2_{k}")
    model.addConstr(largest_gender_imbalance >= imbalance_vars[k], name=f"largest_imbalance_constraint_{k}")    

# Find Utopia Point for Gender
model.setObjective(largest_gender_imbalance, GRB.MINIMIZE)

model.optimize()
