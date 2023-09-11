## About this project
- Title: Improving Diversity and Preferred Assignment in Dickinson’s First-Year Seminar Selection Process Using Optimization Models
- Advisor: [Professor Dick Forrester](https://www.dickinson.edu/dickforrester) 

### Abstract: 
Dickinson currently uses a process developed by Professor Dick Forrester and Dr. Thanh To (’11) to assign students to First-Year Seminars (FYS). This process utilizes a nonlinear multicriteria optimization model with the goal of assigning students to one of their top-ranked seminars while balancing the classes with regard to gender and the number of international students. In this study, we investigate alternative approaches aiming to improve the run-time and quality of the assignments. Specifically, we consider the linearization of the nonlinear objectives and the use of the hierarchical optimization model. These improvements resulted in a significant reduction in runtime and offer improved flexibility in adjusting assignment outcomes.

## Objective
- Improve the program efficiency and quality of the assignement of the existing program.
- The deployment of this computer program in practice for FYS assignment in Summer 2024 for students in Class of 2028.
- Broaden the impact of this research to other academic institutions.
- Try alternative optimization models to implement the same feature such as hierarchical and blended multi-criteria optimization models.

## Research Materials
- Assignment Models
- Linear/Non-linear Programming
- Integer Programming
- Multi-objective convex quadratic functions (Hierarchial, Combining blended & Hierarchial)
- Normalization 

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
  - `parse.py`: This program parses the data that was provided by Dickinson College and generates the `DickinsonFirstYearSeminar.xlsx` file to be loaded for `run.py`.
    

 


