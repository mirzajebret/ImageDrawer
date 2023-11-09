import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.config import Config
from kivy.clock import Clock
import random
import os

# Define the directory containing the images
image_folder = 'D:/Programming/aPPS/IMG_Drawer/img/'

# Get a list of all files in the directory
img_list = [f for f in os.listdir(image_folder) if f.endswith('.png')]

# Add the directory path to the file names
img_list = [os.path.join(image_folder, f) for f in img_list]


Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '250')
#img_list = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png',
 #           '12.png', '13.png', '14.png', '15.png', '16.png' '17.png', '18.png', '19.png', '20.png', '21.png',
  #          '22.png', '23.png', '24.png', '25.png']



run = True
counter = 0

class App(App):

    def build(self):
        self.img = Image()
        Clock.schedule_interval(self.update_image, 1)  # Schedule image update every 1 second
        return self.img

    def update_image(self, dt):
        self.img.source = random.choice(img_list)



App().run()
