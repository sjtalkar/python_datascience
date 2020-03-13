# Use CTRL + forward slash to block comment in Jupyter

''' Program to rename files that are currently sorted alphabetically, so that the number of the file appears before any string'''

import os

print (os.getcwd())

#C:\WINDOWS\system32
os.chdir('C:\PYTHONDATASCIENCE')

print (os.getcwd())
#C:\PYTHONDATASCIENCE

print(os.listdir())

# Create the fils that will be renamed These are currently sorted in the lsiting by nae of Animal

with open('Zebra-Zoo Animals-#2.txt', 'w') as fileRef:
    fileRef.write('Test File for sorting by number')
    
with open('Monkey-Zoo Animals-#1.txt', 'w') as fileRef:
    fileRef.write('Test File for sorting by number')

with open('Aardvak-Zoo Animals-#3.txt', 'w') as fileRef:
    fileRef.write('Test File for sorting by number')    
        

with open('Giraffe-Zoo Animals-#4.txt', 'w') as fileRef:
    fileRef.write('Test File for sorting by number')    
        

# with open('Giraffe-Zoo Animals-#4.txt', 'r') as fileRef:
#     print(fileRef.read())

#help(str)

filesToRename = [fileName for fileName in os.listdir() if fileName.find('Zoo Animals') > 0 ]
print(filesToRename)

  
#     print(animalName.strip())
#     print(residence.strip())
#     print(fileNumber.strip())
for oneName in filesToRename:
    oneName = oneName.split('.')[0]
    #print(oneName)
    animalName, residence, fileNumber = oneName.split('-')
    
    reorderName = fileNumber[1:].strip() + '-'+ animalName.strip() + '-'+ residence.strip() + '.txt'
    print(oneName, reorderName)
    os.rename(oneName+'.txt', reorderName)    
	