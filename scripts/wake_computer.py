"""
Wake the computer from sleep
"""

import ctypes
import time
import subprocess
import os
import sys
from datetime import datetime

class WakeComputer:
    def __init__(self, logger=None):
        self.logger = logger
        self.wake_methods = [
            self._simulate_key_press,
            self._reset_system_timer,
            self._simulate_mouse_move,
        ]
        
    def _log(self, message, level="info"):
        if self.logger:
            if level == "info":
                self.logger.info(message)
            elif level == "error":
                self.logger.error(message)
            elif level == "warning":
                self.logger.warning(message)
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    
    def wake_up(self, method="auto"):
        self._log(f"Attempting to wake up  computer using method: {method}")
        
        try:
            if method == "auto":
                for wake_method in self.wake_methods:
                    try:
                        if wake_method():
                            self._log(f"Computer Successfully woken up using {wake_method.__name__}")
                            return True
                        time.sleep(0.5)
                    except Exception as e:     
                        self._log(f"Method {wake_method.__name__} failed with error: {e}", "warning")
                        continue
                
                #If all methods fail
                return self._direct_wake()
            
            elif method == "keypress":
                return self._simulate_key_press()
            elif method == "mouse":
                return self._simulate_mouse_move()
            elif method == "api":
                return self._reset_system_timer()
            else:
                self._log(f"Unknown wake method: {method}", "error")
                return False

        except Exception as e:
            self._log(f"Error waking the computer: {e}", "error")
            return False
    
    def _simulate_key_press(self):
        try:
            #Virtual key codes
            VK_MEDIA_PLAY_PAUSE = 0xB3
            VK_SPACE = 0x20
            VK_VOLUME_UP = 0xAF
            
            # Try different keys 
            keys_to_try = [VK_SPACE, VK_MEDIA_PLAY_PAUSE, VK_VOLUME_UP]
            
            for key in keys_to_try:
                try:
                    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
                    time.sleep(0.05)
                    #Release key
                    ctypes.windll.user32.keybd_event(key, 0, 2, 0)
                    time.sleep(0.05)
                except:
                    continue
            self._log("Simulated key press")
            return True
        
        except Exception as e:
            self._log(f"Key press simulation failed: {e}", "warning")
            return False
        
    def _reset_system_timer(self):     
        try:
            ES_SYSTEM_REQUIRED = 0x00000001
            ES_CONTINUOUS = 0x80000000
            ES_DISPLAY_REQUIRED = 0x00000002
            
            #Reset the idle timer
            result = ctypes.windll.kernel32.SetThreadExecutionState(
                ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
            )
            
            if result:
                self._log("Reset system idle timer")
                return True
            else:
                self._log("Failed to reset idle timer", "warning")
                return False
        
        except Exception as e:
            self._log(f"System timer reset failed: {e}", "warning")
            return False
        
    def _simulate_mouse_move(self):
        try:
            class POINT(ctypes.Structure):
                _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
            
            point = POINT()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
            
            #Move cursor slightly
            ctypes.windll.user32.SetCursorPos(point.x + 2, point.y + 2)
            time.sleep(0.1)
            ctypes.windll.user32.SetCursorPos(point.x, point.y)
            
            self._log("Simulated mouse movement")
            return True
        
        except Exception as e:
            self._log(f"Mouse movement simulation failed: {e}", "warning")
            return False
        
    def _direct_wake(self):
        try:
            self._reset_system_timer()
            time.sleep(0.1)
            self._simulate_key_press()
            time.sleep(0.1)
            self._simulate_mouse_move()
            
        except Exception as e:
            self._log(f"Direct wake failed: {e}", "error")
            return False
        
    def prevent_sleep(self, duration_minutes=60):
        try:
            ES_CONTINUOUS = 0x80000000
            ES_SYSTEM_REQUIRED = 0x00000001
            ES_DISPLAY_REQUIRED = 0x00000002
            
            ctypes.windll.kernel32.SetThreadExecutionState(
                ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
            )
            
            self._log(f"Sleep prevention activated for {duration_minutes} minutes")
            
            time.sleep(duration_minutes * 60)
            
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        
        except Exception as e:
            self._log(f"Failed to prevent sleep: {e}", "error")
            
    def check_sleep_state(self):
        try:
            class POINT(ctypes.Structure):
                _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
                
            point = POINT()
            success = ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
            
            if success:
                self._log("Computer appears to be awake")
                return "awake"
            else:
                self._log("Computer may be sleeping")
                return "sleeping"
        
        except:
            return "unknown"
        
        
# Test function
def test_wake_functions():
    """Test all wake functions"""
    print("Testing wake computer functions...")
    wake = WakeComputer()
    
    # Check current state
    state = wake.check_sleep_state()
    print(f"Current state: {state}")
    
    # Test key press
    print("\n1. Testing key press...")
    if wake._simulate_key_press():
        print("✓ Key press successful")
    else:
        print("✗ Key press failed")
    
    # Test mouse movement
    print("\n2. Testing mouse movement...")
    if wake._simulate_mouse_move():
        print("✓ Mouse movement successful")
    else:
        print("✗ Mouse movement failed")
    
    # Test system timer
    print("\n3. Testing system timer reset...")
    if wake._reset_system_timer():
        print("✓ System timer reset successful")
    else:
        print("✗ System timer reset failed")
    
    # Test auto wake
    print("\n4. Testing auto wake...")
    if wake.wake_up("auto"):
        print("✓ Auto wake successful")
    else:
        print("✗ Auto wake failed")
    
    print("\nTest completed!")

if __name__ == "__main__":
    test_wake_functions()
            
            
            
                
            
            
            
            
            
            
            
            
            
            
            
                
                    
            
            
    
            
                       