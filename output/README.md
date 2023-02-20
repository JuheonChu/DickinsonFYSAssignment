
# original.py 
This file directly translated the mosel assignment program developed by Dr. Forrester, Richard.

## Result
![Seminar Assignment Result 1](https://user-images.githubusercontent.com/35699839/220000410-2ee54bc8-36ae-44cb-bf47-2eaaace8fdfe.png)
![Seminar Assignment Result 2](https://user-images.githubusercontent.com/35699839/220000425-c81d2362-6dbc-4bd4-9c0a-b3f8faa559d7.png)

# nonlinearized_objectives.py
This file improved the `original.py` by successfully normalizing the scale of each objective function. This was accomplished by computing nadir points for each objectives successfully.

## Result
![Result 1](https://user-images.githubusercontent.com/35699839/220000475-24b93f6c-0d44-4ae9-8f1e-032a62db668a.png)
![Result 2](https://user-images.githubusercontent.com/35699839/220000485-7d90d7e8-3457-421d-8657-fb7f54ae9f45.png)
![Result 3](https://user-images.githubusercontent.com/35699839/220000501-db5b7437-d916-4fb6-9408-b8b24134ea56.png)

# linearized_objectives.py
This file improved the runtime of `nonlinearized_objectives.py` by linearizing the nonlinear gender and citizenship objectives. The program runtime now improved from 5+ minutes to 1 second.

## Result
![Assignment result 1](https://user-images.githubusercontent.com/35699839/220000578-683d6b01-b00d-43ed-95ee-c10cfd0ab53c.png)
![Assignment result 2](https://user-images.githubusercontent.com/35699839/220000591-4b786c21-53a5-4075-b564-431a890e6ff9.png)
![Assignment result 3](https://user-images.githubusercontent.com/35699839/220000628-aa0adf6b-9ed4-4641-b365-cfe803bb60fc.png)
