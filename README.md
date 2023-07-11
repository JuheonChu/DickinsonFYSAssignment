# Improving Diversity and Preferred Assignment in Dickinson’s First-Year Seminar Selection Process Using Optimization Models

This is a student-faculty collaborative research with Professor Dick Forrester at Dickinson College to accomplish assigning Dickinson first-year students into their First-Year Seminar courses in timely and efficient manner.


## Research Materials

- Assignment Problem (Operations Research)
- Linear/Non-linear Programming
- Integer Programming
- Multi-objective convex quadratic functions (Hierarchial, Combining blended & Hierarchial)
- Normalization (Nadir Points, utopian points)
- Linearize non-linear functions

## Research Objectives

- Linearize convex quadratic gender and citizenship objectives
- Hierarchial multi-objectives
- Blended multi-objectives

## PreRequisite
 - Python
 - PyCharm/spyder/Python Idle
 - Gurobi solver

## Set Up

### 1. Install [Python Gurobi Solver](https://www.gurobi.com/downloads/gurobi-software/)

- Choose the right Operating System that fits into the local machine and download the Gurobi Solver
- Issue the Gurobi License ID. 
- Customize the Environment Settings by setting the System variables.

![environment setting](https://user-images.githubusercontent.com/35699839/201580110-9a733a25-05d4-4240-a7f1-f336c2e76b5a.png)

### 2. Install xlsxwriter
- This is required to successfully automate the given information from Dickinson College to load it into run.py.

## Dataset

  ### DickinsonFirstYearSeminar.xlsx excel spreadsheet
  When we parse the dataset provided by college via `parse.py`, this results in producing `DickinsonFirstYearSeminar.xlsx` file which is able to be 
  loaded into our `run.py`. This file contains the following student information.
  - citizenship
    - student_id: Student id that uniquely identifies each student in Dickinson.
    - citizenship: 0 (internatinoal students) or 1 (U.S domestic students).
  - gender
    - student_id: Student id that uniquely identifies each student in Dickinson.
    - gender: 0 (female) or 1 (male)
  - obj_coef
    - obj_coef_key: An index of the coefficients for each objective function.
    - obj_coef: An object coefficient value
  - rank
    - rank_index: An index of the rank values in an order that student prefers to take seminar courses.
    - rank_weights: A rank weight value. The lower rank weight value is, the higher priority that the corresponding ranked course is considered accordingly.
  - seminar
    - stu_id: Student id that uniquely identifies each student in Dickinson.
    - rank: rank values (1-6). Each student can prioritize 6 courses in one's order.
    - seminar: a seminar course that the student selected.
  - course_num
    - seminar_no: seminar course number
    
  ## Program Functionality
  
  - `run.py`: This assigns Dickinson first-year students into 40+ seminar courses aiming to balance gender and student-type ratios while maintaining the course capacities. Among many versions of running this program, run.py specifically describes the program that shows the best performance in timely and efficient manner.
  - `parse.py`: This auto-generates the `DickinsonFirstYearSeminar.xlsx` file based on the data pieces given from the college.
    

 


