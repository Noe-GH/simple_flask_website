# To load a new template, you have to create the corresponding HTML file and save it in the 'templates' directory.
# Then, you create here a function with the corresponding @page.route() decorator stating the url pattern. Remember, the function has to return a render_template()
# object in order to show the template.

# Usually, the website is shown on 127.0.0.1:5000, so you can copy and paste that port information into your browser after you run the script to see the website running.

from flask import Flask, render_template

page=Flask(__name__)

@page.route("/")
def home():
    return render_template("home.html")

@page.route("/pag1/")
def pag1():
    return render_template("pag1.html")

if __name__ == "__main__":
    page.run(debug=True)
