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
    
    select_area= '士林區' if select_area is None else select_area
        
    return render_template("index.html.jinja", areas=areas, show_area=select_area)

   