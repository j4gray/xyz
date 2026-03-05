from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/almanac")
def almanac():
    return render_template('almanac.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/posts")
def posts():
	return render_template('posts/posts.html')

@app.route("/posts/<post_html_file>")
def posts_html(post_html_file):
	return render_template('posts/'+post_html_file)


@app.route("/projects")
def projects():
	return render_template('projects/projects.html')

@app.route("/projects/<project_html_file>")
def projects_html(project_html_file):
	return render_template('projects/'+project_html_file)

if __name__ == "__main__":
    app.run(debug=False)