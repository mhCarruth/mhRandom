from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# Define 13 entities
entities = [
    {"title": "Trystan Carruth", "description": "Tech"},
    {"title": "Amber Kochevar", "description": "Ops"},
    {"title": "Amy Kendall", "description": "Tech"},
    {"title": "Chelsea Mason", "description": "Ops"},
    {"title": "Heather Stevens", "description": "Ops"},
    {"title": "Kim Rowe", "description": "Ops"},
    {"title": "Lauren Sündermann", "description": "Ops"},
    {"title": "Levi Njord", "description": "Tech"},
    {"title": "Marguerite Tuthill", "description": "Ops"},
    {"title": "Myrisa Mitchell", "description": "Tech"},
    {"title": "Quincie Cowell-Armstrong", "description": "Ops"},
    {"title": "Tessa Calloway", "description": "Tech"},
    {"title": "Tuyen Van", "description": "Ops"}
]

@app.route('/')
def index():
    # HTML, CSS, and JavaScript all within the render_template_string
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Person</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 2em;
                margin-bottom: 20px;
            }
            .selection-area {
                margin-bottom: 20px;
            }
            .slot-machine {
                font-size: 1.5em;
                font-weight: bold;
                height: 100px;
                margin: 20px 0;
                background-color: #efefef;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border-radius: 8px;
                padding: 10px;
                transition: background-color 0.3s ease;
            }
            .description {
                margin-top: 10px;
                font-size: 1em;
                color: #555;
            }
            button {
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                font-size: 1em;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Random Person</h1>
            <div class="selection-area">
                <div class="slot-machine">
                    <p id="random-title">Press "Randomize" to select a person</p>
                    <p id="random-description" class="description"></p>
                </div>
            </div>
            <button id="randomize-button">Randomize</button>
        </div>

        <script>
            const button = document.getElementById("randomize-button");
            const titleElement = document.getElementById("random-title");
            const descriptionElement = document.getElementById("random-description");

            button.addEventListener("click", () => {
                titleElement.textContent = "Randomizing...";
                descriptionElement.textContent = "";

                // Add some animation for slot machine effect
                setTimeout(() => {
                    fetch('/randomize')
                        .then(response => response.json())
                        .then(data => {
                            titleElement.textContent = data.title;
                            descriptionElement.textContent = data.description;
                        });
                }, 1000); // Delay for slot machine effect
            });
        </script>
    </body>
    </html>
    """)

@app.route('/randomize', methods=['GET'])
def randomize():
    selected_entity = random.choice(entities)
    return jsonify(selected_entity)

if __name__ == '__main__':
    app.run(debug=True)
