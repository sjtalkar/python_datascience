class MessageReader(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
      
    def __enter__(self): 
        self.file = open(self.file_name, 'r') 
        return self.file
  
    def __exit__(self, exception_type, exception_value, traceback): 
        self.file.close() 
  
class MessageWriter(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
      
    def __enter__(self): 
        self.file = open(self.file_name, 'w') 
        return self.file
  
    def __exit__(self, exception_type, exception_value, traceback): 
        self.file.close()   

line1='ID,Age,Gender,GenderGroup,Glasses,GlassesGroup,Height,Wingspan,CWDistance,Complete,CompleteGroup,Score'
line2='1,56,F,1,Y,1,62,61,79,Y,1,7'
line3='2,26,F,1,Y,1,62,60,70,Y,1,8'
with open('cartwheeldata.csv','w') as fileref:
    fileref.write('{}\n{}\n{}\n'.format(line1,line2,line3))

with MessageReader("cartwheeldata.csv") as fileref:
	for line in fileref:
		print(line)
    
 