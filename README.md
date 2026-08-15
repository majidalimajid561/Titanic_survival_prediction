# 🚢 Titanic Survival Prediction Web App

A **Flask-based machine learning web application** that predicts whether a passenger survived the Titanic disaster. Users input passenger details (class, sex, age, fare, embarkation port, and family size), and the app returns a real-time prediction with a confidence score.

 <!-- Replace with your actual screenshot path -->

---

## 📊 Live Demo

> **Live URL**: [https://your-app-name.onrender.com](https://your-app-name.onrender.com)  
> *(Update this link with your actual Render/PythonAnywhere URL after deployment)*

---

## 📝 Table of Contents

- [🚢 Titanic Survival Prediction Web App](#-titanic-survival-prediction-web-app)
- [📊 Live Demo](#-live-demo)
- [📝 Table of Contents](#-table-of-contents)
- [📖 About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [📁 Dataset](#-dataset)
- [🤖 Model Performance](#-model-performance)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started (Local Setup)](#-getting-started-local-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## 📖 About The Project

This project was built as a **portfolio-grade machine learning product**. It bridges the gap between a Jupyter Notebook model and a fully functional, deployable web application. 

The core predictive model is trained on the famous Kaggle Titanic dataset. The web interface is built using **Flask** and serves HTML templates with a clean, responsive UI.

---

## ✨ Key Features

- **User-Friendly Interface**: Clean, professional UI with input validation.
- **Instant Predictions**: Real-time inference using a pre-trained Scikit-learn pipeline.
- **Confidence Score**: Shows the model's probability for the predicted outcome.
- **Comprehensive Validation**: Handles missing, incorrect, or out-of-range inputs gracefully.
- **Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices.

**Features Used:**
| Feature | Description |
| :--- | :--- |
| `Pclass` | Passenger Class (1st, 2nd, or 3rd) |
| `Sex` | Gender (male or female) |
| `Age` | Age in years |
| `Fare` | Ticket fare in GBP |
| `Embarked` | Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |
| `family_size` | Total number of siblings, spouses, parents, and children aboard |


## 🛠️ Tech Stack

**Backend**
- Python 3.10+
- Flask
- Scikit-learn
- Pandas & NumPy

**Frontend**
- HTML5
- CSS3 (Vanilla, responsive design)



## 📂 Project Structure
titanic_survival_projection/
│
├── flask_app/
│   ├── app.py
│   └── templates/
│       ├── home.html
│       └── result.html
├── data/                       
│   └── train.csv 
├── notebook/                       
│   └── model_code.ipynb
├── models/                       
│   └── titanic_pipeline.pkl      
│
├──Streamlit_app/
│        └── Script.py
├── requirements.txt              
└── .gitignore   


## 🚀 Getting Started (Local Setup)


### Installation

1. **Clone the repository** (or download the ZIP):
   ```bash
   git clone https://github.com/your-username/titanic-predictor.git
   cd titanic-predictor
   
2.**Create a virtual environment** 
python -m venv venv
source venv/bin/activate
3.**Install the dependencies**:
pip install -r requirements.txt

👨‍💻 Author
Majid Mehmood
