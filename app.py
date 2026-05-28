from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def portfolio():
    return jsonify({
        "name": "Ezra Mwalongo",
        "title": "Data Scientist",
        "profile": "Passionate about data analytics, ML model deployment, and web development.",
        "skills": [
            "Data Analytics",
            "Database Management",
            "ML Model Deployments using Python",
            "Web Development (HTML, CSS, Python, PHP, JavaScript)"
        ],
        "qualifications": ["BSc Data Science"],
        "projects": [
            {
                "title": "HTML Web Pages Development",
                "description": "Built responsive web pages using HTML, CSS, and JavaScript."
            },
            {
                "title": "Excel and R Data Analysis",
                "description": "Performed statistical analysis and visualization using Excel and R."
            }
        ],
        "contact": {
            "email": "ezramwalongo23@gmail.com",
            "phone": "0654470448",
            "location": "Dar es Salaam, Tanzania"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
