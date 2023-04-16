# Construct blended multi-objectives
obj_functions = sum([obj_coef[1] * f_rank, obj_coef[2] * f_gender, 
                     obj_coef[3] * f_stu_type])
model.setObjective(obj_functions, GRB.MINIMIZE)
model.optimize()
