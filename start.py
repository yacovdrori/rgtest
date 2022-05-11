#
# Acquires data from micro:bit using serial IO
# Author: Lisa Ong, NUS/ISS
#

# import helper classes for acquiring data from the Micro:bit

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

# async def main(mysg):
    # await reader()
    # writer = await writer()

loop = get_event_loop()
loop.create_task(writer(mysg))
loop.create_task(reader(mysg))
loop.run_forever()

# serial4.run_loop_forever(comport, baudrate, SerialIoBase_Factory)