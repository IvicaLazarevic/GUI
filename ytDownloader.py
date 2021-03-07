#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'ytDownloader.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call
from tkinter import *
from tkinter import messagebox

try:
    from pytube import YouTube
    from pytube import Playlist
    from pytube.cli import on_progress
    from colorama import Fore
except:
    call('pip3 install colorama pytube', shell=True)
    exit()


def logo():
    print(Fore.RED+"\n       __           __        ____      __        ")
    print(Fore.RED+"  ____/ /___ ______/ /_______/ __ \____/ /__  _____ ")
    print(Fore.RED+" / __  / __ `/ ___/ //_/ ___/ / / / __  / _ \/ ___/ ")
    print(Fore.RED+"/ /_/ / /_/ / /  / ,< / /__/ /_/ / /_/ /  __/ /     ")
    print(Fore.RED+"\__,_/\__,_/_/  /_/|_|\___/\____/\__,_/\___/_/      ")
    print(Fore.RED+"                                                \n")
    print(Fore.RED+'                               Naziv: '+ __scriptName__)
    print(Fore.RED+'                               Verzija: '+ __version__)
    print(Fore.RED+'                               Koder: '+ __coder__)
    print(Fore.RED+ '                               Sajt: ' + __site__+Fore.WHITE)

if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()

def yTVideo():
    YouTube(LINK.get(), on_progress_callback=on_progress).streams.first().download()
    messagebox.showinfo('Youtube Downloader', 'Uspesno skinut video fajl!')

def yTAudio():
    YouTube(LINK.get(), on_progress_callback=on_progress).streams.get_by_itag(140).download()
    messagebox.showinfo('Youtube Downloader', 'Uspesno skinut .mp4 fajl!')

if __name__ == '__main__':
    print('\n[+] Dobrodosli u ytDownloader.py GUI verziju\n')

    PROZOR = Tk()
    PROZOR.geometry('700x400')
    PROZOR.minsize(width=700, height=400)
    PROZOR.maxsize(width=700, height=400)
    PROZOR.title(f'YouTube downloader v.{__version__}')

    Label(PROZOR, text='Dobrodosli u Youtube Downloader', font='roman 20 bold').pack(pady=10)
    Label(PROZOR, text='Molimo vas unesite link ispod', font='normal 10').pack(pady=5)

    TEKST = StringVar()
    LINK = StringVar()

    Entry(PROZOR, textvariable=LINK, width=100).pack(pady=20)

    Button(PROZOR, text='Skini Video', width=30, command=yTVideo).pack()
    Button(PROZOR, text='Skini mp4', width=30, command=yTAudio).pack(pady=10)
    pbytes = Label(PROZOR, text='pythonbytes.rs', font='normal 10')
    pbytes.place(relx = 0.0, rely= 1.0, anchor='sw')

    PROZOR.mainloop()