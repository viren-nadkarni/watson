#!/usr/bin/env python
import requests
import json
import operator
import pickle
import thread
import Quandl

from lxml import html
from flask import *
import xml.etree.ElementTree as ET
from flask.ext.cors import CORS

from sandp_100 import constituent_list
from Insights import personality_insights
from StockAnalyzer import stock_analyzer


app = Flask(__name__)
CORS(app)
app.debug = True

__author__ = 'viren'
__version__ = '0.1'

quandl_api_key = 'sD8AYTmp-6WBT86TUPmE'
watson_username = '427d0334-7d24-4d15-9288-a92c3b89a390'
watson_password = 'mwDxdhxiex'
tradeoff_username = 'e388ab69-d331-4dee-9290-cc670ae809d9'
tradeoff_password = 'aN4vqbv3QM3U'
risk_threshold = 0.005

all_stock_list = constituent_list
twitter_handle = ''
index = dict()
watchlist = []


class Scrip:
    def __init__(self, name, symbol, turnover, quantity):
        self.name = name
        self.symbol = symbol
        self.turnover = turnover
        self.quantity = quantity
        self.buzz_factor = None
        self.buzz = None

#############################

def update_cache():
    print ' * getting data'

    for scrip in all_stock_list.keys():
        try:
            data = Quandl.get('WIKI/' + scrip, authtoken=quandl_api_key)
        except Exception as e:
            print ' * data fetch for', scrip, 'failed:', e.message

        symbol = scrip
        name = all_stock_list[scrip]
#        quantity = int(data["Total Trade Quantity"][-1])
        quantity = int(data["Volume"][-1])
#        turnover = int(data["Turnover (Lacs)"][-1])

        index[scrip] = Scrip(name=name,
                            symbol=symbol,
                            turnover=-1,
                            quantity=quantity)

        try:
            short_term_gain = 100* (data["Close"][-1] - data["Close"][-300])/data["Close"][-300]
            index[scrip].short_term_gain = short_term_gain
        except:
            print ' * short term gain calc for', scrip, 'failed: insufficient data'
        try:
            mid_term_gain = 100* (data["Close"][-1] - data["Close"][-1500])/data["Close"][-1500]
            index[scrip].mid_term_gain = mid_term_gain
        except:
            print ' * mid term gain calc for', scrip, 'failed: insufficient data'
        try:
            long_term_gain = 100* (data["Close"][-1] - data["Close"][-3000])/data["Close"][-3000]
            index[scrip].long_term_gain = long_term_gain
        except:
            print ' * long term gain calc for', scrip, 'failed: insufficient data'

        index[scrip].buzz, index[scrip].buzz_factor = stock_analyzer.StockAnalyzer().get_stock_analyze(symbol).split(',')
        

    print ' * saving cache...',
    pickle.dump(index, open('cache.p', 'wb'))
    print 'done'


def get_headlines():
    urls = [ 'http://www.moneycontrol.com' ]

    for url in urls:
        page = requests.get(url)
        tree = html.fromstring(page.content)

        headlines = tree.xpath('//a[@class="bl_14"]/text()')
        headlines += tree.xpath('//a[@class="bl_18"]/text()')
        headlines += tree.xpath('//h1[@class="bl_20 dinline"]/text()')
    return headlines


def stocks_in_news():
    headlines = get_headlines()
    resp = requests.post('http://ibmlaser.mybluemix.net/sire',
                data={ 'svcname': 'relationship_extraction',
                         'sid': 'ie-en-news',
                         'rt': 'json',
                         'text': ''.join(headlines)})

    root = ET.fromstring(resp.text)

    return [ a.text for a in root.findall(".//*[@type='ORGANIZATION']/mentref") ]


def risk_factor(growth):
    if growth < -25.0:
        return 1.0
    elif growth > 25.0:
        return 0.0
    elif -25.0 <= growth <= 25.0:
        return -(0.02 * growth) + 0.5


############################################


print ' * reading cache...',
try:
    index = pickle.load(open('cache.p', 'rb'))
    print 'done'
except:
    print 'failed'
    print ' * cache not found. creating cache'
    update_cache()

print ' * reading saved watchlist...',
try:
    watchlist = pickle.load(open('watchlist.p', 'rb'))
    print 'done'
except:
    print 'failed'
    print ' * loading default watchlist...',
    watchlist = pickle.load(open('watchlist_default.p', 'rb'))
    print 'done'


##############################


@app.route('/')
def apiindex():
    return jsonify(version=__version__)


@app.route('/headlines')
# get top headlines from news sources
def headlines():
    return json.dumps(get_headlines())


@app.route('/update')
# force update cache
def upd():
    thread.start_new_thread(update_cache, ())
    return ''


@app.route('/stocks/hot', methods=['GET'])
# list of hot stocks in news
def stockshot():
    return json.dumps(stocks_in_news())


@app.route('/stocks/active', methods=['GET'])
# most traded stocks
def stocksactive():
    return json.dumps(sorted([ (z.symbol, z.quantity) for z in index.values() ], key=lambda x: x[1])[:-20])


@app.route('/stocks/inactive', methods=['GET'])
# least traded stocks
def stocksinactive():
    return json.dumps(sorted([ (z.symbol, z.quantity) for z in index.values() ], key=lambda x: x[1])[:20])


@app.route('/stocks/gainers')
# top gainers
def stocksgainers():
    return json.dumps(sorted([ (z.symbol, z.short_term_gain) for z in index.values() ], key=lambda x: x[1])[-20:])


@app.route('/stocks/losers')
# top losers
def stockslosers():
    return json.dumps(sorted([ (z.symbol, z.short_term_gain) for z in index.values() ], key=lambda x: x[1])[:20])


@app.route('/stocks/turnover', methods=['GET'])
def stockshighestturnover():
    abort(501)


@app.route('/personality/risk/<handle>', methods=['GET'])
# get personality risk score of a twitter handle
def shrink(handle):
    return personality_insights.PersonalityInsights(handle).get_insights()


@app.route('/risk/short/<scrip>')
# get short term risk of the specified stock
def scripsrisk(scrip):
    return risk_factor(index[scrip].short_term_gain)


@app.route('/risk/mid/<scrip>')
def scripmrisk(scrip):
    return risk_factor(index[scrip].mid_term_gain)


@app.route('/risk/long/<scrip>')
def scriplrisk(scrip):
    return risk_factor(index[scrip].long_term_gain)


@app.route('/personality/suggestions/<handle>')
# suggest stocks according to personality score
def suggest(handle):
    user_risk = json.loads(personality_insights.PersonalityInsights(handle).get_insights())["risk_score"]

    short_term_risks = [ ( w.symbol, risk_factor(w.short_term_gain)) \
            for w in index.values() if hasattr(w, 'short_term_gain' )]
    mid_term_risks = [ ( w.symbol, risk_factor(w.mid_term_gain)) \
            for w in index.values() if hasattr(w, 'mid_term_gain' )]
    long_term_risks = [ ( w.symbol, risk_factor(w.long_term_gain)) \
            for w in index.values() if hasattr(w, 'long_term_gain' )]

    s_suggested = [ u[0] for u in short_term_risks \
            if abs( risk_threshold ) > float( u[1] ) - float(user_risk) ]
    m_suggested = [ u[0] for u in mid_term_risks \
            if abs( risk_threshold ) > float( u[1] ) - float(user_risk)]
    l_suggested = [ u[0] for u in long_term_risks \
            if abs( risk_threshold ) > float( u[1] ) - float(user_risk) ]

    return json.dumps({ 
                        'twitter_handle': handle,
                        'risk_factor': user_risk,
                        'suggestions': { 
                                         'short_term': s_suggested,
                                         'mid_term': m_suggested,
                                         'long_term': l_suggested
                       }})


@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist_ops():
    global watchlist
    if request.method == 'GET':
        resp = []
        for w_item in watchlist:
            buzz, buzz_factor = index[w_item].buzz, index[w_item].buzz_factor
            symbol = index[w_item].symbol
            quantity = index[w_item].quantity
            name = index[w_item].name

            resp.append({  "buzz": buzz,
                "buzz_factor": buzz_factor,
                "symbol": symbol,
                "quantity": quantity,
                "name": name })

        return json.dumps(resp)

    elif request.method == 'POST':
        try:
            watchlist = json.loads(request.data)["watchlist"]
            pickle.dump(watchlist, open('watchlist.p', 'wb'))
            print ' * updated watchlist:', watchlist
            return 'Success'
        except:
            abort(400)


@app.route('/stocks/buy')
def stocksbuy():
    resp = sorted([ ( i.symbol, i.buzz_factor ) for i in index.values() if i.buzz == 'positive' ],
            key=lambda x: x[1]).reverse() 

    return json.dumps(resp)


@app.route('/stocks/sell')
def stockssell():
    resp = sorted([ ( i.symbol, i.buzz_factor ) for i in index.values() if i.buzz == 'negative' ],
            key=lambda x: x[1])

    return json.dumps(resp)



@app.route('/tradeoff')
def tradeoff_analysis():
    option_string = ''
    for b in zip(index.values(), range(len(index))):
        a = b[0]
        stg = a.short_term_gain if hasattr(a, 'short_term_gain') else 0
        mtg = a.mid_term_gain if hasattr(a, 'mid_term_gain') else 0
        ltg = a.long_term_gain if hasattr(a, 'long_term_gain') else 0
        
        option_skel = '''
            {
                "key": "%s",
                "name": "%s",
                "values": {
                    "Short Term Gain": %s,
                    "Mid Term Gain": %s,
                    "Long Term Gain": %s,
                    "Risk Factor": %s,
                    "Quantity": %s
                },
                "description_html": "%s",
                "app_data": {}
            },''' % (b[1], a.symbol, stg, mtg, ltg,
                    risk_factor((stg+mtg+ltg)/3),
                    a.quantity, a.name)
        option_string += option_skel

    option_string = option_string[:-1]
    json_skel = '''{
        "subject": "Stocks Comparison",
        "columns": [
            {
                "type": "numeric",
                "key": "Short Term Gain",
                "full_name": "Short Term Gain",
                "description": "",
                "goal": "max",
                "is_objective": true
            },
            {
                "type": "numeric",
                "key": "Mid Term Gain",
                "full_name": "Mid Term Gain",
                "description": "",
                "goal": "max",
                "is_objective": true
            },
            {
                "type": "numeric",
                "key": "Long Term Gain",
                "full_name": "Long Term Gain",
                "description": "",
                "goal": "max",
                "is_objective": true
            },
            {
                "type": "numeric",
                "key": "Risk Factor",
                "full_name": "Risk Factor",
                "description": "",
                "goal": "min",
                "is_objective": true
            },
            {
                "type": "numeric",
                "key": "Quantity",
                "full_name": "Quantity",
                "goal": "max",
                "is_objective": false
            }
        ],
        "options": [ %s ]
    }''' % (option_string)
    return requests.post('https://watson-api-explorer.mybluemix.net/tradeoff-analytics/api/v1/dilemmas/',
            auth=(tradeoff_username, tradeoff_password), 
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, 
            data=json_skel).text


##############################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

