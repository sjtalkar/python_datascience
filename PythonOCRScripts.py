import PIL
PIL.__version__
from PIL import Image
from PIL.Image import core as _imaging
#help(PIL)

# Python also has a function called dir() which will list the contents of an object. This is especially useful
# with modules where you might want to see what classes you might interact with. Lets list the details of 
# the PIL module

#dir(PIL)
#There is a class called Image

#help(Image)
#There is a method called open

#help(Image.open)

#Discovery trail on how to open an Image
import inspect

file="C:\PYTHONDATASCIENCE\PYDATASCIENCEOCR/msi_recruitment.gif"
image=Image.open(file)
print(image)

print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))
image.show()
#The above popped up the image on Picture application

# Instead, we want to render the image in the Jupyter notebook. It turns out Jupyter has a function
# which can help with this.
from IPython.display import display
display(image)