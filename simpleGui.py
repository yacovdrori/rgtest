
import PySimpleGUI as sg
import asyncio

class mygui():
    def __init__(self, writer):
        self.writer = writer
        self.window = None
        self.speed = 0

    def writeSpeed(self, speed):
        self.window('SPEED').update(speed)
        self.speed = speed

    def startWindow(self):
        sg.theme('DarkAmber')
        layout = [
                [sg.T("speed"), sg.Text(self.speed,key='SPEED')],
                [sg.Button("Click",enable_events=True)],
                [sg.Button("incspeed")]]
    
        # Create the window
        self.window = sg.Window('Rogat test', layout,
                       use_default_focus=True,
                       finalize=True,
                       margins=(10,10),
                       element_padding=(10,10),
                       border_depth=0)
        # Create an event loop
        while True:
            event, values = self.window.read()
            # End program if user closes window or
            # presses the OK button
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == "Click":
                self.writer.write(b'click')
                self.window.close()
                self.startWindow()
            if event == "incspeed":
                self.speed = self.speed +1
                self.window.close()
                self.startWindow()
                # break
        