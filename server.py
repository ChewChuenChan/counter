from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = 'keey it secret'


#Bonus: display how many times the user has actually visited the page
# as well as the value of the counter
# Session has divided into 3 parts:
# the single times, 
# 2x counter and counter from the form group in one part,
# and the sum of both of them. 
# The single times is the user actual visit the page, 
# while the counter value will be 2x counter + counter from the form.


# Have the root router render a template that displays the number of times the client has visited the site.
# Refresh the page several times to ensure the counter is working
@app.route('/')
def index():
    session['count_plus']=0
    session['sum']=0
    if 'count' in session:
        print('key exists!')
        session['count'] += 1
        session['sum'] =session['count']+ session['count_plus']
    else:
        print("key 'count' does NOT exist")
        session ['count'] = 0
    return render_template("index.html")

# Add a "/destroy-session" route that clears the sessions
# redirects to the root route
@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys
    return redirect('/')

# Bonus: add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/add_2_visits')
def add_2_visits():
    if 'count_plus' in session:
        print('key exists!')
        session['count_plus'] +=2
        session['sum'] =session['count']+ session['count_plus']
    else:
        print("key 'testing' does NOT exist")
        session ['count_plus'] = 0
    return render_template("index.html")


@app.route('/form',methods=['POST'])
def counter_form():
    print("Got form info")
    if 'count_plus' in session:
        print('key exists!')
        session['count_plus'] += (int)(request.form['counter'])
        session['sum'] =session['count']+ session['count_plus']
        
    else:
        print("key 'count_plus' does NOT exist")
        session ['sum'] = 0
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
