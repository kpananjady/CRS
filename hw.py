#file outline

#Purpose: To read in a file, plot the distribution of values and mark measures of central tendency.
#I'm working with a discrete distribution, which I know isn't ideal, but I wanted to finish the exercise to understand why.
#Data source: https://www.fema.gov/media-library/assets/documents/180273. This shows what rating communities that participate in the Community Rating System have achieved as of April last year. 


#Pseudocode
#Read in the file 
#Parse the file 
#Calculate quartile measures
#Calculate mean, standard deviation measures
#Plot everything

#import csv, matplotlib, stats and numpy libraries

#for percentaile, standard deviation and arange
import numpy as np 
#for viz 
import matplotlib.pyplot as plt
#this is for the mean calculations
import statistics 
#this is to open and read the file
import csv

#open the file w the csv library
csv_file = open("CRS_2019.csv")
#create the DictReader object to read it
csv_read = csv.DictReader(csv_file)

#create a list to store the ratings
total_ratings = []
#for each row of the dataset
for row in csv_read:
    #find column with the rating, convert to float and add to my empty list
    total_ratings += [float(row[csv_read.fieldnames[5]])]


#define the quartiles
my_quartiles = np.percentile(total_ratings, [25,50,75])
#define the interquartile range
my_iqr = my_quartiles[2] - my_quartiles[0]
#define the lower bound using interquartile range
upper = my_quartiles[2] + (1.5*my_iqr)
#define the lower bound using interquartile range
lower= my_quartiles[2] - (1.5*my_iqr)

#use the stats library to calculate the mean
my_mean = statistics.mean(total_ratings)
#use the stats library to calculate the standard deviation
my_std_dev = np.std(total_ratings)

#I'm just initializing the list bc the mean value appears twice below anyway?
mean_tendencies = []

#i goes from 0 to 3
for i in range(4):
    #lines on the right
    mean_tendencies+=[my_mean+(i*my_std_dev)]
    #lines on the left
    mean_tendencies+=[my_mean-(i*my_std_dev)]

#this is important for centering the ticks (given that it's a discrete disribution)
#here's where the code is from 
#np.arange produces numbers between 0 and 12 (you're going to have ticks from 0-12), and then you dock 0.5 off each number to center it in its bar
my_bins=np.arange(13)-0.5
#set you historgram's data, bins, color
my_hist = plt.hist(total_ratings,my_bins,histtype='bar',color='red')
#set which ticks to show
plt.xticks(range(13))
#set the length of the x axis
plt.xlim([0, 13])

#plot the quartile lines 
plt.vlines(my_quartiles, 0,30,color=['b','b','b'],linestyle='dashed')
#plot the upper and lower bound lines in the same color
plt.vlines([lower,upper],0,30,color=['b','b'],linestyle='dashed')
#plot the mean stuff in a different color
plt.vlines(mean_tendencies, 0,30,color=['g','g','g'],linestyle='dashed')

#show the plot! 
plt.show()

#print the measures to the terminal
print('The mean is', my_mean)
print('The standard deviation is', my_std_dev,'. I can see that this is not going to be that useful for my purposes.')
print('The 1st, 2nd and 3rd quartiles are', my_quartiles,'. This seems a lot more useful here.')
print('The interquartile range is',my_iqr)
print('My lower bound is', lower,', while my upper bound is', upper,'.')

#Next steps:
#There's something weird about no 4s! I don't know why there aren't any, and it makes me question whether the data is good. 