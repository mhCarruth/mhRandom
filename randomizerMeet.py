from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# Define 13 entities
entities = [
    {"title": "Trystan Carruth", "description": "Tech"},
    {"title": "Amber Kochevar", "description": "Ops"},
    {"title": "Chelsea Mason", "description": "Ops"},
    {"title": "Josh Ochoa", "description": "Ops"},
    {"title": "Heather Stevens", "description": "Ops"},
    {"title": "Lauren Sündermann", "description": "Ops"},
    {"title": "Levi Njord", "description": "Tech"},
    {"title": "Marguerite Tuthill", "description": "Ops"},
    {"title": "Myrisa Mitchell", "description": "Tech"},
    {"title": "Quincie Cowell-Armstrong", "description": "Ops"},
    {"title": "Tessa Calloway", "description": "Tech"},
    {"title": "Tuyen Van", "description": "Tech"}
]

@app.route('/')
def index():
    # Pass the `entities` list to the template
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
                overflow: hidden;
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
            .slot-machine-text {
                transition: transform 0.1s ease-in-out;
            }
            .slot-machine-animation {
                animation: slotMachineSpin 1.5s infinite;
            }
            @keyframes slotMachineSpin {
                0% {
                    transform: translateY(0);
                }
                25% {
                    transform: translateY(-40px);
                }
                50% {
                    transform: translateY(40px);
                }
                75% {
                    transform: translateY(-40px);
                }
                100% {
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Random Person</h1>
            <div class="selection-area">
                <div class="slot-machine">
                    <p id="random-title" class="slot-machine-text">Press "Randomize" to select a person</p>
                    <p id="random-description" class="description"></p>
                </div>
            </div>
            <button id="randomize-button">Randomize</button>
        </div>

        <!-- Include canvas-confetti library -->
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti"></script>

        <script>
            // Pass the `entities` list from Python to JavaScript
            const entities = {{ entities | tojson }};

            const button = document.getElementById("randomize-button");
            const titleElement = document.getElementById("random-title");
            const descriptionElement = document.getElementById("random-description");

            button.addEventListener("click", () => {
                titleElement.textContent = "Randomizing...";
                descriptionElement.textContent = "";

                // Add animation for slot machine effect
                titleElement.classList.add("slot-machine-animation");

                // Simulate slot machine effect with random names
                let count = 0;
                const interval = setInterval(() => {
                    titleElement.textContent = getRandomName();
                    count++;

                    if (count > 20) {
                        clearInterval(interval);

                        // Fetch the final random person after the animation
                        fetch('/randomize')
                            .then(response => response.json())
                            .then(data => {
                                titleElement.classList.remove("slot-machine-animation");
                                titleElement.textContent = data.title;
                                descriptionElement.textContent = data.description;

                                // Trigger confetti after the person is chosen
                                triggerConfetti();
                            });
                    }
                }, 100); // Update the name every 100ms
            });

            function getRandomName() {
                const randomIndex = Math.floor(Math.random() * entities.length);
                return entities[randomIndex].title;
            }

            function triggerConfetti() {
                // Trigger confetti effect using the canvas-confetti library
                confetti({
                    particleCount: 200,
                    spread: 70,
                    origin: { x: 0.5, y: 0.5 },
                    colors: ['#ff0000', '#00ff00', '#0000ff', '#ffcc00']
                });
            }
        </script>
    </body>
    </html>
    """ , entities=entities)

@app.route('/randomize', methods=['GET'])
def randomize():
    selected_entity = random.choice(entities)
    return jsonify(selected_entity)

if __name__ == '__main__':
    app.run(debug=True)

