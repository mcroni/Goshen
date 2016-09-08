from kivy.metrics import dp
from kivy.properties import ObjectProperty
from mat.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from mat.list import MDList
from mat.list import TwoLineListItem, OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import mat.snackbar as Snackbar
from kivy.app import App



from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView



from models import *
#from models_sql import *
session = Session()


class Pastors(Screen, FloatLayout):
    pas_text_field = ObjectProperty(None)
    name_text_field = ObjectProperty(None)

    def login(self):
        names = []
        passwords = []
        for name, password in session.query(PastorsCircle.name, PastorsCircle.password):
            names.append(name)
            passwords.append(password)
    #chale find a better to tally the username with the password, i dont like this
        if self.name_text_field.text in names and self.pas_text_field.text in passwords:
            print("yes i dey")
            self.name_text_field.text = ''
            self.pas_text_field.text = ''
            # oh i see,so i can use this trick to move to another screen, hmmmmmmmm kivy

            App.get_running_app().change_screen('requests_reader')

        else:
            self.show_example_snackbar('simple')
            self.name_text_field.text = ''
            self.pas_text_field.text = ''


    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Wrong Credentials!")





class RequestsReader(Screen):
    def load_requests(self):
        content = ScrollView()
        mdlist = MDList()
        content.add_widget(mdlist)
        title = "Prayer Requests"
        pop = Popup(title=title,content=content)
        pop.open()
        for name, prayer_request in session.query(PrayerRequest.name, PrayerRequest.prayer_request):
            mdlist.add_widget(TwoLineListItem(text=str(name), secondary_text=str(prayer_request)))


    def add_announce(self):
        pop = Announce()
        pop.open()





class Announce(Popup):
    message = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Announce, self).__init__(**kwargs)

    def add_announce(self):
        if len(self.message.text) == 0:
            self.show_example_snackbar('simple')

        else:
            add_announce = Announcementss(message=self.ids.message.text)
            session.add(add_announce)
            session.commit()
            print('added announcement')
            self.ids.message.text = ''
            self.dismiss()
            self.show_example_snackbar('sent')

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Please key in Something")
        elif snack_type == 'sent':
            Snackbar.make("Announcement Sent")
