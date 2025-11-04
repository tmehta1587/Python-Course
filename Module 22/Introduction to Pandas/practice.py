import pandas as pd

data_set = {'subjects': ['English', 'Maths', 'Science', 'Business', 'Psychology', 'Economics'],
            'name': ['Bob', 'Sam', 'Tom', 'Ace', 'Jim', 'Anne'],
            'score': [6, 5, 7, 6, 4, 3]}

df = pd.DataFrame(data_set)
print("Student Data Set")
print(df)
