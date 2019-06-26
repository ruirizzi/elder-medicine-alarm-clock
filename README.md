# Elder Medicine Alarm Clock
> A Python solution running on Raspberry Pi (Raspbian)

A Raspberry Pi-based solution to help elder people take their medicines at the right date & time.
## Why?
My mother-in-law is (was) having a hard time remembering her medicine's schedule and using a simple smartphone alarm-clock/schedules is not an option as she's not very fond of such devices.

I decided to create a quite simple Python application that runs on Raspberry Pi's Raspbian so I could use a simple 3.2 inches TFT LCD display as UI.

I'm also learning Python and wanted something to do with my newly learned language.

## Installing / Getting started

This small guide is aimed at configuring the same (or similar) environments as the one I used, so we have:
 - [Raspberry Pi 3 B board](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (probably works on other RPi boards too);
 - [Raspbian on a micro-SD](https://www.raspberrypi.org/downloads/raspbian/) (I used the Stretch with Desktop and recommended software);
 - [3.2 inches TFT LCD](https://www.waveshare.com/wiki/3.2inch_RPi_LCD_%28B%29) (will certainly work with other displays too);

After doing all that, you should be good to go and run PyQt5-based apps with `python3` (please note that Raspbian comes with both Python 2 and Python 3)

### Running PyQt5-based Apps on Raspbian

It's a bit tricky to run Python apps that use PyQt5 to create GUI, but after some work, I figured that you should (as of June 2019):

```bash
sudo apt-get install qt5-default
wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.17/sip-4.19.17.zip 
wget https://www.riverbankcomputing.com/static/Downloads/PyQt5/5.12.2/PyQt5_gpl-5.12.2.zip
tar -xzfv sip-4.19.17.zip (on your download directory)
tar -xzfv PyQt5_gpl-5.12.2.zip (on your download directory)
```
CD to `sip-4.19.17`folder:
```bash
python3 configure.py
make (this will take a shit-load of time)
```
CD to `PyQt5_gpl-5.12.2`folder:
```bash
python3 configure.py --sip \your-sip-dir-location\sip-4.19.17\sipgen\sip
make
```
After all theses steps you should be able to run the Python script with PyQt5 GUI.
### Setting up Dev Tools

I've developed the application and the UI on Windows 10 using [**Visual Studio Code**](https://code.visualstudio.com/) for IDE and **QT designer** as GUI designer. 

In order to develop on Windows, you must have Python 3 installed on your machine. 

- You can [download the installer](https://www.python.org/downloads/) and find instructions on the [official Python Software Foundation's page](https://www.python.org/). Make sure you allow the installer to add `python`to your `PATH`environment variable.

After installing Python 3 on your machine, you should be able to install the `PyQt5` and  `pyqt5-tools` (**QT designer** included) by running these on your `command prompt`:
```
C:\Users\YourName>python -m pip install PyQt5
C:\Users\YourName>python -m pip install pyqt5-tools
```
When all is done, you can go to `pyqt5-tools` folder inside your site packages folder (you can get where it is by `python -m site`) and find the **QT designer** executable.

In my case, the `site-package`folder user is at `C:\Users\myName\AppData\Roaming\Python\Python37\site-packages\pyqt5_tools`. Create a shortcut to `designer.exe` on your `Desktop`.

***You're all set!***

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## References
Articles and posts that helped me throughout my adventure:
 - [PyQt5 on a Raspberry Pi](https://raspberrypi.stackexchange.com/a/63058/104888);
 - [PyQt5 Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt5/);
 - [Python GUI's with PyQt5](https://www.youtube.com/watch?v=ksW59gYEl6Q);
 - [This PyQt5 GUI Playlist](https://www.youtube.com/watch?v=yD0iu3n-e_s&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa);
 - [Installing Raspbian](https://www.raspberrypi.org/downloads/raspbian/);
 - [This article on Periodic Tasks](https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679);

## Licensing

[![License](https://img.shields.io/github/license/ruirizzi/elder-medicine-alarm-clock.svg?color=blue&style=flat-square)](https://github.com/ruirizzi/elder-medicine-alarm-clock/blob/master/LICENSE)

