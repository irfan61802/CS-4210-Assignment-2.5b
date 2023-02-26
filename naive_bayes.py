#-------------------------------------------------------------------------
# AUTHOR: Irfan Iqbal
# FILENAME: naive_bayes.py
# SPECIFICATION: naive bayes classification program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

dbTraining = []
X = []
Y = []

#reading the training data in a csv file
#--> add your Python code here

with open("weather_training.csv", 'r') as csvfile:
     reader = csv.reader(csvfile)
     for i, row in enumerate(reader):
         if i > 0: #skipping the header
            dbTraining.append (row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here

for row in dbTraining:
    xRow=[]
    for i,x in enumerate(row):
        if i==0 or i==5: continue
        if x=="Sunny" or x=="Hot" or x=="High" or x=="Weak":
            xRow.append(1)
        elif x=="Rain" or x=="Cool":
            xRow.append(3)
        else:
            xRow.append(2)
    X.append(xRow)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here

for row in dbTraining:
    if row[-1]=="Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

dbTest=[]
#reading the test data in a csv file
#--> add your Python code here

with open("weather_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            del row[-1]
            dbTest.append(row)
X_test=[]
for row in dbTest:
    xRow=[]
    for i,x in enumerate(row):
        if i==0 or i==5: continue
        if x=="Sunny" or x=="Hot" or x=="High" or x=="Weak":
            xRow.append(1)
        elif x=="Rain" or x=="Cool":
            xRow.append(3)
        else:
            xRow.append(2)
    X_test.append(xRow)

#printing the header of the solution
#--> add your Python code here
print("Day Outlook Temperature Humidity Wind PlayTennis Confidence")

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here

for i in range(len(X_test)):
    prediction=clf.predict_proba([X_test[i]])[0]
    res=""
    if prediction[0]>prediction[1]:
        res="yes     "+str(round(prediction[0],2))
    else:
        res="no      "+str(round(prediction[1],2))
    print('{:<5s}{:<8s}{:^8s}{:^8s}{:^12s}{:>7s}'.format(dbTest[i][0],dbTest[i][1],dbTest[i][2],dbTest[i][3],dbTest[i][4],res))



