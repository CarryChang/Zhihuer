# coding=utf-
from flask import Flask, jsonify, request,Flask,redirect
from flask_bootstrap import Bootstrap
from flask import render_template
import json
import time
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_pyfile('config.ini')
app.url_map.strict_slashes = False # Disable redirecting on POST method from /star to /star/
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        st = time.clock()
        id = request.form.get('hot_id')
        # id = '318446058'
        if len(str(id)) > 1:
            star = open('data/zhihu.json','r',encoding='utf-8')
            point = []
            c_time = []
            ti = []
            type = []
            rank = []
            s1 = star.readlines()
            for s in s1:
                s = json.loads(s)
                if str(id) in str(s['question_id']) or str(id) in str(s['question_title']):
                    point.append(s['hot_point'])
                    # point.append(s['rank'])
                    c_time.append(s['crawled_time'])
                    rank.append(s['rank'])
                    ti.append(s['question_title'])
                    type.append(s['type'])
                # all_list.append({'time':s['question_title'],'value':s['hot_point']})
                # output.append({'question_title':  s['question_title'], 'hot_point': s['hot_point'],
                #                'rank': s['rank'], 'update_time': s['crawled_time'], 'type': s['type']})
            # 自动转换格式并设置响应头
            # return jsonify({"point_list":point,"time_list":time})
            data = dict({'time': c_time,'point':point,'title':ti,'rank':rank,'type':type})
            print(time.clock() - st)
            return render_template('hot.html',li=data)
    return render_template('index.html')
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
@app.errorhandler(500)
def not_found(error):
    return render_template('404.html')
# @app.route('/contact.html',methods=['GET','POST'])
# def contact():
#     return render_template('contact.html')
if __name__ == '__main__':
    # 使用ipconfig进行调试，http://172.20.10.7:5000/hot_research_api/330354375
    # app.run(host='0.0.0.0',port=5001,debug=True)
    app.run(debug=True,port=5001)