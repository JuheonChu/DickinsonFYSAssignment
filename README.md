![Dickinson logo](https://github.com/JuheonChu/DickinsonFYSAssignment/assets/35699839/e00c566f-da16-4820-8645-5ec63394964d)

## About this project
- Title: Improving Diversity and Preferred Assignment in Dickinson’s First-Year Seminar Selection Process Using Optimization Models
- Advisor: [Professor Dick Forrester](https://www.dickinson.edu/dickforrester) 

### Abstract: 
Dickinson currently uses a process developed by Professor Dick Forrester and Dr. Thanh To (’11) to assign students to First-Year Seminars (FYS). This process utilizes a nonlinear multicriteria optimization model with the goal of assigning students to one of their top-ranked seminars while balancing the classes with regard to gender and the number of international students. In this study, we investigate alternative approaches aiming to improve the run-time and quality of the assignments. Specifically, we consider the linearization of the nonlinear objectives and the use of the hierarchical optimization model. These improvements resulted in a significant reduction in runtime and offer improved flexibility in adjusting assignment outcomes. The overarching aim of this study is to contribute robust optimization approaches that can be widely adopted across educational institutions.

## Objective
- Improve the program efficiency and quality of the assignement of the existing program.
- The deployment of this computer program in practice for FYS assignment in Summer 2024 for students in Class of 2028.
- Broaden the impact of this research to other academic institutions.
- Try alternative optimization models to implement the same feature such as hierarchical and blended multi-criteria optimization models.

## Approaches 
1. Blended Optimization Model
2. Hierarchical Optimization Model

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

## Pipeline
![Pipeline](https://github.com/JuheonChu/DickinsonFYSAssignment/assets/35699839/ef5ab142-c29a-4a5c-bf0b-36cab80a643e)

## Program Functionality
  
  - `run.py`: This assigns Dickinson first-year students into 40+ seminar courses aiming to balance gender and student-type ratios while maintaining the course capacities. Among many versions of running this program, run.py specifically describes the program that shows the best performance in timely and efficient manner.
  - `parse.py`: This program parses the data that was provided by Dickinson College and generates the `DickinsonFirstYearSeminar.xlsx` file to be loaded for `run.py`.
  - `seminar_frequency.py`: This program provides the frequency distribution of the seminars. 
 


