import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont

# read image and convert to RGB
try:
    image=Image.open("readonly/msi_recruitment.gif")
except:
    print("This file readonly/msi_recruitment.gif cannot be found")
#Highly important for manipulations that the image is to be in RGB
image=image.convert('RGB')

def change_rgb(new_image, channel, intensity):
    width, height = new_image.size 
    mult_red = 1
    mult_green = 1
    mult_blue = 1
    if channel == 0:
       mult_red =  intensity
    elif channel == 1:
       mult_green =  intensity
    else:
       mult_blue =  intensity
    print(" Multipliers are {} {} {} and intensity = {} ".format(mult_red, mult_green, mult_blue, intensity) )
    #The image has to be RGB for getpixel and putpixel to work 
    for x in range(width):
        for y in range(height):
            red, green, blue = new_image.getpixel((x, y))
            new_image.putpixel((x, y), (int(red * mult_red), int(green * mult_green), int(blue * mult_blue), 255) )
    return new_image
    
#Load a font
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
                         
text = "channel: 0 intensity: 0.1"
width_text,height_text = font.getsize(text)
 
#Replace the width by the width of the picture image
width_text = image.width
print("Width of text : {} Height of text: {}".format(width_text, height_text))

# build a list of 9 images which have different channel and intensity
images=[]
channel_num = 0
intensity = 0.1
for i in range(3):
  for j in range(3):
         new_image = image.copy()
         images.append(change_rgb(new_image, channel_num, intensity))
         #display(new_image)
         intensity = intensity + 0.4
  intensity = 0.1
  channel_num = channel_num + 1

#print("Length of images : {}".format(len(images)))    

#create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+height_text*3))
draw = ImageDraw.Draw(contact_sheet)
#print(type(draw))


##############################################################################################################
#Capture the width and height of the contact sheet
width_contact_sheet, height_contact_sheet = contact_sheet.size
#print(width_contact_sheet, height_contact_sheet)
                         
#Set the co-ordinates of the first text image
x, y = (0, image.height)
channel_num = 0
intensity = 0.1
for i in range(3):
    for j in range(3):
        #draw white text on black background
        #print("Rectangle drawn at x= {}, y= {}, bottom_right X = {} bottom_right height = {}".format(x, y, x+ image.width,y+height_text))
        text = "channel: "+ str(channel_num) + "intensity: " + str(intensity)
        draw.rectangle(((x, y), (x+image.width, y+height_text)), fill='black')
        draw.text((x, y), text, fill='white', font=font)
        x = x + image.width
        intensity = intensity + 0.4
        #print("updated x= {}, intensity = {}".format(x, intensity))
    x=0
    y = y + height_text + image.height
    intensity = 0.1
    channel_num = channel_num + 1
    #print("updated y= {}, intensity = {} channel_num = {}".format(x, intensity, channel_num)) 

##############################################################################################################

x=0
y=0
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height + height_text
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
