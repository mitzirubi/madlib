from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    play_game = request.args.get("yesno")
    if play_game == 'Yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    name=request.args.get("name")
    color=request.args.get("color")
    adjective=request.args.get("adjective")
    noun=request.args.get("noun")
    adjective4=request.args.get("adjective4") 
    print adjective4
    verb_ed=request.args.get("verb_ed")
    noun_p=request.args.get("noun_p")
    liquid=request.args.get("liquid")
    noun_p2=request.args.get("noun_p2")
    famous=request.args.get("famous")
    place=request.args.get("place")
    adjective2=request.args.get("adjective2")
    noun2=request.args.get("noun2")
    nationality=request.args.get("nationality")
    f_celebrity=request.args.get("f_celebrity")
    noun_p3=request.args.get("noun_p3")
    number=request.args.get("number")
    adjective3=request.args.get("adjective3")

    return render_template("madlib.html", adjective4=adjective4,verb_ed=verb_ed, 
        noun_p=noun_p, liquid=liquid, noun_p2=noun_p2, famous=famous, place=place, adjective2=adjective2,
        noun2=noun2, nationality=nationality, f_celebrity=f_celebrity, noun_p3=noun_p3, number=number,
        adjective3=adjective3)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
