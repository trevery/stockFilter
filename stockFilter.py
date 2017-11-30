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

    if (df.open.tolist()[0] and df.close.tolist()[0]
                           and df.high.tolist()[0]
                           and df.low.tolist()[0]):
        
        if df.open.tolist()[0]-df.low.tolist()[0] <= threshode :
            print('Hit reverse hammer: %s \n' % code)
            return True
        else:
            return False
    else:
        return False


def is_down_r_hammer(code='000927',
                     date='2017-11-28',
                     threshode=0):
    '''
    

                             |     |    <-- high
                             | |   |
                             | |  ---   <-- close
        min(open,close) _____  |  | |
                                  ---   <-- open, low

    '''
    df = ts.get_hist_data(code, start='2017-11-27', end=date)
    
    if df.open.tolist()[0] <= min(df.close.tolist()[1], df.open.tolist()[1]):
        if df.open.tolist()[0] - df.low.tolist()[0] <= threshode:
            print('Hit dropping down reverse hammer: %s \n' % code )
            return True
        else:
            return False
    else:
        return False


def up_or_down(code='000927', date='2017-11-29'):
    df = ts.get_hist_data(code, date, date)
    if (df.open.tolist()[0] < df.close.tolist()[0]):
        print('code %s up' % code)
        return True
    else:
        print('code %s down' % code)
        return False
    

def get_all_code_set(year=2017, quarter=3):
    report = ts.get_report_data(2017,3)
    codeSet = set(report.code.tolist()[0:20])
    return codeSet

    


'''
get all reverse hammer of day 11-28
'''

date = '2017-11-28'
hammerCodeSet = set()
allCodeSet = get_all_code_set()

for index,code in enumerate(allCodeSet):
    #print('--------------')
    try:
        if is_down_r_hammer(str(code)):
            hammerCodeSet.add(code)
    except:
        pass
    continue


'''
statistic the change of the dropping down hammer code
'''

date = '2017-11-29'
upCount = 0
downCount = 0
stayCount = 0

for hammerCode in hammerCodeSet:
    tag = up_or_down(hammerCode)
    if tag:
        upCount += 1
    elif not(tag):
        downCount += 1
    else:
        stayCount += 1

print('------statistics-----')
print('totoal hammer: %d' % len(hammerCodeSet))
print('up numbers: %d' % upCount)
print('down numbers: %d' % downCount)
upRate = upCount / len(hammerCodeSet)
print('up rate: %f' % upRate)



