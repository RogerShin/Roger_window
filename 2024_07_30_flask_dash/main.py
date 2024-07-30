from flask import Flask, render_template, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dashboard.board1 import app1
from dashboard.board2 import app2
import data
from auth.main import auth_blueprint

app = Flask(__name__)
app.register_blueprint(auth_blueprint)

application = DispatcherMiddleware(app, {
    "/dashboard/app1": app1.server,
    "/dashboard/app2": app2.server
})

@app.route("/")
def index():
    return render_template("index.html.jinja")

@app.route("/index1")
def index1():
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
    return render_template("index1.html.jinja", areas=areas, show_area=select_area, detail_snaes=detail_snaes)

@app.errorhandler(404)
def page_not_found(error):
    return "<h2>沒有此頁面</h2>", 404

if __name__ == "__main__":
    run_simple("localhost", 8080, application, use_debugger=True, use_reloader=True)   