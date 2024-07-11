from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def index():
    # 方法1
    # print(list(map(lambda value:value[0], data.get_areas())))
    # 方法2
    areas = [tup[0] for tup in data.get_areas()]
    print(areas)
    return render_template("index.html.jinja", areas=areas)