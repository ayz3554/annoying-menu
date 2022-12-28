# imports:
from tkinter import *

import pyautogui
import time
import schedule


def mass_ping_dc():

    def discord_ping():
        discordID = inputDiscordID.get()
        fullDiscordID = '<@' + discordID + '>'

        dcInterval = 1

        try:
            dcInterval = int(inputTime.get())
        except ValueError:
            pass

        whatTimeDCSchedule = str(inputWhatTime.get())

        def dc_task():
            while True:
                pyautogui.typewrite(fullDiscordID)
                pyautogui.press('enter')
                time.sleep(dcInterval)

        schedule.every().day.at(whatTimeDCSchedule).do(dc_task())


    # create massPingDC window
    massPingDCWindow = Tk()

    massPingDCWindow.title('Discord Mass-Ping by ayz')
    massPingDCWindow.geometry('256x144')
    massPingDCWindow.configure(bg='#29333E')



    # code:
    inputDiscordID = Entry(
        massPingDCWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputDiscordID.insert(0, 'Type nickname')
    inputDiscordID.pack()

    inputTime = Entry(
        massPingDCWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputTime.insert(0, 'Type every how many seconds')
    inputTime.pack()

    inputWhatTime = Entry(
        massPingDCWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputWhatTime.insert(0, 'Type what time')
    inputWhatTime.pack()

    discordPingButton = Button(
        massPingDCWindow,
        text='Start pinging',
        command=discord_ping,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )

    discordPingButton.pack()

    massPingDCWindow.mainloop()



def mass_ping_msg():

    def messenger_ping():
        messengerID = '@' + inputMessengerID.get()

        msgInterval = 1

        try:
            msgInterval = int(inputMSGTime.get())
        except ValueError:
            pass

        whatTimeMSGSchedule = str(inputMSGWhatTime.get())

        def msg_task():
            while True:
                pyautogui.typewrite(messengerID)

                pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(msgInterval)

        schedule.every().day.at(whatTimeMSGSchedule).do(msg_task())


    massPingMSGWindow = Tk()

    massPingMSGWindow.title('Messenger Mass-Ping by ayz')
    massPingMSGWindow.geometry('256x144')
    massPingMSGWindow.configure(bg='#29333E')

    inputMessengerID = Entry(
        massPingMSGWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputMessengerID.insert(0, 'Type nickname')
    inputMessengerID.pack()

    inputMSGTime = Entry(
        massPingMSGWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputMSGTime.insert(0, 'Type every how many seconds')
    inputMSGTime.pack()

    inputMSGWhatTime = Entry(
        massPingMSGWindow,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )
    inputMSGWhatTime.insert(0, 'Type what time')
    inputMSGWhatTime.pack()

    messengerPingButton = Button(
        massPingMSGWindow,
        text='Start pinging',
        command=messenger_ping,
        bg='#D0D3D4',
        font=('Cascadia Code', 10)
    )

    messengerPingButton.pack()


    massPingMSGWindow.mainloop()


if __name__ == '__main__':
    # main window:
    annoyingMenu = Tk()

    # create annoyingMenu window
    annoyingMenu.title('Annoying Menu by ayz')
    annoyingMenu.geometry('640x360')
    annoyingMenu.configure(bg='#29333E')
    annoyingMenu.eval('tk::PlaceWindow . center')

    # programs:
    massPingDC = Button(
        annoyingMenu,
        text='Discord Mass-Ping',
        command=mass_ping_dc,
        bg='#D0D3D4',
        font=('Cascadia Code', 12)
    )

    massPingMsg = Button(
        annoyingMenu,
        text='Messenger Mass-Ping',
        command=mass_ping_msg,
        bg='#D0D3D4',
        font=('Cascadia Code', 12)
    )

    massPingDC.place(relx=0.5, rely=0.43, anchor=CENTER)
    massPingMsg.place(relx=0.5, rely=0.57, anchor=CENTER)

    # mainloop
    annoyingMenu.mainloop()
