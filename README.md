![Dickinson logo](https://github.com/JuheonChu/DickinsonFYSAssignment/assets/35699839/e00c566f-da16-4820-8645-5ec63394964d)

## About this project
- Title: Improving Diversity and Preferred Assignment in Dickinson’s First-Year Seminar Selection Process Using Optimization Models
- Author: [John Chu](https://www.linkedin.com/in/juheonchu/), [Prof. Dick Forrester](https://www.dickinson.edu/dickforrester) 

### Background: 
Dickinson currently uses a process developed by Professor Dick Forrester and Dr. Thanh To (’11) to assign students to First-Year Seminars (FYS). This process utilizes a nonlinear multicriteria optimization model with the goal of assigning students to one of their top-ranked seminars while balancing the classes with regard to gender and the number of international students. In this study, we investigate alternative approaches aiming to improve the run-time and quality of the assignments. Specifically, we consider the linearization of the nonlinear objectives and the use of the hierarchical optimization model. These improvements resulted in a significant reduction in runtime and offer improved flexibility in adjusting assignment outcomes. The overarching aim of this study is to contribute robust optimization approaches that can be widely adopted across educational institutions.

## Acknowledgement
We want to convey our sincere gratitude to the [Gurobi](https://support.gurobi.com/hc/en-us) community for its providing invaluable resources. The comprehensive documentations and responsive Q&A support significantly facilitated the implementation of the enhancements we aforementioned. For those new to the platform, Gurobi offers an accessible and well-structured manual available [here](https://www.gurobi.com/documentation/10.0/refman/working_with_multiple_obje.html).

## Objective
- Improve the program efficiency and quality of the assignement of the existing program.
- The deployment of this computer program in practice for FYS assignment in Summer 2024 for students in Class of 2028.
- Generalize the assignment optimization models to other academic institutions.
- Undertake comparative analysis of the assignment qualities performed by those alternative optimization approaches.

## Approaches 
We performed a comparative analysis of assignment quality using the following optimization approaches. Each is aimed for a distinct purpose. [This documentation](https://www.gurobi.com/documentation/10.0/refman/working_with_multiple_obje.html) outlines the detailed explanation of those approaches including the exemplary implementations in GurobiPy. 
1. Blended Optimization Model
2. Hierarchical Optimization Model
3. Combining Blended and Hierarchical Objectives

## Prerequisite
 - Python
 - PyCharm/spyder/Python Idle
 - Gurobi solver

## How to set up Gurobi solver?

### 1. Download Install [Python Gurobi Solver](https://www.gurobi.com/downloads/gurobi-software/)

- Create your account [here](https://portal.gurobi.com/iam/login/).
- Choose the OS that supports your local machine and download the Gurobi Solver that corresponds to your system.
- Issue the Gurobi License ID. 
- Customize the Environment Settings by setting the System variables.

![environment setting](https://user-images.githubusercontent.com/35699839/201580110-9a733a25-05d4-4240-a7f1-f336c2e76b5a.png)

### 2. Python Install
- Follow the protocol denoted [here](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-).

## Project Workflow
![Pipeline](https://github.com/JuheonChu/DickinsonFYSAssignment/assets/35699839/a837f135-74ab-4f91-9207-68238480e0e8)


## Program Functionality
  
  - `run.py`: This assigns Dickinson first-year students into 40+ seminar courses aiming to balance gender and student-type ratios while maintaining the course capacities. Among many versions of running this program, run.py specifically describes the program that shows the best performance in timely and efficient manner.
  - `parse.py`: This program parses the data that was provided by Dickinson College and generates the `DickinsonFirstYearSeminar.xlsx` file to be loaded for `run.py`.
  - `seminar_frequency.py`: This program provides the frequency distribution of the seminars. 
 


