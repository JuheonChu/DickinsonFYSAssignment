# Ensure to allow relative tolerance for less-prioritized objectives
zU_Rank = model.getObjective().getValue()
model.addConstr(f_rank <= 0.999999999 * zU_Rank, "Rank")
model.addConstr(g <= 1.0000000001 * zU_Gender, "Gender")

model.setObjective(g, GRB.MINIMIZE)
model.optimize()
