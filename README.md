# `Battery Monitor`

_**Version** 7.7_

A Python script for **Windows** that monitors and controls the laptop's battery percentage, optionally with a smart plug, preventing it from getting too low or too high, thus helping to extend battery life. It works as an icon in the system tray.

#### **[Source code](https://github.com/FyeCobain/BatteryMonitor)**

### Requirements
##### **[pynput](https://pynput.readthedocs.io)**
##### **[simplesystray](https://github.com/actorpus/systrayv2)**
```console
pip install pynput simplesystray
```

### Usage

> To configure the script edit the _config.ini_ file

- You can set a **domain** to ping. Useful for gaming.

- If the **hibernation hotkey** is set to True, you can hibernate your computer by pressing **_Windows_ + _Insert_**.

- You can set two **URLs** so that the script makes a GET request when the percentage is less than the minimum or greater than the maximum allowed. Intended to set up an **IFTTT** webhook to turn **ON/OFF** a smart plug.

- You can set a Kasa username, password and device name (the one set in the Kasa app) for the same result.

If no ON/OFF **URLs** and no Kasa device are set, the script will play a sound when the battery needs to be connected or disconnected.

- You can open the script and pass it the path to a file. Closing the script will open that file. Intended to open the script from an application that needs to be closed and will be reopened when the user exits the script.
```
batterymonitor.pyw "C:\OpenWhenClosing.exe"
```

### Attributions

#### Icons

[Plug icons created by Pixel perfect - Flaticon](https://www.flaticon.com/free-icons/plug)

<a href="https://www.flaticon.com/free-icons/ui" title="ui icons">Ui icons created by Yudhi Restu - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/folder" title="folder icons">Folder icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/pause-button" title="pause button icons">Pause button icons created by Anggara - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/pause" title="pause icons">Pause icons created by IYAHICON - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/off" title="off icons">Off icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/clock" title="clock icons">Clock icons created by dmitri13 - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/right" title="right icons">Right icons created by Pixel perfect - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/cat" title="cat icons">Cat icons created by Dave Gandy - Flaticon</a>

#### Sounds

<a href="https://freesound.org/people/FoolBoyMedia/sounds/352650/">Piano Notification 4</a> by <a href="https://freesound.org/people/FoolBoyMedia/">FoolBoyMedia</a> | License: <a href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution NonCommercial 4.0</a>

<a href="https://freesound.org/people/ricemaster/sounds/278142/">effect_notify.wav</a> by <a href="https://freesound.org/people/ricemaster/">ricemaster</a> | License: <a href="http://creativecommons.org/publicdomain/zero/1.0/">Creative Commons 0</a>
