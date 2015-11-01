from flask import Flask, render_template, request, redirect
#import requests
#import json
import Quandl

data = Quandl.get("ZILL/Z50010_C", authtoken="_MB77xscFeMTofom3tR8")


data_value = data["Value"]
data_date = data.index.tolist();
data_deriv = list;

first = True;
for item in data_value:
    if first==True:
        temp = item;
        temp_date = data_date.next();
    else:
        data_deriv.append((item-temp)/(data_date.next()-temp_date));    
    
TIME_QUERY = "MOST RECENT";
TIME_LAPSE = "2 YEARS";

        

#api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/stock.json'
#session = requests.Session()
#session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
#raw_data = session.get(api_url)

from bokeh.plotting import figure

plot = figure(title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

from bokeh.embed import components 

plot.line(data_date, data_deriv, color='navy', legend='Open')
script, div = components(plot)

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('graph.html', script=script, div=div)
  
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(port=33507)
