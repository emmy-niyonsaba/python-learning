
import pandas as panda

StudentRecord={
'names':['alice','bob','charlie','cyiza','manzi'],
'age': [18,24,55,45,44],
'gender':['F','m','F','M','M'],
'marks': [78,67,81,65,72]
}

studentDF= panda.DataFrame(StudentRecord)
#print("The Student record :",studentDF)

# you print the only one clumun for the DataFrame 
# By example here we can now get only age or marks for record 

print("Age colmun for DF",studentDF['age'])

studentDF.to_csv("student.csv",index=False)
studentDF.to_csv("student.xlsx",index=False)