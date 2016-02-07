#!/usr/bin/env python
from Extractor import tweet_extract
from StockAnalyzer import stock_analyzer

list1={'GOOG','AAPL'}
print stock_analyzer.StockAnalyzer().get_stock_analyze('GOOG')
