## 🔐 File Integrity Monitor with Intruder Capture (Python)

A security-focused file monitoring system that watches sensitive directories for unauthorized changes and captures a **photo of the user** attempting the modification. This project offers a lightweight but effective solution for file integrity monitoring, insider threat detection, and forensic evidence collection using Python, Watchdog, and OpenCV.

---

## 🎯 Project Purpose

This project aims to **monitor sensitive file directories in real-time**, log any unauthorized file modifications, and **capture photographic evidence** of the person attempting the access. It's designed for personal systems, research labs, or internal networks where file protection and accountability are critical.

---

## 🚀 Features

- 🕵️ **Monitors selected file or folder paths in real-time**  
- 🔄 **Logs all file modification events with timestamps**  
- 📸 **Captures an image of the person using webcam** upon modification  
- 💾 **Stores photo evidence locally for forensic use**  
- 🧠 **Simple, efficient, and lightweight script using Python**  
- 📍 **Ideal for tracking tampering attempts in restricted areas**

---

## 🛠 Technologies Used

- **Python** – Core language for monitoring logic  
- **OpenCV** – Captures webcam snapshots for evidence  
- **Watchdog** – File system observation and event handling  
- **Logging** – Built-in Python module for real-time event logging  
- **NumPy** – Required for OpenCV image array processing

---

## ⚙️ How It Works

1. **Directory Watcher**: The user sets target directories to monitor.
2. **Event Trigger**: When a file is modified, an event is raised by Watchdog.
3. **Photo Capture**: The system immediately activates the webcam and captures the user's image.
4. **Logging**: A detailed timestamped log entry is created, and the photo is saved locally.

---

## 🗂 Project Structure

```
file-integrity-monitor/
│
├── fim_capture.py         --> Main script with monitoring + camera logic
├── thief photo/           --> Folder where intruder images are stored
├── test folder/           --> Directory being monitored
├── README.md              --> Project documentation
```

---

## 💻 Installation

```bash
# Clone the repository
git clone https://github.com/AkhilSharmaCyber/File-Integrity-Monitor.git

# Navigate into the project directory
cd file-integrity-monitor

# Install required libraries
pip install opencv-python watchdog numpy
```

---

## ▶️ Usage

Update the paths in the script (`fim_capture.py`) to match:

```python
file_paths = "C:\\Users\\ADMIN\\Desktop\\test folder"
photo_path = "C:\\Users\\ADMIN\\Desktop\\thief photo"
```

Then, run the script:

```bash
python fim_capture.py
```

To stop monitoring, press `Ctrl + C`.

---

## ✅ Results

- 🟢 Successfully detects file modifications
- 📸 Captures intruder images instantly
- 📄 Stores logs and photos in defined local paths
- 🔐 Adds an extra layer of **physical accountability** to file protection

---

## 🔮 Future Improvements

- 🔐 Encrypt and timestamp captured images for secure logging  
- 🌐 Add email/Telegram alert system when intruder is detected  
- 📊 Integrate SQLite or NoSQL DB for scalable log storage  
- 🧠 Add facial recognition to match known user profiles  
- ☁️ Push alerts or photos to the cloud for off-site backup  

---

## 🧪 Sample Log Output

```
2025-04-17 16:20:04 - File modified: test folder\secret.txt
2025-04-17 16:20:04 - Intruder photo saved as: thief photo\intruder_20250417_162004.jpg
```

---

## 👤 Author

**Akhil Sharma** – Cybersecurity & AI Enthusiast  
📎 [LinkedIn](https://linkedin.com/in/akhilsharma91328243)

---

Let me know if you'd like help turning this into a **GUI app**, building an **executable**, or **adding encryption/photo hashing** next!
