import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def SexSurvived(df):
    group = df.groupby(['Sex']).Survived.count()
    return group['male'], group['female']
def percentage(function, ti):
    male, female = function(ti)
    total = male + female
    return calculate(male, total), calculate(female, total)
def calculate(x, y):
    return round(((x / y) * 100), 3)

titanic = pd.read_csv('train.csv')
#print(percentage(titanic))
male, female = SexSurvived(titanic)
#
''' print(SexSurvived(titanic))
print(percentage(SexSurvived,titanic)) '''

#constructing the pie chart
def piechart(df, title):
    label = ['male['+ str(SexSurvived(df)[0])+']', 'female['+ str(SexSurvived(df)[1])+']']
    print(label)
    sex = list(percentage(SexSurvived,df))
    print(sex)
    patches, text = plt.pie(sex, colors=['blue','red'], startangle=90)
    plt.legend(patches, label, loc= 'best') 
    plt.title(title, fontsize=12, color='r')
    plt.axis('equal')
    plt.tight_layout()
    #plt.savefig('%s'%(name))
    plt.show()

piechart(titanic, 'Pie chart of women : men on board the titanic')


#working on the percentage of survived individuals
survived = titanic[titanic.Survived == 1]
print(survived.groupby('Sex').Survived.count())
piechart(survived, 'Pie chart of women : men ration that survived the titanic')


array = survived.groupby(['Pclass', survived.Sex == 'male']).Survived.count()
survivedClass = list(array[::-2])
print(survivedClass)

#printing barcharts
plt.xticks(survivedClass, ('class 3', 'class 2', 'class 1'))
plt.plot(survivedClass, '+', color='k')
plt.title('barchat example', color='r', fontsize='12')
plt.show()