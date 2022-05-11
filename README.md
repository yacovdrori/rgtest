# rgtest
This is consisted of 2 main modules
* ui
* serial broker

## requirments
asyncio
PySimpleGUI
serial_asyncio

To emulate ttyUSB0 on linux I use socut
install

'''
sudo socat -d -d -v pty,rawer,echo=0,link=/dev/ttyS1 pty,rawer,echo=0,link=/dev/ttyUSB0 
'''

Run with 
'''
sudo python start.py
'''
