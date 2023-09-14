# -*- coding: utf-8 -*-
import pandas as pd
import xlsxwriter

seminar_selection_df = pd.read_excel('2023_Seminar_Selections_Initial.xlsx')


# Function to fill in missing Seminar Ids
def preprocess_data(group):
    for i, row in group.iterrows():
        if pd.isna(row['Seminar Id']):  # Check for NaN instead of zero
            current_order = row['Selection Order']
            target_order = {
                1: 2,
                2: 1,
                3: 2,
                4: 3,
                5: 4,
                6: 5
            }.get(current_order, None)
            
            if target_order is not None:
                target_seminar_id = group.loc[group['Selection Order'] == target_order, 'Seminar Id'].values[0]
                group.at[i, 'Seminar Id'] = target_seminar_id
                
    return group

# Apply the function to each student group
seminar_selection_df = seminar_selection_df.groupby('Student ID').apply(preprocess_data)


# Extract unique student information for citizenship and gender
unique_students = seminar_selection_df.drop_duplicates(subset=['Student ID'])
unique_stu_id = unique_students['Student ID'].tolist()
unique_gender = [1 if g == 'M' else 0 for g in unique_students['Gender']]
unique_citizen = [1 if c == 'US' else 0 for c in unique_students['Citizen Code']]


stu_id = seminar_selection_df['Student ID'].tolist()
seminar_id = seminar_selection_df['Seminar Id'].tolist()
seminar_id = [int(x) if pd.notna(x) else 0 for x in seminar_id]
rank_order = seminar_selection_df['Selection Order'].tolist()
gender = seminar_selection_df['Gender'].tolist()
citizen = seminar_selection_df['Citizen Code'].tolist()

# Convert M to 1 and F to 0
gender = [1 if g == 'M' else 0 for g in gender]
# Convert 'US' to 1 and others to 0
citizen = [1 if c == 'US' else 0 for c in citizen]




seminar_id_write = [None] * len(seminar_id)
for i in range(len(seminar_id)):
    seminar_id_write[i] = int(str(seminar_id[i])[-2:])


workbook = xlsxwriter.Workbook('parsed.xlsx')
worksheet_citizenship = workbook.add_worksheet('citizenship')
worksheet_gender = workbook.add_worksheet('gender')
worksheet_obj_coef = workbook.add_worksheet('obj_coef')
worksheet_rank_weights = workbook.add_worksheet('rank_weights')
worksheet_seminar = workbook.add_worksheet('seminar')
worksheet_course_num = workbook.add_worksheet('course_num')

citizenship_dict = {'student_id': stu_id,
           'citizen': citizen}

gender_dict={
    'stu_id':stu_id,
    'gender': gender         
    }

obj_coef_dict = {
    'obj_coef_key':[1,2,3],
    'obj_coef': [1,4,1]
    }

rank_weights_dict = {
    'rank_index': [1,2,3,4,5,6],
    'rank_weights': [-70, -60, -30, 1, 100, 300]
    }

seminar_dict = {
    'stu_id': stu_id,
    'rank': rank_order,
    'seminar': seminar_id_write
    }

course_num_dict={
    'seminar_no': list(set(seminar_id_write))
    }

# Write to 'citizenship' sheet
citizenship_dict = {'student_id': unique_stu_id, 'citizen': unique_citizen}
col = 0
for key, value in citizenship_dict.items():
    worksheet_citizenship.write(0, col, key)
    worksheet_citizenship.write_column(1, col, value)
    col += 1

# Write to 'gender' sheet
gender_dict = {'stu_id': unique_stu_id, 'gender': unique_gender}
col = 0
for key, value in gender_dict.items():
    worksheet_gender.write(0, col, key)
    worksheet_gender.write_column(1, col, value)
    col += 1

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
