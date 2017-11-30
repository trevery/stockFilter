import tushare as ts
import sys
import time
from datetime import datetime, timedelta


def get_all_code(date='2017-11-28'):
    for i,code in enumerate(report.code):
        yield code
        
    
today = time.strftime("%Y-%m-%d", time.localtime())
yesterday = datetime.now() + timedelta(days = -1)
yesterday = yesterday.strftime("%Y-%m-%d")

def find_r_hammer(code='000927',date='2017-11-28',threshode=0):
    '''
    check the stock is 'reverse hammer' chart or not
    reverse hammer chart looks like this:

               |    <-- high
               |
              ---   <-- close
              | |
              ---   <-- open, low

    it has no tail, which means : open - low = 0 or little more than 0,like 0.1 
    '''
    df = ts.get_hist_data(code,start=date,end=date)
    #df0 = ts.get_hist_data(code,yesterday,yesterday)
    if df.open[0] and df.close[0] and df.high[0] and df.low[0]:
        if df.open[0]-df.low[0] <= threshode :
            print('code %s is a reverse hammer chart \n' % code)
        else:
            pass



report = ts.get_report_data(2017,3)

for index,code in enumerate(report.code):
    try:
        find_r_hammer(str(code),'2017-11-29')
    except:
        '''
        ignore the except and continue
        '''
        pass
    continue

