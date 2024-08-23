from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to render the main portfolio page
@app.route('/')
def home():
    return render_template('index.html')

# API route to fetch project data
@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = [
        {"title": "Diabetes Prediction Web App", "description": "A web app using Streamlit to predict diabetes based on user input data."},
        {"title": "Machine Learning Model for XYZ", "description": "An ML model built using Python and scikit-learn to solve a complex problem."}
    ]
    return jsonify(projects)

# Route to handle contact form submissions
@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Process the form data (e.g., save to a database or send an email)
    print(f"Received message from {name} ({email}): {message}")
    
    # Respond with a success message
    return jsonify({"status": "success", "message": "Thank you for your message!"})

if __name__ == '__main__':
    app.run(debug=True)