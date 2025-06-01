# 🔍 Multi-Feature Object Tracker

A web-based application that allows users to upload a **reference image** and a **target image**, and then visually highlights matched features between them using computer vision algorithms. This app is built with **Flask** on the backend and enhanced with a modern, responsive frontend using **HTML**, **CSS**, and **JavaScript**.

---

## 🚀 Features

- Upload a reference object and a target scene image
- Visualize the detected object through feature matching
- Beautiful and responsive UI with helpful feedback messages

---


## ⚙️ Tech Stack

- **Frontend**: HTML5, CSS3 (modern responsive styling)
- **Backend**: Python Flask
- **Computer Vision**: OpenCV
- **Templating**: Jinja2

---

## 📂 Project Structure

```

object-tracking-app/
│
├── static/
│   └── styles.css               # Custom CSS for styling
│
├── templates/
│   └── index.html               # Main web page
│
├── uploads/                     # Temporary storage for uploaded images
├── utils/
│   └── tracker.py     
├── app.py                       # Flask backend logic
├── requirements.txt             # Python dependencies
└── README.md                    # Project info

````

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/object-tracking-app.git
cd object-tracking-app
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Visit the app**

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 Usage

1. Upload a **reference image** (the object to track).
2. Upload a **target image** (scene where the object might appear).
3. Click `🚀 Track Object` to run feature matching.
4. Results will display:

   * Original and processed image with matched features.
   * Status (object found/not found).
   * Number of total and top matches.

---

## 🧠 How It Works

This app uses **ORB (Oriented FAST and Rotated BRIEF)** or **SIFT/SURF** algorithms from OpenCV to:

* Detect keypoints in both images
* Compute descriptors
* Match descriptors using BFMatcher
* Filter good matches and visualize them

---

## ✅ Future Enhancements

* Add drag-and-drop image upload
* Add support for video frame matching
* Allow users to choose the matching algorithm (ORB, SIFT, AKAZE)
* Download result as image
* Add dark/light theme toggle

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* [OpenCV](https://opencv.org/) for providing robust computer vision tools
* [Flask](https://flask.palletsprojects.com/) for lightweight backend framework
* [Font Awesome / Emoji support](https://emojipedia.org/) for icons and UI enhancement

---

## 🤝 Contributing

Feel free to fork the project and submit a pull request to enhance the UI/UX, add new vision algorithms, or refactor the backend.

## THANK YOU !!

