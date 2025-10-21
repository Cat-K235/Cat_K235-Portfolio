from flask import Flask, render_template, url_for

app = Flask(__name__)

PERSON = {
    "name": "Mirali",  # <-- write your name
    "title": "Full-Stack Developer | Designer | Creator",  # <-- change this
    "bio": "I got into coding two years ago and I'm still learning to make lots of different stuff.",  # <-- edit this
    "socials": [
        {"label": "GitHub", "url": "https://github.com/Cat-K235"},
    ]
}

# Your projects — add more here
PROJECTS = [
    {
        "id": "p1",
        "title": "Simple Game in Pygame",
        "description": "A simple game where you run from enemies built in Pygame.",
        "image": None,  # example: "images/p1.png"
        "link": "https://github.com/Cat_K235/Escape-Enemies-Game-Pygame"
    },
    {
        "id": "p2",
        "title": "Recipe Website",
        "description": "A website where you can see the recipe for different foods made in Flask.",
        "image": None,
        "link": "https://github.com/Cat-K235/Recipe-Website"
    },
    {
        "id": "p3",
        "title": "Flask Magic 8-Ball",
        "description": "Magic 8-Ball made in Flask",
        "image": None,
        "link": "https://github.com/Cat-K235/8-Ball-Flask"
    },
]


@app.route('/')
def index():
    return render_template('index.html', person=PERSON, projects=PROJECTS)


@app.route('/project/<project_id>')
def project(project_id):
    proj = next((p for p in PROJECTS if p['id'] == project_id), None)
    if not proj:
        return render_template('index.html', person=PERSON, projects=PROJECTS)
    return render_template('project.html', person=PERSON, project=proj)


if __name__ == '__main__':
    app.run(debug=True)
