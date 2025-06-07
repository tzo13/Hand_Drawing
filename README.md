# Finger Drawing App with Hand Gestures 🎨🤚

A cool real-time finger tracking drawing app using **MediaPipe**, **OpenCV**, and Python, where you control the canvas with your hands! Draw with your right hand, and use your left hand to send commands—like toggling drawing, saving your masterpiece, or clearing the canvas—without touching a single key.

---

## Features

* **Right Hand Index Finger Drawing**: Draw lines by moving your right hand’s index finger.
* **Left Hand Gestures to Control**:

  * **Thumb Up**: Toggle drawing on/off.
  * **Two Fingers Up (Index + Middle)**: Save the current drawing.
  * **Three Fingers Up (Index + Middle + Ring)**: Clear the canvas.
* **Brush size control** with `+` and `-` keys.
* **Color buttons** on screen to select drawing colors by touching them with your finger.
* **Filename input box** for saving images without leaving the app.
* Visual debug overlays for wrist position and finger states.
* Real-time hand landmark visualization using MediaPipe.

---

## How to Use

1. Run the script, allow webcam access.
2. Use your **right hand** index finger to draw on the screen.
3. Use your **left hand** to:

   * Show **thumb up** to toggle drawing mode on/off.
   * Show **two fingers up** (index + middle) to enter save mode.
   * Show **three fingers up** (index + middle + ring) to clear the canvas.
4. When saving, type the filename and press **Enter**, or press **Esc** to cancel.
5. Use `+` and `-` keys to adjust brush size.
6. Press **Esc** anytime to quit.

---

## Requirements

* Python 3.7+
* OpenCV (`cv2`)
* MediaPipe (`mediapipe`)
* NumPy

Install dependencies via pip:

```bash
pip install opencv-python mediapipe numpy
```

---

## How It Works 

* Uses **MediaPipe Hands** to detect hand landmarks.
* Detects finger positions relative to the wrist to decide if fingers are "up" or "down".
* Differentiates right and left hands to assign drawing vs gesture control roles.
* Implements debouncing logic to avoid accidental repeated gestures.
* Combines webcam feed with a transparent canvas layer for smooth drawing.

---

## Why This Is Awesome

No mouse, no keyboard—just your hands! Perfect for quick sketches, presentations, or impressing friends at parties.

---


