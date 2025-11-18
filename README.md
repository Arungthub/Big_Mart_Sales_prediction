# Big_Mart_Sales_prediction

Big Mart Sales Prediction – Web Application

A machine learning-powered web application built using Flask, designed to predict retail item sales based on various product and outlet attributes.
This project integrates data visualization, interactive dataset previews, and model performance metrics — making it a complete end-to-end machine learning deployment example.

Project Overview

This project demonstrates how to deploy a Sales Prediction Model as a web application using Flask.

Users can:

1. Upload a dataset (Train.csv)
2. Preview dataset contents directly in the browser
3. Visualize basic insights such as sales charts
4. Select specific attributes (e.g., Fat Content, Item Type, Outlet Type, etc.)
5. Predict the expected sales value
6. View accuracy and precision metrics with chart visualizations
7. The system also includes user authentication (Register/Login) and securely stores     credentials using bcrypt hashing in an SQLite database.

Key Features

1. User Authentication – Secure registration and login functionality with password encryption
2. Dataset Upload – Upload and preview CSV datasets directly in the web interface
3. Data Visualization – Generate charts using Matplotlib for basic dataset insights
4. Prediction System – Choose input features via dropdowns to generate predicted sales outputs
5. Model Performance – Displays model accuracy and precision with bar chart visualization
6. Clean User Flow – Smooth workflow from Upload → Preview → Predict → Results
7. Database Integration – SQLite used for credential storage and management
8. Modular Code Design – Organized Flask routes, ML logic, and utility scripts

Project Structure

Big_Mart_Sales_Project
│
├── app.py                # Main Flask application
├── model.py              # Model performance and prediction logic
├── utils.py              # Helper functions for preview and visualization
│
├── templates/            # HTML templates (Jinja2)
│   ├── login.html
│   ├── register.html
│   ├── upload.html
│   ├── preview.html
│   └── result.html
│
├── static/               # Optional: CSS, JS, images
├── uploads/              # Uploaded files (auto-created)
│
├── salesdb.sqlite        # SQLite database (auto-created)
├── Train.csv             # Sample training dataset (local use only)
├── requirements.txt      # Python dependencies
├── .gitignore            # Files ignored in version control
└── README.md             # Project documentation


Setup and Run Instructions

Follow these steps to set up and run the project locally:

1. Open the repository.
2. Click on Codespaces.
3. In your local environment, open the Codespace create a new codespace , or open the folder in VS Code.
4. Install the dependencies listed in requirements.txt.

Terminal Commands

cd Big_Mart_Sales_Project     # Navigate to the project folder
pip install -r requirements.txt   # Install required dependencies
python app.py                     # Run the application

After running the above commands, a local web address will appear in the terminal.
Press Ctrl + Click on the address to open the web application in your browser.

Application Workflow

1. Login / Register Page – New users can register and then log in securely.
2. Upload Page – Upload the Test.csv file (ensure it is saved successfully).
4. Preview Page – Displays a sample of the dataset and a bar chart showing the top 5 items by category.
5. Prediction Section – Choose conditions from four dropdown menus to predict sales.
6. Result Page – Displays the predicted sales value along with accuracy and precision charts for the model.

Technologies Used

Python 3.x
Flask
Pandas, NumPy
Scikit-learn
Matplotlib
SQLite
bcrypt
HTML, CSS (Jinja2 Templates)


Acknowledgment

This project was developed as part of an Undergraduate (UG) academic project by a team of three members.
It represents our collaborative effort to apply machine learning and web development techniques in a real-world scenario of retail sales prediction.

Team Members:
1. Arun Kumar T
2. Lakshman Reddy 
3. Nandha Vardhan K
