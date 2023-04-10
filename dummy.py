# Add constraints for Gender Penalty 
for k in MSEM:
  # Minimize the Gender Penalty
  model.addConstr(gen_penalty[k] >= MSEM[k] - FSEM[k])
  model.addConstr(gen_penalty[k] >= FSEM[k] - MSEM[k])
  model.addConstr(g >= gen_penalty[k])
# Add constraints for Citizenship Penalty
for k in US_SEM:
  # Minimize the Citizenship Penalty
  model.addConstr(citizenship_penalty[k] >= MSEM[k] - FSEM[k])
  model.addConstr(citizenship_penalty[k] >= FSEM[k] - MSEM[k])
  model.addConstr(c >= citizenship_penalty[k])
  
