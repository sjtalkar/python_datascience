import math

def findMean(inList):
    total_items = len(inList)
    if total_items == 0:
        return 0

    sum_items = 0
    for item in inList:
        sum_items = sum_items+item
    
    return sum_items/total_items

def findStandardDev(inList, mean):
    total_items = len(inList)
    if total_items == 1:
        return 0

    sum_square_diffs = 0
    for item in inList:
        sum_square_diffs = sum_square_diffs + pow((item - mean), 2)
    
    return pow(sum_square_diffs/(total_items-1), .5)

def createZFactorList (inList, mean, standard_deviation):
    if standard_deviation == 0:
        return 0
    z_factor_list = []
    for item in inList:
         z_factor_list.append((item - mean)/standard_deviation)
    return z_factor_list

def computeCorelationCoefficient (x_z_factor_list, y_z_factor_list):
    num_elements = len(x_z_factor_list)
    if num_elements == 1:
        return 0
    sum_zfactor_mult = 0
    for item in range(num_elements):
          print ("Multiplying {} and {} gives {}".format(x_z_factor_list[item],
                                                       y_z_factor_list[item], x_z_factor_list[item] * y_z_factor_list[item]))
          sum_zfactor_mult = sum_zfactor_mult + (x_z_factor_list[item] * y_z_factor_list[item])
            
    return sum_zfactor_mult/(num_elements-1)


inputTuple = ((1,1), (2,2), (2,3), (3,6))
x_list = []
y_list = []

#print(type(x_list))
#help(list)
for item in inputTuple:
     x_list.append(item[0])
     y_list.append(item[1])
    
  

x_mean = findMean(x_list)
y_mean = findMean(y_list)
print ("Mean of x is {} and mean of y is {}".format(x_mean, y_mean))  

  

x_standard_dev = findStandardDev(x_list, x_mean)
y_standard_dev = findStandardDev(y_list, y_mean)
print (x_standard_dev, y_standard_dev)  
print ("Standard Deviation  of x is {} and standard deviation of y is {}".format(x_standard_dev, y_standard_dev)) 

x_z_factor_list = createZFactorList(x_list, x_mean, x_standard_dev)
y_z_factor_list = createZFactorList(y_list, y_mean, y_standard_dev)

print ("Z factor list for x is {} and Z factor list for y is {}".format(x_z_factor_list, y_z_factor_list)) 

print ("Corelation coefficient is {}".format(computeCorelationCoefficient (x_z_factor_list, y_z_factor_list)))
    
    