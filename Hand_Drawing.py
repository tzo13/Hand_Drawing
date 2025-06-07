import cv2
import numpy as np
import mediapipe as mp
import time
from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk

# Specify image paths for gesture images (update these with your actual file paths)
THUMB_UP_IMAGE_PATH = "thumbsupimg.png"  # Replace with your thumb-up image path
PEACE_SIGN_IMAGE_PATH = "peacesignimg.png"  # Replace with your peace sign image path
THREE_FINGERS_IMAGE_PATH = "punchimg.png"  # Replace with your punch image path

# Tkinter instruction windows
try:
    def show_first_window():
        root = Tk()
        root.title("Finger Drawing App Instructions - Page 1")
        root.geometry("800x600")  # Window size
        root.configure(background="black")
        # Center the window
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')

        # Main frame with grid layout
        frame = Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Instructions
        row = 0
        Label(frame, text="Finger Drawing App Instructions - Page 1", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=5)
        row += 1
        Label(frame, text="Welcome to the Finger Drawing App! Use your hands to draw on a virtual canvas via webcam.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="Hand Assignments:", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=5)
        row += 1
        Label(frame, text="- Right Hand: Draws lines when drawing mode is ON.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="- Left Hand: Performs gestures to control the app.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="Controls:", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=5)
        row += 1
        Label(frame, text="- Color Buttons: Click with right hand to select Green, Red, or Blue (top of screen) when drawing mode is OFF.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="- + Key: Increase brush size (1 to 20).", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="- - Key: Decrease brush size (1 to 20).", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="- ESC Key: Exit the app.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="Tips:", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=5)
        row += 1
        Label(frame, text="- Keep hands ~30-60 cm from the camera, palm facing forward.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)
        row += 1
        Label(frame, text="- Ensure good lighting for accurate hand tracking.", background="black", foreground="light blue").grid(row=row, column=0, sticky="w", pady=2)

        # Next button
        def go_to_second():
            root.destroy()  # Close first window
            show_second_window()

        Button(frame, text="Next", command=go_to_second, background="black", foreground="light blue").grid(row=row+1, column=0, pady=20)

        root.mainloop()

    def show_second_window():
        root = Tk()
        root.title("Finger Drawing App Instructions - Page 2")
        root.geometry("800x600")  # Window size
        # Center the window
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')

        # Main frame with grid layout
        frame = Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Load and resize images
        try:
            thumb_up_img = Image.open(THUMB_UP_IMAGE_PATH)
            thumb_up_img = thumb_up_img.resize((100, 100), Image.LANCZOS)
            thumb_up_photo = ImageTk.PhotoImage(thumb_up_img)
        except Exception as e:
            thumb_up_photo = None
            print(f"Error loading thumb-up image: {e}")

        try:
            peace_sign_img = Image.open(PEACE_SIGN_IMAGE_PATH)
            peace_sign_img = peace_sign_img.resize((100, 100), Image.LANCZOS)
            peace_sign_photo = ImageTk.PhotoImage(peace_sign_img)
        except Exception as e:
            peace_sign_photo = None
            print(f"Error loading peace sign image: {e}")

        try:
            three_fingers_img = Image.open(THREE_FINGERS_IMAGE_PATH)
            three_fingers_img = three_fingers_img.resize((100, 100), Image.LANCZOS)
            three_fingers_photo = ImageTk.PhotoImage(three_fingers_img)
        except Exception as e:
            three_fingers_photo = None
            print(f"Error loading three-finger image: {e}")

        # Instructions
        row = 0
        Label(frame, text="Finger Drawing App Instructions - Page 2", font=("Arial", 16, "bold")).grid(row=row, column=0, columnspan=2, sticky="w", pady=5)
        row += 1
        Label(frame, text="Gestures (Left Hand):", font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, sticky="w", pady=5)
        row += 1
        Label(frame, text="- Thumb Up: Toggles drawing mode ON/OFF.", font=("Arial", 12)).grid(row=row, column=0, sticky="w", pady=2)
        if thumb_up_photo:
            Label(frame, image=thumb_up_photo).grid(row=row, column=1, sticky="w", padx=10)
        else:
            Label(frame, text="Thumb-Up Image Missing", font=("Arial", 10), bg="lightgray", relief="solid", width=15, height=7).grid(row=row, column=1, sticky="w", padx=10)
        row += 1
        Label(frame, text="- Peace Sign (Index + Middle): Enters save mode to save the drawing.", font=("Arial", 12)).grid(row=row, column=0, sticky="w", pady=2)
        if peace_sign_photo:
            Label(frame, image=peace_sign_photo).grid(row=row, column=1, sticky="w", padx=10)
        else:
            Label(frame, text="Peace Sign Image Missing", font=("Arial", 10), bg="lightgray", relief="solid", width=15, height=7).grid(row=row, column=1, sticky="w", padx=10)
        row += 1
        Label(frame, text="- Three Fingers (Index, Middle, Ring): Clears the canvas.", font=("Arial", 12)).grid(row=row, column=0, sticky="w", pady=2)
        if three_fingers_photo:
            Label(frame, image=three_fingers_photo).grid(row=row, column=1, sticky="w", padx=10)
        else:
            Label(frame, text="Three-Finger Image Missing", font=("Arial", 10), bg="lightgray", relief="solid", width=15, height=7).grid(row=row, column=1, sticky="w", padx=10)
        row += 1
        Label(frame, text="Saving a Drawing:", font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, sticky="w", pady=5)
        row += 1
        Label(frame, text="- In save mode (peace sign), type a filename, press Enter to save the webcam + drawing, or Esc to cancel.", font=("Arial", 12)).grid(row=row, column=0, columnspan=2, sticky="w", pady=2)

        # Keep photo references to prevent garbage collection
        root.thumb_up_photo = thumb_up_photo
        root.peace_sign_photo = peace_sign_photo
        root.three_fingers_photo = three_fingers_photo

        # Previous and Start buttons
        def go_to_first():
            root.destroy()  # Close second window
            show_first_window()

        def start_app():
            root.destroy()  # Close second window
            start_drawing_app()

        Button(frame, text="Previous", command=go_to_first, font=("Arial", 12)).grid(row=row+1, column=0, pady=20, padx=10)
        Button(frame, text="Start", command=start_app, font=("Arial", 12)).grid(row=row+1, column=1, pady=20, padx=10)

        root.mainloop()

except Exception as e:
    print(f"Error initializing Tkinter: {e}")
    exit()

def start_drawing_app():
    # Initialize MediaPipe Hands
    try:
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.8, min_tracking_confidence=0.5)
        mp_drawing = mp.solutions.drawing_utils
    except Exception as e:
        print(f"Error initializing MediaPipe: {e}")
        exit()

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        exit()

    canvas = None  # Canvas for drawing
    last_x, last_y = -1, -1
    color = (0, 255, 0)  # Default: Green
    brush_size = 10  # Default for bolder lines
    drawing_enabled = False  # Drawing toggle
    last_button_press_time = 0  # For debouncing button presses
    last_gesture_time = 0  # For debouncing gestures
    debounce_interval = 0.8  # 0.8s debounce for gestures
    save_mode = False  # Toggle for save input mode
    filename_input = ""  # Current filename being typed
    gesture_counter = {}  # Track gesture consistency
    gesture_stability_frames = 3  # Require gesture for 3 frames
    min_movement_threshold = 5  # Pixels to consider valid movement for drawing

    # Frame dimensions (original webcam resolution)
    frame_width, frame_height = 640, 480

    # Get screen resolution (fallback to common resolution if screeninfo unavailable)
    try:
        import screeninfo
        monitor = screeninfo.get_monitors()[0]
        screen_width, screen_height = monitor.width, monitor.height
    except:
        screen_width, screen_height = 1920, 1080  # Fallback resolution

    # Calculate scaling to fit screen while preserving aspect ratio
    aspect_ratio = frame_width / frame_height
    screen_aspect_ratio = screen_width / screen_height

    if screen_aspect_ratio > aspect_ratio:
        new_height = screen_height
        new_width = int(new_height * aspect_ratio)
    else:
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

    # Set up fullscreen window
    cv2.namedWindow("Finger Drawing App", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Finger Drawing App", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Define color buttons (x, y, width, height, color, label)
    buttons = [
        {"rect": (10, 10, 100, 50), "color": (0, 255, 0),"label": "Green", "image": "green.png"},
        {"rect": (120, 10, 100, 50), "color": (0, 0, 255), "label": "Red","image": "red.png"},
        {"rect": (230, 10, 100, 50), "color": (255, 0, 0), "label": "Blue","image": r"E:\ΠΑΙΔΙΑ\Tzo\blue.png"}
    ]

    def is_finger_up(tip, wrist_y, pip_y=None, threshold=0.15):
        """Check if a finger's tip is above the wrist (optional PIP check)."""
        try:
            if pip_y is not None:
                return tip.y < wrist_y - threshold and tip.y < pip_y - 0.05
            return tip.y < wrist_y - threshold
        except Exception as e:
            print(f"Error in is_finger_up: {e}")
            return False

    def is_finger_down(tip, wrist_y, pip_y=None, threshold=0.1):
        """Check if a finger's tip is near wrist level (optional PIP check)."""
        try:
            if pip_y is not None:
                return tip.y >= wrist_y - threshold and tip.y > pip_y
            return tip.y >= wrist_y - threshold
        except Exception as e:
            print(f"Error in is_finger_down: {e}")
            return False

    def detect_gesture(hand_landmarks):
        """Detect specific gestures based on finger positions."""
        try:
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_pip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]

            wrist_y = wrist.y

            # Check finger states
            thumb_up = is_finger_up(thumb_tip, wrist_y, thumb_pip.y, threshold=0.12)
            index_up = is_finger_up(index_tip, wrist_y, index_pip.y)
            middle_up = is_finger_up(middle_tip, wrist_y, middle_pip.y)
            ring_up = is_finger_up(ring_tip, wrist_y, ring_pip.y)
            pinky_up = is_finger_up(pinky_tip, wrist_y, pinky_pip.y)

            thumb_down = is_finger_down(thumb_tip, wrist_y, thumb_pip.y)
            index_down = is_finger_down(index_tip, wrist_y, index_pip.y)
            middle_down = is_finger_down(middle_tip, wrist_y, middle_pip.y)
            ring_down = is_finger_down(ring_tip, wrist_y, ring_pip.y)
            pinky_down = is_finger_down(pinky_tip, wrist_y, pinky_pip.y)

            # Debug: Display finger states and wrist position
            finger_states = f"T:{'U' if thumb_up else 'D'} I:{'U' if index_up else 'D'} M:{'U' if middle_up else 'D'} R:{'U' if ring_up else 'D'} P:{'U' if pinky_up else 'D'}"
            debug_info = f"Wrist Y: {wrist_y:.2f}"

            # Highlight fingertips for three-finger (clear) gesture
            highlight_tips = []
            if index_up and middle_up and ring_up and not thumb_up and not pinky_up:
                highlight_tips = [(index_tip.x, index_tip.y), (middle_tip.x, middle_tip.y), (ring_tip.x, ring_tip.y)]

            # Gesture: Two fingers up (index and middle)
            if index_up and middle_up and not thumb_up and not ring_up and not pinky_up:
                return "save", finger_states, debug_info, []
            # Gesture: Thumb up, others not up
            elif thumb_up and not index_up and not middle_up and not ring_up and not pinky_up:
                return "toggle_drawing", finger_states, debug_info, []
            # Gesture: Three fingers (index, middle, ring up)
            elif index_up and middle_up and ring_up and not thumb_up and not pinky_up:
                return "clear", finger_states, debug_info, highlight_tips
            return None, finger_states, debug_info, []
        except Exception as e:
            print(f"Error in detect_gesture: {e}")
            return None, "", "", []

    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            frame = cv2.flip(frame, 1)
            if canvas is None:
                canvas = np.zeros_like(frame)

            # Process hand tracking only if not in save mode
            if not save_mode:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)

                fingertip_detected = False
                x, y = -1, -1
                gesture_detected = None
                gesture_x, gesture_y = 0, 0
                finger_states = ""
                debug_info = ""
                highlight_tips = []
                current_time = time.time()

                if results.multi_hand_landmarks and results.multi_handedness:
                    # Sort hands by x-coordinate to handle misclassification
                    hands_data = []
                    for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                        wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        label = handedness.classification[0].label
                        hands_data.append((hand_landmarks, label, wrist_x))
                    hands_data.sort(key=lambda x: x[2], reverse=True)

                    for i, (hand_landmarks, label, wrist_x) in enumerate(hands_data):
                        is_right_hand = (i == 0) if len(hands_data) > 1 else (label == "Right")

                        # Debug: Display handedness
                        wrist_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame_height)
                        wrist_x_px = int(wrist_x * frame_width)
                        cv2.putText(frame, "R" if is_right_hand else "L", (wrist_x_px, wrist_y + 20),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                        if is_right_hand:
                            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                            x, y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
                            fingertip_detected = True

                            cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)

                            # Check for color button press (only when drawing is disabled)
                            button_pressed = False
                            if not drawing_enabled and current_time - last_button_press_time >= debounce_interval:
                                for button in buttons:
                                    bx, by, bw, bh = button["rect"]
                                    if bx <= x <= bx + bw and by <= y <= by + bh:
                                        color = button["color"]
                                        last_button_press_time = current_time
                                        button_pressed = True
                                        last_x, last_y = -1, -1  # Reset to prevent unwanted lines
                                        break

                            # Draw only if enabled, with valid previous position, and sufficient movement
                            if drawing_enabled:
                                if last_x == -1 or last_y == -1:
                                    # Set starting position without drawing
                                    last_x, last_y = x, y
                                else:
                                    # Check movement threshold to filter jitter
                                    distance = np.sqrt((x - last_x)**2 + (y - last_y)**2)
                                    if distance > min_movement_threshold:
                                        cv2.line(canvas, (last_x, last_y), (x, y), color, brush_size)
                                    else:
                                        print(f"Drawing blocked: insufficient movement (distance: {distance:.2f} pixels)")
                                    last_x, last_y = x, y

                        else:
                            gesture, finger_states, debug_info, highlight_tips = detect_gesture(hand_landmarks)
                            if gesture:
                                gesture_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame_width)
                                gesture_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame_height)
                                gesture_counter[gesture] = gesture_counter.get(gesture, 0) + 1
                                if gesture_counter[gesture] >= gesture_stability_frames:
                                    gesture_detected = gesture
                            else:
                                gesture_counter.clear()

                            # Visual debugging: Draw wrist and threshold lines
                            wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                            wrist_y_px = int(wrist_y * frame_height)
                            threshold_up_px = int((wrist_y - 0.15) * frame_height)
                            threshold_down_px = int((wrist_y - 0.1) * frame_height)
                            cv2.line(frame, (0, wrist_y_px), (frame_width, wrist_y_px), (255, 255, 255), 1)
                            cv2.line(frame, (0, threshold_up_px), (frame_width, threshold_up_px), (0, 255, 0), 1)
                            cv2.line(frame, (0, threshold_down_px), (frame_width, threshold_down_px), (0, 0, 255), 1)

                            # Draw fingertip highlights (red for three-finger gesture)
                            for tip_x, tip_y in highlight_tips:
                                cv2.circle(frame, (int(tip_x * frame_width), int(tip_y * frame_height)), 7, (0, 0, 255), -1)

                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Process detected gesture with debouncing
                if gesture_detected and current_time - last_gesture_time >= debounce_interval:
                    if gesture_detected == "save":
                        save_mode = True
                        filename_input = ""
                    elif gesture_detected == "clear":
                        canvas[:] = 0
                        last_x, last_y = -1, -1
                    elif gesture_detected == "toggle_drawing":
                        drawing_enabled = not drawing_enabled
                        if not drawing_enabled:
                            last_x, last_y = -1, -1  # Reset when disabling drawing
                    last_gesture_time = current_time
                    gesture_counter.clear()

                # Display gesture feedback and debug info
                if gesture_detected:
                    gesture_text = {
                        "save": "Save Detected",
                        "clear": "Clear Detected (Three Fingers)",
                        "toggle_drawing": "Toggle Drawing"
                    }[gesture_detected]
                    cv2.putText(frame, gesture_text, (gesture_x, gesture_y - 20),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                if finger_states:
                    cv2.putText(frame, finger_states, (gesture_x, gesture_y - 40),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(frame, debug_info, (gesture_x, gesture_y - 60),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                if not fingertip_detected:
                    last_x, last_y = -1, -1  # Reset when right hand exits

            # Create clean composite for saving (webcam + drawing, no UI)
            composite = cv2.addWeighted(frame, 1, canvas, 1.0, 0)

            # Draw buttons on display frame (not composite)
            for button in buttons:
                bx, by, bw, bh = button["rect"]
                button_color = button["color"]
                label = button["label"]
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), button_color, -1)
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 255, 255), 2)
                cv2.putText(frame, label, (bx + 10, by + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

            # Overlay canvas on display frame with full opacity
            output = cv2.addWeighted(frame, 1, canvas, 1.0, 0)

            # Display drawing status and current color
            status = "Drawing: ON" if drawing_enabled else "Drawing: OFF"
            cv2.putText(output, status, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            color_name = "Green" if color == (0, 255, 0) else "Red" if color == (0, 0, 255) else "Blue"
            cv2.putText(output, f"Color: {color_name}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Draw instruction box
            box_x, box_y = 350, 10
            box_width, box_height = 250, 150
            cv2.rectangle(output, (box_x, box_y), (box_x + box_width, box_y + box_height), (200, 200, 200), -1)
            cv2.rectangle(output, (box_x, box_y), (box_x + box_width, box_y + box_height), (255, 255, 255), 2)

            text_x, text_y = box_x + 10, box_y + 20
            cv2.putText(output, "Left: Thumb up = Toggle draw", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(output, "Left: Two fingers = Save", (text_x, text_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(output, "Left: Three fingers = Clear", (text_x, text_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(output, "+: Increase brush size", (text_x, text_y + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(output, "-: Decrease brush size", (text_x, text_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(output, "ESC: Exit", (text_x, text_y + 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)

            # Draw save mode input box if active
            if save_mode:
                overlay = output.copy()
                cv2.rectangle(overlay, (0, 0), (frame_width, frame_height), (0, 0, 0), -1)
                output = cv2.addWeighted(overlay, 0.5, output, 0.5, 0)

                input_box_x, input_box_y = 100, frame_height // 2 - 30
                input_box_width, input_box_height = 440, 60
                cv2.rectangle(output, (input_box_x, input_box_y),
                             (input_box_x + input_box_width, input_box_y + input_box_height),
                             (200, 200, 200), -1)
                cv2.rectangle(output, (input_box_x, input_box_y),
                             (input_box_x + input_box_width, input_box_y + input_box_height),
                             (255, 255, 255), 2)

                cv2.putText(output, "Enter filename (Enter to save, Esc to cancel):",
                           (input_box_x + 10, input_box_y - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                cv2.putText(output, filename_input,
                           (input_box_x + 10, input_box_y + 40),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

            # Display output
            output_resized = cv2.resize(output, (new_width, new_height), interpolation=cv2.INTER_AREA)
            screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
            x_offset = (screen_width - new_width) // 2
            y_offset = (screen_height - new_height) // 2
            screen[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = output_resized

            cv2.imshow("Finger Drawing App", screen)
            key = cv2.waitKey(1) & 0xFF

            # Handle key inputs
            if save_mode:
                if key == 27:  # Esc: Cancel save mode
                    save_mode = False
                    filename_input = ""
                elif key == 13:  # Enter: Save file
                    if filename_input.strip():
                        filename = filename_input.strip()
                        if not filename.endswith('.png'):
                            filename += '.png'
                        try:
                            cv2.imwrite(filename, composite)  # Save composite (webcam + drawing)
                            print(f"Drawing saved as {filename}")
                        except Exception as e:
                            print(f"Error saving drawing: {e}")
                    else:
                        print("Save cancelled: No filename entered")
                    save_mode = False
                    filename_input = ""
                elif key == 8:  # Backspace: Delete last character
                    filename_input = filename_input[:-1]
                elif 32 <= key <= 126:  # Printable ASCII characters
                    filename_input += chr(key)
            else:
                if key == ord('+'):
                    brush_size = min(brush_size + 1, 20)
                elif key == ord('-'):
                    brush_size = max(brush_size - 1, 1)
                elif key == 27:  # ESC key
                    break

        except Exception as e:
            print(f"Error in main loop: {e}")
            break

    cap.release()
    cv2.destroyAllWindows()
    hands.close()

# Start the program with the first instruction window
show_first_window()