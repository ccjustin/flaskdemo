import flask
app = flask.Flask(__name__)

# FLASK REQUIRES A SECRET KEY 
# session cookies are "signed" so the server can detect tampering
app.secret_key = b'\xf9L\xa4\x04\x824\x17`\x19\x1c\x0f\x87\xf5\xdaM@)|P\x13&\xadd\xff'

@app.route('/')
def show_index():
    # for displaying home page
    # on form submission, hit /login/ url and execute POST method
    if 'username' not in flask.session:
        return '''
        <form action="/login/" method="post">
        <p><input type=text name=username></p>
        <p><input type=submit value=Login></p>
        </form>'''
    else:
        user = flask.session['username']
        return '''
        Logged in as {}
        <form action="/logout/" method="post">
        <p><input type="submit" value="Logout"></p>
        </form>'''.format(user)

# know POST vs GET
@app.route('/login/', methods=['POST'])
def login():
    # handles login requests
    print("DEBUG Login:", flask.request.form['username'])

    # flask session object to store cookies
    flask.session['username'] = flask.request.form['username']

    # using a function that calls the route 
    return flask.redirect(flask.url_for('show_index'))

@app.route('/logout/', methods=['POST'])
def logout():
    # POST-only route for handling logout requests
    print("DEBUG Logout:", flask.session['username'])
    flask.session.clear()
    return flask.redirect(flask.url_for('show_index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
