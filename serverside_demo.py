import flask
app = flask.Flask(__name__)
count = 0  # don’t actually do this in production
unique_ips = set()  # don’t actually do this in production

@app.route('/')
def show_index():
    """Show homepage."""
    return '''
    Logged in as {}
    <form action="/logout/" method="post">
    <p><input type="submit" value="Logout"></p>
    </form>'''

@app.route('/u/<username>/')
def show_user(username):
    """Show logged user."""
    return "hello {}!".format(username)


@app.route("/visitor/")
def visitor_counter():
    """Show visitor count."""
    global count  # don’t actually do this in production!
    count += 1
    return "<html>"\
        "<body>"\
        f"Hello visitor number {count}!"\
        "</body>"\
        "</html>"


@app.route("/unique/")
def unique_visitor_counter():
    """Show unique visitor counter."""
    global count  # don’t actually do this in production
    global unique_ips  # don’t actually do this in production
    count += 1
    addr = flask.request.remote_addr
    unique_ips.add(addr)
    return "<html>"\
        "<body>"\
        f"Hello visitor number {count} from IP {addr}!<br>"\
        f"{len(unique_ips)} unique IPs seen today."\
        "</body>"\
        "</html>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
