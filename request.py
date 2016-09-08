from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen



from models import *
#from models_sql import *



session = Session()

#from plyer import call
#from plyer.platforms.android.notification import AndroidNotification


class Requests(Screen):
    name = ObjectProperty(None)
    prayer = ObjectProperty(None)

    def add_request(self):
        add_request = PrayerRequest(name=self.ids.name.text, prayer_request=self.ids.prayer.text)
        session.add(add_request)
        session.commit()
        print('done committing')
        self.send_notify()

    def send_notify(self):
        print('sent')
        # notiff=  AndroidNotification()
        # notiff.notify(title="Sending Requests",message='Sending Request',timeout=.2)


