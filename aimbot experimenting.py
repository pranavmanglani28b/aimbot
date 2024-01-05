import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time

time.sleep(10)

def detect_red(image):
    # Convert the image from BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a mask for the red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if contours are found
    if contours:
        # Get the coordinates of the contour with the maximum area (assumed to be the red object)
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        return (x + w // 2, y + h // 2)  # Return the center coordinates

    return None  # Return None if no red color is detected

def main():
    while True:
        # Capture the screen
        screenshot = np.array(ImageGrab.grab())

        # Detect red color and get coordinates
        red_coordinates = detect_red(screenshot)

        if red_coordinates:
            print("Red color detected at coordinates:", red_coordinates)

            # Move the mouse to the detected coordinates
            pyautogui.moveTo(red_coordinates[0], red_coordinates[1])

            # Hold the left mouse button
            pyautogui.mouseDown(button='left')
            
            # Sleep to hold the click for a certain duration (adjust as needed)
            time.sleep(1)

            # Release the left mouse button
            pyautogui.mouseUp(button='left')

if __name__ == "__main__":
    main()
