from microbit import *
image1 = Image("09099:"
               "09099:"
               "09099:"
               "09099:"
               "90900:")

image2 = Image("09099:"
               "90900:"
               "09099:"
               "90900:"
               "90900:")

image3 = Image("90900:"
               "09099:"
               "90900:"
               "09099:"
               "90900:")

image4 = Image("90900:"
               "90900:"
               "90900:"
               "90900:"
               "90900:")

image5 = Image("99999:"
               "99999:"
               "99999:"
               "99999:"
               "00000:")

image6 = Image("99999:"
)
while True:
    if pin0.is_touched():
        if pin1.is_touched():
            if pin2.is_touched():
                display.show(image1)
            else:
                display.show(image2)
        else:
            if pin2.is_touched():
                display.show(image3)
            else:
                display.show(image4)
    else:
        if pin1.is_touched():
            if pin2.is_touched():
                display.show(image5)
            else:
                display.show(image6)
        else:
            if pin2.is_touched():
                display.show(image7)
            else:
                display.show(image8)