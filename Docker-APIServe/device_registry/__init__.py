from flask import Flask
import os
import markdown

app = Flask(__name__)


@app.route("/")
def index():
	"""Present some documentation"""
	# Open README file
	with open(os.path.dirname(app.root_path)+ "/README.md", "r") as markdown_file:
		content=markdown_file.read()
		return markdown.markdown(content)