import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result=[]
count=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print(mean)
print(std_deviation)
print(median)
print(mode)
first_std_dev_start, first_std_dev_end = mean-std_deviation, mean+std_deviation
sec_std_dev_start, sec_std_dev_end = mean-(2*std_deviation), mean+(2*std_deviation)
thi_std_dev_start, thi_std_dev_end = mean-(3*std_deviation), mean+(3*std_deviation)
list_of_data_within_1_std_deviation=[result for result in dice_result if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_deviation=[result for result in dice_result if result > sec_std_dev_start and result < sec_std_dev_end]
list_of_data_within_3_std_deviation=[result for result in dice_result if result > thi_std_dev_start and result < thi_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))