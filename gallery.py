from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from mat.list import MDList
from mat.grid import SmartTile,SmartTileWithLabel
from mat.button import MDFloatingActionButton
import threading
from kivy.app import App







#convert this into python2 format before building
import urllib.request
import _thread


from kivy.clock import Clock
Clock.max_iteration = 15
# i did this to prevent the app from crashing when looping through the images



class Gallery(Screen,):
    scroller = ObjectProperty(None)
    grid = ObjectProperty(None)
    passed = []
    def __init__(self,**kwargs):
        super(Gallery,self).__init__(**kwargs)


    def load(self):
        _thread.start_new_thread(self.list_files,('name',))

    def list_files(self,name):
        print('display thread')
        self.ids.grid.clear_widgets()

        self.ids.spinner.active = True
        from ftplib import FTP
        ftp = FTP('ftp.goshen.heliohost.org')
        ftp.login(user='mcroni', passwd='paloma')
        print('connected t2')
        ftp.cwd('/public_html/albums/%s' % 'menz')
        print('changed t2')
        print(name)
        try:
            self.files = ftp.nlst()
        except ftplib.error_perm:
            if str(resp) == "550 No files found":
                print("No files in this directory")
            else:
                raise
        tests = ['.jpg']

        for f in self.files:
            if f[-4:] in tests:
                self.passed.append(f)

        #print(self.passed)
        for photo in self.passed:
            src = 'ftp://mcroni:paloma@ftp.goshen.heliohost.org/public_html/albums/menz/{}'.format(photo)
            #print(src)
            album = SmartTileWithLabel(source=src, )
            self.ids.grid.add_widget(album)
        self.ids.spinner.active = False
