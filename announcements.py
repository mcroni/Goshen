from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from mat.list import OneLineListItem
from kivy.properties import ObjectProperty



from models import *
#from models_sql import *




session = Session()





class Announcements(Screen,FloatLayout):
    ml = ObjectProperty(None)
    scroller = ObjectProperty(None)
    def load_announcements(self):
        for message in session.query(Announcementss.message):
            self.ids.ml.add_widget(OneLineListItem(text=str(message)))
