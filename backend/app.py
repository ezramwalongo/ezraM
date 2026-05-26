
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to EzraM Backend!",
        "skills": [
            "Data Science",
            "Data Analysis",
            "Data Management"
        ]
    })

# Example: Data analysis endpoint
@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    """
    Accepts JSON data, performs basic analysis, and returns summary stats.
    Example input:
    {
        "data": [
            {"value": 10},
            {"value": 20},
            {"value": 30}
        ]
    }
    """
    input_data = request.get_json()
    df = pd.DataFrame(input_data["data"])
    
    # Perform simple analysis
    summary = {
        "count": int(df["value"].count()),
        "mean": float(df["value"].mean()),
        "min": float(df["value"].min()),
        "max": float(df["value"].max())
    }
    
    return jsonify({"analysis": summary})

# Example: Data management endpoint
@app.route('/api/store', methods=['POST'])
def store_data():
    """
    Pretend to store data (in real case, connect to DB).
    """
    input_data = request.get_json()
    # Here you’d normally insert into a database
    return jsonify({"status": "success", "stored_records": len(input_data["data"])})

if __name__ == '__main__':
    app.run(debug=True)
