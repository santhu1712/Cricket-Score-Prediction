# Cricket Score Predictor 

This is a machine learning-based web application built with **Flask** that predicts the final score of a cricket match based on various match-related inputs. The model uses **Random Forest Regression** to make predictions, and the web application allows users to input details such as the batting team, bowling team, current score, overs, wickets, and runs scored in the last 5 overs to predict the final score.

## Key Features

- **Machine Learning Model**: A **Random Forest Regression** model is used to predict the final score based on historical data.
- **User Input Interface**: Users can enter details about the match, including the batting and bowling teams, current score, overs, wickets, and runs scored in the last 5 overs.
- **Web Interface**: Built with Flask for backend, HTML, and Bootstrap for frontend to provide a simple and interactive user experience.
- **Prediction**: The model predicts the final score based on the provided match data.

## Technologies Used

- **Flask**: Lightweight web framework for Python.
- **scikit-learn**: Machine learning library used for training the Random Forest Regression model.
- **pandas**: For handling and manipulating data.
- **Pickle**: For serializing the trained machine learning model and loading it into the app.
- **HTML/CSS**: For creating the frontend interface.
- **Bootstrap**: For making the app responsive and visually appealing.

## Model Description

### Features:
- **batting_team**: The team currently batting.
- **bowling_team**: The team currently bowling.
- **city**: The city where the match is played.
- **current_score**: The current score of the batting team.
- **balls_left**: Number of balls remaining in the innings.
- **wickets_left**: Number of wickets remaining for the batting team.
- **current_run_rate**: The current run rate of the batting team.
- **last_five**: Runs scored by the batting team in the last 5 overs.

### Model:
The machine learning model used in this project is a **Random Forest Regression** model trained to predict the final score of the batting team based on the input features mentioned above.

The trained model is saved using **Pickle** for easy loading in the Flask application.

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/cricket-score-predictor.git
cd cricket-score-predictor
```

### Step 2: Create and Activate a Virtual Environment
- For **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- For **Mac/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add the Trained Model
To use the application, you need the trained machine learning model. If you don’t have the pre-trained model (`pipe.pkl`), follow the **Model Training** section below to train the model, or download the model and place it in the root directory of the project.

### Step 5: Run the Flask Application
```bash
python app.py
```

After running the app, open your browser and visit `http://127.0.0.1:5000/` to interact with the application and make predictions.

## Model Training

If you don’t have the trained model, you can train it using the following steps:

1. Collect and prepare the dataset for training, ensuring it contains the match data with features like batting team, bowling team, current score, etc.
2. Use **Random Forest Regression** from **scikit-learn** to train the model:

## How to Use the Web Application

1. **Select Batting Team**: Choose the team currently batting from the dropdown menu.
2. **Select Bowling Team**: Choose the team currently bowling.
3. **Select City**: Choose the city where the match is taking place.
4. **Enter Current Score**: Enter the score of the batting team at the moment.
5. **Enter Overs**: Provide the number of overs completed.
6. **Enter Wickets**: Enter the number of wickets the batting team has lost.
7. **Enter Runs in Last 5 Overs**: Provide the runs scored in the last 5 overs.

After submitting the form, the app will display the predicted final score of the batting team based on the entered data.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, make your changes, and submit a pull request.
