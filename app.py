from flask import Flask, request, render_template_string

app = Flask(__name__)

# Store name-description pairs
data = {}

# Password required to add entries
ADMIN_PASSWORD = "townsodasigma272767!@a"

# HTML template with CSS link
template = """
<!doctype html>
<html>
<head>
    <title>Name Lookup</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<h2>Add Name and Description (Password Required)</h2>
<form method="POST" action="/add">
  Name: <input name="name" type="text"><br>
  Description: <input name="description" type="text"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Add">
</form>

<h2>Look Up a Name</h2>
<form method="GET" action="/get">
  Name: <input name="name" type="text">
  <input type="submit" value="Search">
</form>

{% if result %}
  <h3>Result:</h3>
  <p>{{ result }}</p>
{% endif %}

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    password = request.form['password']

    if password != ADMIN_PASSWORD:
        return render_template_string(template, result="❌ Incorrect password. Entry not added.")

    data[name] = description
    return render_template_string(template, result=f"✅ Added: {name} - {description}")

@app.route('/get')
def get():
    name = request.args.get('name')
    description = data.get(name)
    if description:
        result = f"{name}: {description}"
    else:
        result = "❌ Name not found."
    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(debug=True)