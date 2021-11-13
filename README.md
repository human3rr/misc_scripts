# misc_scripts
# b4bInfGrenade.py 

Install Python:

https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

Make sure to enable python path when you start the installer

In windows, run cmd:

>pip install pynput

>pip install pydirectinput

>pip install pyautogui

Then run:

python b4bInfGrenade.py

The resolution on your pc is probably different than mine so you'll need to change line 36 ( pydirectinput.click(982, 978)  )

  982, 978 should be whatever x, y coordinates works on your screen

Script is a little janky but it works most of the time
