# Dickinson College First Year Seminar Student Assignment

## Abstract
This is an independent research conducted by John Chu and supervised by Professor D.Forrester in Dickinson College. In this research, we target to minimize the cost for assigning 660+ Dickinson freshmen into ~42 first year seminar courses while balancing gender and student type ratios and maintaining coure capacities.

## Research Materials

- Assignment Problem (Operations Research)
- Hungarain Method
- Integer Programming
- Multi-objective convex quadratic functions
- Normalization (Nadir Points, Pareto Utopian sets)
- Python Gurobi solver

## PreRequisite
 - Python
 - PyCharm/spyder/Python Idle
 - Gurobi solver

## Set Up

### Install [Python Gurobi Solver](https://www.gurobi.com/downloads/gurobi-software/)

- Choose the right Operating System that fits into the local machine and download the Gurobi Solver
- Issue the Gurobi License ID. 
- Customize the Environment Settings by setting the System variables.

![environment setting](https://user-images.githubusercontent.com/35699839/201580110-9a733a25-05d4-4240-a7f1-f336c2e76b5a.png)


## Dataset

  ### DickinsonFirstYearSeminar.xlsx excel spreadsheet
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
  
  - run.py: rum.py assigns Dickinson first-year students into 40+ seminar courses aiming to balance gender and student-type ratios while maintaining the course capacities.
  - parse.py: parse.py automates to generate the DickinsonFirstYearSeminar.xlsx file based on the data pieces given from the college.
    
  ## Future Improvements
 
  - Handle an exceptional case of students who ask for extraordinary requests in the *run.py*
  - Develop an algorithm that runs the program more in timely efficient manneer. Specifically, I would try implementing this program with Genetic Algorithms if times are allowed.
  - Compute the exact Nadir points used to compute the utopian points for gender, rank, and citizenship.


