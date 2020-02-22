import pdb
import logging

# IPython session starts up logging so basicConfig doesn't work. Here is the setup that works for me


# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20, backupCount=5)
 
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler = logging.FileHandler(filename='C:\\PYTHONDATASCIENCE\\loggingexample.log', mode='a')
fhandler.setFormatter(formatter)
fhandler.setLevel(level=logging.DEBUG)

logger.addHandler(fhandler)
logger.info('is when this event was logged.')


alist = ['a', 'b', 'c', 'd', 'e', 'f']

try:
    alist.remove("1")
except Exception as ex:
    print(type(ex))
    template = "An exception of type {0} occurred {1}"
    type(ex)
    message = template.format(ex, type(ex))
    
    logger.info(message)
    logger.warning(message)

else:
    print(alist)
finally:
    print("We are done")
