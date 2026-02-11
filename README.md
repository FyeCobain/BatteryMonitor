# `Battery Monitor`

_**Version** 6.2_

A Python script for **Windows** that monitors and controls the laptop's battery percentage, optionally with a smart plug, preventing it from getting too low or too high, thus helping to extend battery life. It functions as an icon in the system tray.

#### **[Source code](https://github.com/FyeCobain/Battery-monitor)**

### Requirements
##### **[pynput](https://pynput.readthedocs.io)**
##### **[simplesystray](https://github.com/actorpus/systrayv2)**
```console
pip install pynput simplesystray
```

### Usage

> To configure the script edit the _config.ini_ file

- You can set a **domain** to ping. Useful for gaming.

- If the **hibernation hotkey**  is set to True, you can hibernate by pressing _left shift_ + _right shift_ + _space_.

- You can set two **URLs** so that the script makes a GET request when the percentage is less than the minimum or greater than the maximum allowed. Intended to set up an **IFTTT** webhook to turn **ON/OFF** a smart plug.

- You can set a Kasa token and device ID for the same result. Please refer to [this gist](https://gist.github.com/FyeCobain/1e367b0a9d5693c579a4fd6b20fac682).

If no ON/OFF **URLs** and no Kasa device are set, the script will play a sound when the battery needs to be connected or disconnected.

- You can open the script and pass it the path to a file. Closing the script will open that file. Intended to open the script from an application that needs to be closed and will be reopened when the user exits the script.
```
batterymonitor.pyw "C:\OpenWhenClosing.exe"
```

### Attributions

#### Icons

[Plug icons created by Pixel perfect - Flaticon](https://www.flaticon.com/free-icons/plug)

#### Sounds

<a href="https://freesound.org/people/FoolBoyMedia/sounds/352652/">Piano Notification 2</a> by <a href="https://freesound.org/people/FoolBoyMedia/">FoolBoyMedia</a> | License: <a href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution NonCommercial 4.0</a>

<a href="https://freesound.org/people/FoolBoyMedia/sounds/352651/">Piano Notification 3</a> by <a href="https://freesound.org/people/FoolBoyMedia/">FoolBoyMedia</a> | License: <a href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution NonCommercial 4.0</a>

<a href="https://freesound.org/people/FoolBoyMedia/sounds/352655/">Piano Notification 5a</a> by <a href="https://freesound.org/people/FoolBoyMedia/">FoolBoyMedia</a> | License: <a href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution NonCommercial 4.0</a>
