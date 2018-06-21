 app.py 489 Bytes →  Cloud User Cloud User 提交于 2小时前 . change redis host to actuall hostname
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
import os
from flask import Flask 
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
  count = redis.incr('hits')
  result = "<h1>node:" + os.environ.get('HOSTNAME') + "</h1><p>"
  result = result + "<br>该页面已被访问<span style='color:red;font-size:24px;'>" + str(count) + "</span>次"
  return result

if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True)
