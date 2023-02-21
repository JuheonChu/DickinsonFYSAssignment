# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:23:14 2022

Generates an excel file to be loaded into run.py

@author: johnc
"""

import pandas as pd
import xlsxwriter

seminar_selection_df= pd.read_excel('2022_Seminar_Selections_reduced.xlsx', sheet_name='ag-grid')

# write to sheet_name = "seminar", column: 'stu_id'
stu_id = seminar_selection_df['Id'].tolist()


seminar_id = seminar_selection_df['Seminar Id'].tolist()

# write to sheet_name = "seminar", column: 'rank'
rank_order = seminar_selection_df['Selection Order'].tolist()

# 'M' or 'F'
gender = seminar_selection_df['Gender'].tolist()

# 'US': 1, NonUS: 0
citizen = seminar_selection_df['Citizen Code'].tolist()


# wriet to sheet_name = "seminar", column: 'seminar'
seminar_id_write = [None] * len(seminar_id)

# Parse the Seminar Id by getting the last 2 digits
for i in range(len(seminar_id)):
    seminar_id_write[i] = int(str(seminar_id[i])[-2:])


# Generate a distinct student set
# write to sheet_name = "citizenship", column: 'student_id'
#          sheet_name = "gender", column: 'stu_id'

num_students = int(len(stu_id)/6)

STUDENTS = [None] * num_students

for i in range(0, len(stu_id), 6):
    idx = int(i/6)
    STUDENTS[idx] = stu_id[i]
    

GENDER = [None] * num_students

for i in range(0, len(gender), 6):
    idx = int(i/6)
    
    if gender[i] == 'M':
        GENDER[idx] = 1
    elif gender[i] == 'F':
        GENDER[idx] = 0
    else:
        # In case of Non-binary identification of gender,
        # I meant to say 0 as "non-male"
        GENDER[idx] = 0

# shet_name = "citizenship"
US_CITIZEN = [None] * num_students

for i in range(0, len(citizen), 6):
    idx = int(i/6)
    
    if citizen[i] == "US":
        US_CITIZEN[idx] = 1
    else:
        # Any non-US students have '0'
        US_CITIZEN[idx] = 0

# sheet_name = "obj_coef" (column == var name)
obj_coef_key = [1,2,3]
obj_coef = [1,4,1]

# sheet_name = "rank_weights"
rank_index = [1,2,3,4,5,6]
rank_weights = [-70, -60, -30, 1, 100, 300]


set_seminar = set(seminar_id_write) 

# DISTINCT SEMINAR list
SEMINAR = (list(set_seminar))
 

# Write an Excel file 

workbook = xlsxwriter.Workbook('write_dict.xlsx')

worksheet_citizenship = workbook.add_worksheet('citizenship')
worksheet_gender = workbook.add_worksheet('gender')
worksheet_obj_coef = workbook.add_worksheet('obj_coef')
worksheet_rank_weights = workbook.add_worksheet('rank_weights')
worksheet_seminar = workbook.add_worksheet('seminar')
worksheet_course_num = workbook.add_worksheet('course_num')


citizenship_dict = {'student_id': STUDENTS,
           'citizen': US_CITIZEN}

gender_dict={
    'stu_id':STUDENTS,
    'gender': GENDER         
    }

obj_coef_dict = {
    'obj_coef_key':obj_coef_key,
    'obj_coef': obj_coef
    }

rank_weights_dict = {
    'rank_index': rank_index,
    'rank_weights': rank_weights
    }

seminar_dict = {
    'stu_id': stu_id,
    'rank': rank_order,
    'seminar': seminar_id_write
    }

course_num_dict={
    'seminar_no': SEMINAR
    }

col_num = 0

for key, value in citizenship_dict.items():
    worksheet_citizenship.write(0, col_num, key)
    worksheet_citizenship.write_column(1, col_num, value)
    col_num += 1

col_num = 0

for key, value in gender_dict.items():
    worksheet_gender.write(0, col_num, key)
    worksheet_gender.write_column(1, col_num, value)
    col_num += 1

col_num = 0

for key, value in obj_coef_dict.items():
    worksheet_obj_coef.write(0, col_num, key)
    worksheet_obj_coef.write_column(1, col_num, value)
    col_num += 1

col_num = 0

for key, value in rank_weights_dict.items():
    worksheet_rank_weights.write(0, col_num, key)
    worksheet_rank_weights.write_column(1, col_num, value)
    col_num += 1

col_num = 0

for key, value in seminar_dict.items():
    worksheet_seminar.write(0, col_num, key)
    worksheet_seminar.write_column(1, col_num, value)
    col_num += 1

col_num = 0

for key, value in course_num_dict.items():
    worksheet_course_num.write(0, col_num, key)
    worksheet_course_num.write_column(1, col_num, value)
    col_num += 1    
    
workbook.close()    

    

