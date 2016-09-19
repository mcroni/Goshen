from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from mat.list import MDList
from mat.grid import SmartTile,SmartTileWithLabel
from mat.button import MDFloatingActionButton
import threading
from mat.list import OneLineListItem,OneLineAvatarListItem
from kivy.app import App
from kivy.core.audio import SoundLoader

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import mat.snackbar as Snackbar
from kivy.uix.image import AsyncImage
from mat.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
#convert this into python2 format before building
from kivy.network.urlrequest import UrlRequest

import _thread


from kivy.clock import Clock
Clock.max_iteration = 20



import urllib.request as opener


# i did this to prevent the app from crashing when looping through the images

""" chale release this lines when ready to deploy
this will activate the share intent in android"""
from jnius import autoclass
PythonActivity = autoclass('org.renpy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
String = autoclass('java.lang.String')


class AudioButton(OneLineAvatarListItem):
    def __init__(self,**kwargs):
        super(AudioButton,self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print(str(self.text))
            a = DownPopup(title=str(self.text))
            a.open()

        super(AudioButton, self).on_touch_down(touch)



class DownPopup(Popup):
    def __init__(self,**kwargs):
        super(DownPopup,self).__init__(**kwargs)
        self.source = 'http://goshen.heliohost.org/sermons/{}'.format(str(self.title))


    def play(self):
        sound = SoundLoader.load(self.source)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
            if self.ids.play_stop.text =='Play':
                self.ids.play_stop.text="Stop"
            else:
                self.ids.play_stop.text="Play"
                print(sound.state)
                sound.unload()
                sound.stop()
                print(sound.state)
                print('stopping')


    def download(self):
        import webbrowser
        webbrowser.open(self.source)
        print(self.source)


    def share(self):
        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_TEXT, String('{}'.format(self.source)))
        intent.setType('text/plain')
        chooser = Intent.createChooser(intent, String('Share...'))
        PythonActivity.mActivity.startActivity(chooser)


import time
class Sermons(Screen):
    scroller = ObjectProperty(None)
    grid = ObjectProperty(None)
    passed = []
    link = 'http://point3hub.com/mcroni/sermons/'
    def __init__(self, **kwargs):
        super(Sermons, self).__init__(**kwargs)

    def load(self):
        _thread.start_new_thread(self.list_files, ('name',))
        self.ids.search_input.bind(text=self.some_func)

    def list_files(self,name):
        print('display thread')
        self.ids.grid.clear_widgets()

        self.ids.spinner.active = True
        from ftplib import FTP
        ftp = FTP('ftp.goshen.heliohost.org')
        ftp.login(user='mcroni', passwd='paloma')
        print('connected t2')
        ftp.cwd('/public_html/sermons/')
        print('changed t2')
        print(name)
        try:
            self.files = ftp.nlst()
        except ftplib.error_perm:
            if str(resp) == "550 No files found":
                print("No files in this directory")
            else:
                raise
        tests = ['.mp3','.MP3']

        for f in self.files:
            if f[-4:] in tests:
                self.passed.append(f)

        for track in self.passed:
            src = 'ftp://mcroni:paloma@ftp.goshen.heliohost.org/public_html/sermons/{}'.format(track)
            title = src[65:]
            album = AudioButton(text=title)
            self.ids.grid.add_widget(album)
        self.ids.spinner.active = False




    def some_func(self, *args):
        returned_name = self.ids.search_input.text
        self.ids.grid.clear_widgets()
        for track in self.passed:
            if track.startswith(returned_name):
                self.album = AudioButton(text=str(track))
                self.album.add_widget(Photo(source='tower.png'))

                self.ids.grid.add_widget(self.album)
        print(len(self.ids.grid.children))
        if len(self.ids.grid.children) == 0:
            self.show_example_snackbar('simple')

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Sorry Sermon Not Found :-(", duration=1)


class Photo(ILeftBody, AsyncImage):
    pass
