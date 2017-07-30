import csv
from decimal import *

def mean(data_set):
    return Decimal(sum(data_set)) / len(data_set)

def variance(data_set):
    mean_res = mean(data_set)
    differences = []
    squared_res = []
    for elem in data_set:
        differences.append(elem - mean_res)
    for elem in differences:
        squared_res.append(elem ** 2)
    return mean(squared_res)
    
def standard_deviation(data_set):
    variance_res = variance(data_set)
    return variance_res ** Decimal('0.5')
    
if __name__ == "__main__":
    with open("dog_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        height_data = []
        headers = csv_file.next()
        print headers
        for row in csv_reader:
            height_data.append(int(row[1]))
        print "Mean: {}".format(mean(height_data))
        print "Variance: {}".format(variance(height_data))
        print "Standard Deviation: {}".format(standard_deviation(height_data))