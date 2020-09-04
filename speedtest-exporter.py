#!/usr/bin/env python3

import sys
import json
import subprocess

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    data = speedtest()
    return(data)

def speedtest():
    data = []
    try:
        speedtest = subprocess.Popen('speedtest --json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        results = json.loads(speedtest.communicate()[0].decode('utf-8'))
        labels = 'server_name="{}",server_sponsor="{}",client_ip="{}",client_isp="{}",client_isp_rating="{}"'.format(
            results['server']['name'],
            results['server']['sponsor'],
            results['client']['ip'],
            results['client']['isp'],
            results['client']['isprating']
        )
        data.append('speedtest_download{{{}}} {}'.format(labels, results['download']))
        data.append('speedtest_upload{{{}}} {}'.format(labels, results['upload']))
        data.append('speedtest_ping{{{}}} {}'.format(labels, results['ping']))
        data.append('speedtest_bytes_sent{{{}}} {}'.format(labels, results['bytes_sent']))
        data.append('speedtest_bytes_received{{{}}} {}'.format(labels, results['bytes_received']))
    except Exception as e:
        data.append(e)
    return("\n".join(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10101)
