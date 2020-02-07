class MessageReader(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
      
    def __enter__(self): 
        self.file = open(self.file_name, 'r') 
        return self.file
  
    def __exit__(self, exception_type, exception_value, traceback): 
        self.file.close() 
  
  

with open("school_prompt2.txt", 'r') as fileref:
     line = fileref.readline()
     num_char = 0
     while (line != ''):
         print(line)
         num_char += len(line)
         print(num_char)
         line = fileref.readline()
		 