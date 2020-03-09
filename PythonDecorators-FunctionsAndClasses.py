def decorator_function(execFunction):
    def wrapper_function(*args, **kwargs):
        return execFunction(*args, **kwargs)
    return wrapper_function
    

    

@decorator_function
def display_info(name, age):
    print ('display function ran with arguments {} and {}'.format(name, age))
    
@decorator_function
def display():
    print ('display function ran')
      
    

display()

display_info('Simi', 50)

#the above syntax of decorator is same as

#display = decorator_function(d)

#display_info = decorator_function('Simi', 50)