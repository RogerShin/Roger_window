from flask import Flask, render_template, request
import data

app = Flask(__name__)

@app.route("/")
def index():
    # 方法1
    # print(list(map(lambda value:value[0], data.get_areas())))
    
    # 方法2
    select_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    if select_area is None:
        print("第一次進入")
        return render_template("index.html.jinja", areas=areas)
    else:
        print(select_area)
        return render_template("index.html.jinja", areas=areas)

   