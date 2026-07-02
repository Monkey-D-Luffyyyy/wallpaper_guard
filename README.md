# 🛡️ Wallpaper Guard

**A Python-based desktop wallpaper protection tool that automatically enforces your chosen wallpaper and prevents unauthorized changes.**

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Run at Startup (Silent Mode)](#run-at-startup-silent-mode)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)
- [License](#license)

## ✨ Features

- **Automatic Enforcement**: Continuously monitors and reverts wallpaper changes
- **Configurable Interval**: Set how often to check for changes (default: 5 seconds)
- **Silent Background Operation**: Run without visible console windows
- **Auto-Start**: Configure to run automatically at Windows login
- **Lightweight**: Minimal CPU and memory usage
- **Admin Protection**: Prevents standard users from changing desktop wallpaper

## 🔧 How It Works

Wallpaper Guard uses a simple but effective approach:

1. **Monitors** the Windows Registry for wallpaper changes
2. **Detects** when the current wallpaper differs from your configured image
3. **Reverts** any unauthorized changes automatically
4. **Runs** continuously in the background with minimal resource usage

The script uses:
- `ctypes` to interact with Windows API (`user32.dll`)
- `winreg` to read Windows Registry settings
- An infinite loop with sleep intervals for efficient monitoring

## 📦 Requirements

- **Operating System**: Windows 7/8/10/11
- **Python**: 3.6 or higher
- **Dependencies**: 
  - `pywin32` (for Windows Registry access)

## 🚀 Installation & Dependencies
1. **Install Python Dependencies**
- This script requires the pywin32 library to interact with the Windows Registry (winreg).
  Open your Command Prompt (cmd) or PowerShell, navigate to the project folder, and run:
- **pip install pywin32**

3. **Set Your Wallpaper Path**
- Open wallpaper_guard.py in a text editor (like VS Code or Notepad) and update the WALLPAPER_PATH variable to point to       your desired image:
# Change this to the actual path of your image
WALLPAPER_PATH = r"C:\Users\YourName\Pictures\my_wallpaper.png"  

- ⚠️ Note: Use raw strings (r"...") for Windows paths to avoid escape character issues. If your image is in OneDrive, right-click the file in File Explorer and select "Always keep on this device" so it is available offline.

- 🔁 Automating at Startup (Silent VBScript)
- If you want the script to run automatically when Windows boots up, and you want it to run completely silently (no black command prompt window), follow these steps:
- Step 1: Create the VBScript Launcher
- Open Notepad.
- Paste the following code:
Set WshShell = CreateObject("WScript.Shell")
' Update the path below to where your wallpaper_guard.py is located
WshShell.Run "pythonw ""C:\full\path\to\wallpaper_guard.py""", 0, False

(Make sure to change C:\full\path\to\... to the actual location of your script!)

- Go to File > Save As.
- Name the file start_guard.vbs.
- Crucial: Change "Save as type" at the bottom to "All Files (.)" so it doesn't save as a .txt file.
- Save it in the same folder as your Python script.
- 💡 Why pythonw? We use pythonw.exe instead of python.exe. The "w" stands for "windowless", meaning it runs Python scripts in the background without opening a console window.
- Step 2: Add to Windows Startup
- Press Win + R on your keyboard to open the Run dialog.
- Type shell:startup and press Enter. This opens your personal Windows Startup folder.
- Copy or Move your start_guard.vbs file into this Startup folder.


### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wallpaper_guard.git
cd wallpaper_guard




