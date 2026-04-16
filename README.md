# 🗳️ Smart Voting System using Facial Recognition

## 📌 Overview
This project is a secure online voting system that uses facial recognition and multi-level authentication to ensure that only authorized users can cast their votes. It enhances the traditional voting process by improving security, accuracy, and accessibility.

## 🚀 Features
- 🔐 Three-level authentication (UID, Voter ID, Face Recognition)
- 👤 Real-time face detection using OpenCV
- 🧠 Machine Learning-based face recognition (KNN, Eigenfaces, CNN concepts)
- 📩 OTP-based verification for added security
- 🗳️ One-person-one-vote enforcement
- 📊 Automatic vote counting and result generation

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy, Pandas
- Scikit-learn (KNN)
- Flask / Django (for web interface)
- SQLite / MySQL

## ⚙️ How It Works
1. User registers with personal details and facial data
2. System stores face data in database
3. During voting:
   - UID verification
   - Voter ID verification
   - Face recognition matching
4. OTP is generated for final authentication
5. User casts vote securely
6. Votes are stored and counted automatically

## 📂 Project Structure
├── add_faces.py # Capture and store face data
├── give_vote.py # Face recognition and voting system
├── data/ # Stored face data
├── Votes.csv # Voting records
├── background.png # UI background

## 📈 Results
- Achieved ~90% accuracy in face recognition
- Prevented duplicate voting effectively
- Improved security compared to traditional systems

## 🔮 Future Enhancements
- Integrate Blockchain for secure vote storage
- Deploy on cloud for large-scale usage
- Improve accuracy using deep learning models

## 📌 Conclusion
This system provides a secure and efficient alternative to traditional voting by combining machine learning and biometric authentication.
