from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model (from the pickle file)
pipe = pickle.load(open('pipe.pkl', 'rb'))

# List of teams and cities
teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 
    'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 
    'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 
    'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 
    'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 
    'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 
    'Christchurch', 'Trinidad'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Getting the form data
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        city = request.form['city']
        current_score = int(request.form['current_score'])
        overs = float(request.form['overs'])
        wickets = int(request.form['wickets'])
        last_five = int(request.form['last_five'])

        # Calculate additional features
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        # Create the input DataFrame (ensure the column names match the model's expected input)
        input_df = pd.DataFrame(
            {'batting_team': [batting_team],
             'bowling_team': [bowling_team],
             'city': [city],
             'current_score': [current_score],
             'balls_left': [balls_left],
             'wicket_left': [wickets_left],
             'current_run_rate': [crr],
             'last_five': [last_five]}
        )

        # Predict the result using the trained model
        result = pipe.predict(input_df)
        prediction = int(result[0])  # Assuming the prediction is a single value

    return render_template('index.html', teams=sorted(teams), cities=sorted(cities), prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
