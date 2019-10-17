"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/game')
def show_madlib_form():

    response = request.args.get("playgame")
    print(response, "\n\n\n\n")
    # name = request.args.get("person")
    # print(name, "\n\n\n\n")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

    # return render_template("goodbye.html",person="name" )

@app.route('/game_madlibs')
def show_madlib_result():

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    place = request.args.get("place")
    return render_template("madlibs.html", person=person, 
                            color=color, noun=noun,place=place)


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
