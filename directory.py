from kivy.metrics import dp
from kivy.properties import ObjectProperty
from mat.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from mat.list import MDList
from mat.list import TwoLineListItem, OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen


#from plyer import call
#from plyer.platforms.android.notification import AndroidNotification



#from models import *
from models_sql import *


session = Session()





class CallerButton(TwoLineListItem):
    def __init__(self,**kwargs):
        super(CallerButton,self).__init__(**kwargs)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            template = '+233'
            print(template+self.secondary_text)
            number = template+self.secondary_text
            print('calling')
            print(number)
            tel = number
            print(tel)
            call.makecall(tel=tel)



class Directory(Screen,FloatLayout):
    ml = ObjectProperty(None)
    scroller = ObjectProperty(None)
    button = ObjectProperty(None)
    def load_contacts(self):
        for name,number in session.query(Person.name,Person.number):
            self.ids.ml.remove_widget(self.button)
            self.ids.ml.add_widget(CallerButton(text=str(name),secondary_text=str(number)))




