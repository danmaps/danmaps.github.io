---
date: 2024-10-09
tags:
- AutoHotKey
- Productivity
- Work
title: Creating a Virtual Numpad with AutoHotKey
---


<iframe width="100%" height="500" frameborder="0"
  src="https://observablehq.com/embed/@59335169eee5a8a6/numpad@339?cell=*"></iframe>

I recently built a virtual numpad using AutoHotKey to adapt to my new keyboard setup. I switched to a Freestyle2 Blue keyboard, which lacks the built-in numpad I was accustomed to. This became particularly frustrating when starting my workday, as I needed to enter an authenticator code to connect to the corporate VPN. After a few days of struggling with the top-row numbers, I realized I needed a numpad solution that would not add extra hardware to my desk. Separate numpads seemed inefficient and impractical.

## Initial Challenges and Solution

Initially, I explored remapping keys using my keyboard's configuration tools, but this approach proved to be cumbersome. Eventually, I found a simple yet effective solution with AutoHotKey. I configured it so that when I hold down the CapsLock key, the letter keys under 7, 8, and 9 remap to function as a full numpad. This allows me to comfortably touch-type numbers with my right hand while holding CapsLock with my left pinky. The script also ensures that CapsLock does not activate inadvertently—it remains off unless explicitly pressed.

## Alt-Code Functionality

Another useful feature of this script is its ability to handle alt-codes. By holding down CapsLock along with the Alt key, I can type an alt-code, and when I release Alt, the corresponding symbol is sent. For example:

♥ <- `Alt` + `9731`

This setup has significantly improved my workflow, allowing me to maintain a clean desk space while retaining the functionality I need for efficient input.

## The Script

```AutoHotkey
#Requires AutoHotkey v2.0

SetCapsLockState(GetKeyState("CapsLock", "T") ? "AlwaysOn" : "AlwaysOff") ; Prevent capslock from lighting up when first used as modifier.
CapsLock::SetCapsLockState(GetKeyState("CapsLock", "T") ? "AlwaysOff" : "AlwaysOn") ; Set capslock to the opposite state when not used as a hotkey modifier.

CreateNumpadKeys()
CreateNumpadKeys() {
    static AltCode := ""
    static keyMap := Map(
        "m", 0,
        ",", 0,
        "j", 1,
        "k", 2,
        "l", 3,
        "u", 4,
        "i", 5,
        "o", 6,
        "7", 7,
        "8", 8,
        "9", 9
    )
    Hotkey "~*Alt up", OnAltUp, "On"            ; Create hotkey for when Alt is released. 
    for key, num in keyMap {                    ; for-loop each key, value in keyMap.
        Hotkey "CapsLock & " key, remap, "On"   ; Create hotkeys with CapsLock as the modifier.
    }

    static remap(ThisKey) {
        num := keyMap[SubStr(ThisKey, -1)]  ; Get last character from current hotkey, and use it to get number from keyMap.
        if GetKeyState("Alt", "P")
            AltCode .= num                  ; If Alt is down, concatenate the number to AltCode variable.
        else
            Send "{Numpad" num "}"          ; If Alt is not down, send the number.
    }

    static OnAltUp(*) {
        if AltCode {
            Send "{ASC " AltCode "}"        ; When Alt is released send the saved alt code.
            AltCode := ""
        }
    }
}
```

## Making this run at startup

I made this script run when I log into Windows. To do so, I created a shortcut to the script in `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`.