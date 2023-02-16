# Dickinson College First Year Seminar Student Assignment

## Abstract
This is an independent research conducted by John Chu and supervised by Professor D.Forrester in Dickinson College. 

## Acknowledgement
First and foremost, I want to convey my profound appreciation to Dr. Forrester, Richard from Dickinson College for his specialized knowledge in operations research (OR) and his clear direction and unwavering encouragement during this research.

## Objectives
In this research, we want to generate an automated program that targets to minimize the cost for assigning 660+ Dickinson freshmen into ~42 first year seminar courses while balancing gender and student type ratios and maintaining coure capacities. We will implement this program using a variety of techniques and compare one another to select the best one to be operable for assigning incoming new Dickinson first-year students. 


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

### 1. Install [Python Gurobi Solver](https://www.gurobi.com/downloads/gurobi-software/)

- Choose the right Operating System that fits into the local machine and download the Gurobi Solver
- Issue the Gurobi License ID. 
- Customize the Environment Settings by setting the System variables.

![environment setting](https://user-images.githubusercontent.com/35699839/201580110-9a733a25-05d4-4240-a7f1-f336c2e76b5a.png)

### 2. Install xlsxwriter
- This is required to successfully automate the given information from Dickinson College to load it into run.py.

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
  
  - run.py: rum.py assigns Dickinson first-year students into 40+ seminar courses aiming to balance gender and student-type ratios while maintaining the course capacities. Among many versions of running this program, run.py specifically describes the program that shows the best performance in timely and efficient manner.
  - parse.py: parse.py automates to generate the DickinsonFirstYearSeminar.xlsx file based on the data pieces given from the college.
    
  ## Conclusion
 We have implemented three versions of python program that improved the original program functionalities that were used by Dickinson College. First, the initial version directly converts a Mosel assignment program, and we figured out that Python Gurobi solver provides better optimal and utopian points via finding smaller mimized values. Then, we upgraded this functionality by precisely normalizing the objectives. This was accomplished by computing the nadir points. As denoted in Thanh To's Honors research with Dr. Forrester, we need nadir points to normalize scales between three objective functions: rank, gender, and citizenships. The output shows a slightly more balanced results for balancing gender and student type in the classroom. However, we are still struggling with extremely long program run-time. Hence, we enhanced this aspect by linearizing the nonlinear gender and citizenship objectives. It was quadratic that use sum-squared-differences method, but we converted computing those gender and citizenship penalties by summing up the absolute value of differences between males and females and U.S students and international students in the classroom. However, the absolute value function is nonlinear. Hence, we linearized this nonlinear function using the fair allocation technique introduced in OR studies. Due to the linearized gender and citizenship objectives, the empirical analysis of this algoritm shows approximately 1 second to run whereas it took 5 minutes from the first two versions of this program.
  
  
  
  ## Future Improvements

 


