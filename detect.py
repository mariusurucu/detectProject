from threading import Thread

import cv2


class Detect:
    def __init__(self, face_cascade, frame):
        # initialize the file video stream along with the boolean
        # used to indicate if the thread should be stopped or not
        self.faceCascade = face_cascade
        self.frame = frame
        self.stopped = False

    def start(self):
        # start a thread to read frames from the file video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely
        while True:
            # if the thread indicator variable is set, stop the
            # thread
            if self.stopped:
                return
            # Detect faces in the frame
            faces = self.faceCascade.detectMultiScale(
                self.frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)

            )
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
