import ctypes
import time
import os
import winreg  # Part of pywin32, but we only use it for reading registry

# --- CONFIGURATION ---
# Make sure this path is EXACT and the file exists
WALLPAPER_PATH = r"C:\Users\LAB3-StudentPC20\OneDrive\666\bsitlogo.png"  
CHECK_INTERVAL = 5  # Check every 5 seconds
# ---------------------

def set_wallpaper(image_path):
    """Sets the desktop wallpaper using ctypes (Windows API)"""
    if not os.path.exists(image_path):
        print(f"ERROR: Image not found at {image_path}")
        return False
    
    # SPI_SETDESKWALLPAPER = 0x0014
    # SPIF_UPDATEINIFILE = 0x0001
    # SPIF_SENDCHANGE = 0x0002
    result = ctypes.windll.user32.SystemParametersInfoW(
        0x0014, 
        0, 
        image_path, 
        0x0001 | 0x0002
    )
    
    if result == 0:
        print("Failed to set wallpaper. Check if file is accessible.")
        return False
    return True


def get_current_wallpaper():
    """Gets the current wallpaper path from the registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop")
        value, _ = winreg.QueryValueEx(key, "Wallpaper")
        winreg.CloseKey(key)
        return value
    except Exception as e:
        print(f"Error reading registry: {e}")
        return None


def main():
    print(f"Wallpaper Guard Started.")
    print(f"Enforcing: {WALLPAPER_PATH}")
    
    # Verify file exists before starting loop
    if not os.path.exists(WALLPAPER_PATH):
        print("CRITICAL ERROR: Wallpaper file does not exist!")
        input("Press Enter to exit...")
        return

    # Initial set to ensure it's correct right now
    print("Setting initial wallpaper...")
    set_wallpaper(WALLPAPER_PATH)
    
    while True:
        try:
            current_wp = get_current_wallpaper()
            
            # If the current wallpaper is NOT our desired one, revert it
            if current_wp and current_wp.lower() != WALLPAPER_PATH.lower():
                print(f"Detected change! Reverting to original...")
                set_wallpaper(WALLPAPER_PATH)
            
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            print("\nGuard stopped by user (Ctrl+C).")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()