import os
import time
import logging
import cv2
import datetime
import numpy as np
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Set up file paths to monitor
file_paths = ["C:\\Users\\ADMIN\\Desktop\\test folder"]

# Set up OpenCV camera
camera = cv2.VideoCapture(0)

# Define a function to capture a photo of the person making the changes
def capture_photo():
    ret, frame = camera.read()
    if ret:
        photo_path = f"C:\\Users\\ADMIN\\Desktop\\thief photo"
        cv2.imwrite(photo_path, frame)

# Define a class to handle file system events
class FileEventHandler(LoggingEventHandler):
    def on_modified(self, event):
        # Call the parent method to log the event
        super().on_modified(event)
        # Capture a photo of the person making the changes
        capture_photo()

# Set up the Watchdog observer
observer = Observer()
event_handler = FileEventHandler()
for file_path in file_paths:
    observer.schedule(event_handler, path=file_path, recursive=False)

# Start the observer
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# Release the camera
camera.release()
cv2.destroyAllWindows()
