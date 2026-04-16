import cv2
import pickle
import numpy as np
import os

if not os.path.exists('data/'):
    os.makedirs('data/')

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_data = []

i = 0
name = input("Enter your voter id number: ")  # Assuming input for name or identifier
framesTotal = 50
captureAfterFrame = 2



while True:
    ret, frame = video.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data) < framesTotal and i % captureAfterFrame == 0:
            faces_data.append(resized_img.flatten())  # Flattening before appending
        i += 1
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) >= framesTotal:
        break

video.release()
cv2.destroyAllWindows()

# Convert faces_data to numpy array and reshape
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape((len(faces_data), -1))

# Save or update names.pkl and faces_data.pkl
if 'names.pkl' not in os.listdir('data/'):
    names = [name] * len(faces_data)
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names += [name] * len(faces_data)
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        existing_faces = pickle.load(f)
    
    # Ensure shapes match before concatenation
    if existing_faces.shape[1] != faces_data.shape[1]:
        # If shapes don't match, resize or preprocess faces_data to match existing_faces
        faces_data = np.resize(faces_data, existing_faces.shape)  # Resize to match existing_faces shape
    
    # Now concatenate
    faces_data = np.append(existing_faces, faces_data, axis=0)
    
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
