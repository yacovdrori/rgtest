# rgtest
This is consisted of 2 main modules
* ui
* serial broker

## requirments
asyncio
PySimpleGUI
serial_asyncio

To emulate ttyUSB0 on linux I use [socat](https://snoopysecurity.github.io/network-security/2018/03/21/introduction_to_socat.html)
install

```
sudo socat -d -d -v pty,rawer,echo=0,link=/dev/ttyS1 pty,rawer,echo=0,link=/dev/ttyUSB0 

```

Run with 

```
sudo python start.py

```

**Problems:**
1. didn't test incoming signals from Uart
2. send to UART somtimes get stuck until window is closed
