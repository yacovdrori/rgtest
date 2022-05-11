#
# Author: Yacov Drori
#


import PySimpleGUI as sg
import simpleGui
import asyncio
from asyncio import get_event_loop
from serial_asyncio import open_serial_connection

mysg = None
async def writer(mysg):
    _, writer = await open_serial_connection(url='/dev/ttyUSB0', baudrate=115200)
    mysg = simpleGui.mygui(writer)
    mysg.startWindow()

    return writer

async def reader(mysg):
    reader, _ = await open_serial_connection(url='/dev/ttyUSB0', baudrate=115200)
    while True:
        line = await reader.readline()
        mysg.writeSpeed(str(line, 'utf-8'))
        print(str(line, 'utf-8'))


loop = get_event_loop()
loop.create_task(writer(mysg))
loop.create_task(reader(mysg))
loop.run_forever()

