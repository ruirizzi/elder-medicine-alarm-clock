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

### Running PyQt5-based Apps

It's a bit tricky to run Python apps that use PyQt5 to create GUI, but after some work, I figured that you should (as of June 2019):

```shell
sudo apt-get install qt5-default
curl https://www.riverbankcomputing.com/static/Downloads/sip/4.19.17/sip-4.19.17.zip 
curl https://www.riverbankcomputing.com/static/Downloads/PyQt5/5.12.2/PyQt5_gpl-5.12.2.zip
tar sip-4.19.17.zip -xzfv (on your download directory)
tar PyQt5_gpl-5.12.2.zip -xzfv (on your download directory)
```
CD to `sip-4.19.17`folder:
```shell
python3 configure.py
make (this will take a shit-load of time)
```
CD to `PyQt5_gpl-5.12.2`folder:
```shell
python3 configure.py --sip \your-sip-dir-location\sip-4.19.17\sipgen\sip
make
```
After all theses steps you should be able to run the Python script with PyQt5 GUI.

## Licensing

"The code in this project is licensed under MIT license."

MIT © [ruirizzi]()
