# Dickinson College First Year Seminar Student Assignment

## Abstract
This is an independent research conducted by John Chu and supervised by Professor D.Forrester in Dickinson College. In this research, we target to minimize the cost for assigning 660+ Dickinson freshmen into ~42 first year seminar courses while balancing gender and student type ratios and maintaining coure capacities.

## Research Contexts

- Assignment Problem (Operations Research)
- Hungarain Method
- multi-objective convex quadratic functions
- Normalization (Nadir Points, Pareto Utopian sets)
- Python Gurobi solver

## PreRequisite
 - Python
 - PyCharm/spyder/Python Idle

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
    
    
    
    
    
  ## Future Improvements



