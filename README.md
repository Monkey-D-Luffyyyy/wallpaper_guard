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

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wallpaper_guard.git
cd wallpaper_guard


