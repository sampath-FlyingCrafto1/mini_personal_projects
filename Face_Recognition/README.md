# Real-time face detection

This code demonstrates real-time face detection using OpenCV.

## How it works

1. The code imports the OpenCV library (`cv2`).
2. It captures video from the default camera device (`cap = cv2.VideoCapture(0)`)
3. It loads the pre-trained Haar cascade classifiers for face and body detection from OpenCV's data directory (`haarcascade_frontalface_default.xml` and `haarcascade_fullbody.xml`).
4. In a loop, it captures a frame from the video (`_, frame = cap.read()`)
5. It converts the frame from BGR (OpenCV's default color format) to grayscale (`gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`) for better detection results.
6. It detects faces in the grayscale frame using the `face_cascade.detectMultiScale()` function. This function returns a list of rectangles representing the detected faces.
7. It iterates over the detected faces and draws a red rectangle around each face on the original frame (`cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)`)
8. It displays the frame with detected faces in a window named "Camera" (`cv2.imshow("Camera", frame)`)
9. It waits for a key press. If the pressed key is 'q', it breaks out of the loop and terminates the program (`cv2.waitKey(1) == ord('q')`)
10. Finally, it releases the video capture object and destroys all OpenCV windows to clean up resources (`cap.release()` and `cv2.destroyAllWindows()`)

## Requirements

* OpenCV library (`pip install opencv-python`)

## Running the code

1. Save the code as a Python file (e.g., `face_detection.py`)
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using the following command:

```bash
python face_detection.py