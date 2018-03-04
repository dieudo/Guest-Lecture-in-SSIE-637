# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:35:50 2016

@author: dieudonneouedraogo
"""
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv('Visualization637.2.csv')
print df
fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
#Create one or more subplots using add_subplot, because you can't create blank figure
ax = fig.add_subplot(1,1,1)
#Variable
ax.hist(df['Age'],bins = 2) # Here you can play with number of bins
#Labels and Tit
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Patient')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
#Variable
ax.boxplot(df['Age'])
plt.show()
#
#df['COST']
import seaborn as sns 
sns.violinplot(df['Age'], df['Gender']) #Variable Plot
sns.despine()
var = df.groupby('Gender').Cost.sum() #grouped sum of cost at Gender level
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('total Cost')
ax1.set_title("Gender wise total Cost")
var.plot(kind='bar')
var = df.groupby('Body').Cost.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Body')
ax1.set_ylabel('Total Cost')
ax1.set_title("Body wise total Cost")
var.plot(kind='line')
var = df.groupby(['Body','Gender']).Cost.sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue'], grid=False)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['Age'],df['Cost']) #You can also add more variables here to represent color and size.
plt.show()
var=df.groupby(['Gender']).sum().stack()
temp=var.unstack()
type(temp)
x_list = temp['Cost']
label_list = temp.index
plt.axis("equal") #The pie chart is oval by default. To make it a circle use pyplot.axis("equal")
#To show the percentage of each pie slice, pass an output format to the autopctparameter 
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") 
plt.title("Cost distribution")
plt.show()

import numpy as np
#Generate a random number, you can refer your data values also
data = np.random.rand(4,2)
rows = list('1234') #rows categories
columns = list('MF') #column categories
fig,ax=plt.subplots()
#Advance color controls
ax.pcolor(data,cmap=plt.cm.Reds,edgecolors='k')
ax.set_xticks(np.arange(0,2)+0.5)
ax.set_yticks(np.arange(0,4)+0.5)
# Here we position the tick labels for x and y axis
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
#Values against each labels
ax.set_xticklabels(columns,minor=False,fontsize=20)
ax.set_yticklabels(rows,minor=False,fontsize=20)
plt.show()

