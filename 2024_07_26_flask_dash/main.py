from flask import Flask, render_template, request
import data

app = Flask(__name__)
@app.route("/")
def index1():
    return render_template("index1.html.jinja")

@app.route("/index1")
def index():
    # 方法1
    # print(list(map(lambda value:value[0], data.get_areas())))

    # 方法2
    select_area = request.args.get('area')
    # 從資料庫取得行政區資料
    areas = [tup[0] for tup in data.get_areas()]
    select_area= '士林區' if select_area is None else select_area
    # 從資料庫取得該行政區所有站點資訊
    detail_snaes = data.get_snaOfArea(area=select_area)

    # areas -> 所有行政區
    # show_area -> 要顯示的行政區
    # detail_snaes -> 該行政區所有站點資訊
    return render_template("index.html.jinja", areas=areas, show_area=select_area, detail_snaes=detail_snaes)

   