import cv2
import os

# Define the labels for image capture
LABELS = ['one', 'two', 'three']  # Labels represent categories for captured images

##### Configuration for image capture #####
# Uncomment the following lines to capture from a video file
# FILE_NAME_OR_WEBCAM_INDEX = 'video.mp4'  # Path to the video file
# DELAY = 0  # Delay for video playback (0 ensures continuous frame capture)

# Uncomment the following lines to capture from a webcam
FILE_NAME_OR_WEBCAM_INDEX = 0  # Webcam index (0 for the default webcam)
DELAY = 1  # Delay in milliseconds (1 for webcam capture)

class ImageCapturer:
    '''
    A class to capture and save images from video or webcam input.
    
    Usage:
    - Press the corresponding label index (0, 1, 2, etc.) to capture and save a frame.
    - Press 'q' to quit the program.
    - Press any other key to skip to the next frame (only when using videos).
    '''

    def __init__(self, labels, file_name_or_webcam_index=0, delay=1, output_folder='Images'):
        # Initialize parameters
        self.labels = labels  # List of labels for categorization
        self.file_name_or_webcam_index = file_name_or_webcam_index  # Input source (file or webcam)
        self.delay = delay  # Delay for frame capture
        self.output_folder = output_folder  # Folder to save captured images
        self.count_per_label = [0 for i in self.labels]  # Counter for images saved per label
        self.cap = cv2.VideoCapture(self.file_name_or_webcam_index)  # Capture object
        os.makedirs(self.output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    def capture(self):
        '''Capture frames from the input source and save them based on key press.'''
        while True:
            _, img = self.cap.read()  # Read a frame from the input
            cv2.imshow('Preview', img)  # Display the frame in a window
            key = cv2.waitKey(self.delay)  # Wait for a key press
            if key == ord('q'):  # Quit if 'q' is pressed
                break
            key = key - 48  # Convert ASCII key code to decimal (0-9)
            if key >= 0 and key < len(self.labels):  # Check if key corresponds to a valid label
                self.saveImage(img, key)  # Save the frame with the selected label
        self.cap.release()  # Release the capture object
        cv2.destroyAllWindows()  # Close all OpenCV windows

    def saveImage(self, img, key):
        '''Save the captured frame with a filename based on the label and counter.'''
        str_label = self.labels[key]  # Get the label string
        str_count = str(self.count_per_label[key]).zfill(3)  # Format counter as 3 digits
        filename = f"{self.output_folder}/{str_label}-{str_count}.jpg"  # Generate filename
        cv2.imwrite(filename, img)  # Save the image to the file
        self.count_per_label[key] += 1  # Increment the counter for the label

if __name__ == '__main__':
    # Create an ImageCapturer object with specified parameters
    imageCapturer = ImageCapturer(labels=LABELS,
                                  file_name_or_webcam_index=FILE_NAME_OR_WEBCAM_INDEX,
                                  delay=DELAY)
    # Start the capture process
    imageCapturer.capture()
