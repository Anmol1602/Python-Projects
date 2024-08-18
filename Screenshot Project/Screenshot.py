import pyautogui
import cv2
import numpy as np
import time
from datetime import datetime
import subprocess

# Global variables for storing the start and end points of the ROI
start_point = None
end_point = None
drawing = False


def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing, screenshot

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            display_image = screenshot.copy()
            cv2.rectangle(display_image, start_point, end_point, (0, 255, 0), 2)
            cv2.imshow("Select ROI", display_image)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(screenshot, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Select ROI", screenshot)


def screenshot_roi():
    global screenshot

    print("Switch to the window where you want to snip the screen.")
    time.sleep(5)

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    cv2.namedWindow("Select ROI", cv2.WND_PROP_FULLSCREEN)
    cv2.setMouseCallback("Select ROI", draw_rectangle)

    print(
        "Drag the mouse to select the ROI. Press 'Enter' to confirm, or 'Esc' to cancel."
    )

    while True:
        cv2.imshow("Select ROI", screenshot)
        key = cv2.waitKey(1) & 0xFF
        if key == 13:
            break
        elif key == 27:
            cv2.destroyAllWindows()
            return None

    cv2.destroyAllWindows()

    x1, y1 = start_point
    x2, y2 = end_point
    roi_x = min(x1, x2)
    roi_y = min(y1, y2)
    roi_w = abs(x2 - x1)
    roi_h = abs(y2 - y1)

    screenshot_roi = pyautogui.screenshot(region=(roi_x, roi_y, roi_w, roi_h))
    screenshot_array = np.array(screenshot_roi)
    screenshot_array = cv2.cvtColor(screenshot_array, cv2.COLOR_RGB2BGR)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.jpg"
    cv2.imwrite(filename, screenshot_array)
    print(f"Screenshot saved as '{filename}'.")

    # Ask if the user wants to extract text
    extract_text = input(
        "Do you want to extract text from the snipped image? (yes/no): "
    ).lower()
    if extract_text == "yes":
        subprocess.run(["python", "extracted_text.py", filename])

    return screenshot_array


# Example usage
screenshot = screenshot_roi()

if screenshot is not None:
    cv2.imshow("Selected ROI", screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No region selected.")
