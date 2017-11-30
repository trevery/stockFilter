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

def is_r_hammer(code='000927',date='2017-11-28',threshode=0):
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
    if df.open.tolist()[0] and df.close.tolist()[0] and df.high.tolist()[0]
                                                    and df.low.tolist()[0]:
        if df.open.tolist()[0]-df.low.tolist()[0] <= threshode :
            print('Hit reverse hammer: %s \n' % code)
        else:
            return
    else:
        return


def is_down_r_hammer(code='000927',
                     date='2017-11-28',
                     threshode=0):
    '''
    a little different from reverse 

         |     |    <-- high
         | |   |
         | |  ---   <-- close
           |  | |
              ---   <-- open, low

    it has no tail, which means : open - low = 0 or little more than 0,like 0.1 
    '''
    df = ts.get_hist_data(code, start='2017-11-27', end=date)
    
    if df.open.tolist()[0] <= df.close.tolist()[1]:
        if df.open.tolist()[0] - df.low.tolist()[0] <= threshode:
            print('Hit dropping down reverse hammer: %s \n' % code )
        else:
            return
    else:
        return


report = ts.get_report_data(2017,3)

for index,code in enumerate(report.code.tolist()[10:50]):
    #print('--------------')
    try:
        is_down_r_hammer(str(code))
    except:
        pass
    continue

