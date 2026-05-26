from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "name": "Ezra Mwalongo",
        "title": "Data Scientist",
        "skills": [
            "Data Analytics",
            "Database Management",
            "ML Model Deployments using Python",
            "Web Development (HTML, CSS, Python, PHP, JavaScript)"
        ],
        "qualifications": "BSc Data Science",
        "contacts": {
            "email": "ezramwalongo23@gmail.com",
            "phone": "0654470448"
        },
        "projects": [
            "HTML Web Pages Development",
            "Excel and R Data Analysis"
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
