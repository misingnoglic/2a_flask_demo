# To run this file:
# 1. Make sure flask is installed. If it's not, do "pip install flask"
# 2. Run "python flask_intro.py" when in the correct folder

from flask import Flask
from flask import render_template

# Creates the app
app = Flask(__name__)

# The first function we wrote, no arguments
@app.route('/') # Routes this function to the homepage
def hello_world():
    return 'Hello World!'
	
# Takes <name> as an argument in the URL	
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello '+ name + '!'
	
# Regular function
# Takes a number, and returns a list of its factors
def factors(n):
	answer = [ ]
	for i in range(1,n+1):
		# if i is divisible into n, add it to the list
		if n%i == 0: answer.append(i)
	return answer

# first function for displaying the factors
# this one doesn't use HTML, just converts the list into a string
@app.route('/factors_raw/<n>')
def factors_display_raw(n):
	# n is a string, so we have to convert it into an int
	# before passing it into factors()
	factors_list = factors(int(n))
	return "The factors of "+n+" are: "+str(factors_list)
	
# Our second version, using HTML to make it look nicer
@app.route('/factors_raw_html/<n>')
def factors_display_raw_html(n):
	factors_list = factors(int(n))
	# First we put the stuff at the top, adding "n" in there
	html = "<body> The factors of "+n+" are"+"\n"+"<ul>"
	
	# for each factor, we make a <li> item for it
	for f in factors_list:
		html += "<li>"+str(f)+"</li>"+"\n"
	html += "</ul> </body>" # the close tags at the bottom
	return html

# Final version, using the template at templates/factors.html
@app.route('/factors/<n>')
def factors_display(n):
	factors_list = factors(int(n))
	return render_template(
		"factors.html",
		number=n, # passes the value 'n' as the variable "number" in the template
		factors=factors_list # passes value of "factors_list" as variable "factors" in template
	)

# run the app
if __name__ == '__main__':
    app.run()