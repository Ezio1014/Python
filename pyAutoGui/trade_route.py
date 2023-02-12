import time
import pyautogui as pag
import imp

import trade_def as td


#貿易路線1(東南亞+日本線(天津衛出發))
def runSA_JP():
    time_start = time.time() #開始計時
    
    #商品販售1(天津衛出發)
    td.out_port()

    td.run_trading(942,745,25) #淮安

    #基隆
    td.next_port(871,886,1)
    td.navigation(2)
    td.flag(19) #海盜旗使用
    td.trading()
    td.out_port()
    
    #安汶
    td.search_port('安汶',56)
    td.trading()
    td.out_port()
    
    td.run_trading(613,778,22)   #帝利
    td.run_trading(141,377,30)   #泗水
    td.run_trading(419,209,25)   #巴領旁

    #汶萊
    td.next_port(1301,81)
    td.navigation(28)
    td.run_st(1)
    
    #長崎
    td.search_port('長崎',55)
    td.trading()
    td.out_port()
    
    td.run_trading(1131,391,29)  #京都
    td.run_trading(1005,75,40,1) #札幌
    td.run_trading(306,457,25)   #符拉迪沃斯托克
    td.run_trading(674,887,25,1) #釜山
    td.run_trading(624,265,30)   #平壤

    #返回天津衛
    td.next_port(388,462)
    td.navigation(21)
    td.selfGoods()
    
    time_end = time.time() - time_start   #執行所花時間
    print('東南亞+日本線貿易時間:{:.1f}'.format(time_end), 's')
    
#貿易路線2(歐非線(天津衛出發))
def runEA():    
    time_start = time.time() #開始計時    
    td.out_port()

    td.run_tradingItems(896,889,32,[3,1,2,4,6]) #應天府
    
    #班格爾馬辛
    td.search_port('班格爾馬辛',68)    
    td.buyGood([7])    
    td.out_port()

    #莫三比克
    td.search_port('莫三比克',2)
    td.flag(88) #海盜旗使用    
    td.buyGood([3,5,8])
    td.out_port()

    td.run_tradingItems(438,881,30,[4,3,6],1)   #索法拉
    td.run_tradingItems(787,631,16,[4,5])     #納塔爾
    td.run_tradingItems(120,710,35,[2,5])     #開普敦
    td.run_tradingItems(659,53,28,[6],2)      #卡里比布
    td.run_tradingItems(788,57,25,[3],1)      #本格拉
    td.run_tradingItems(517,48,37,[4],2)      #聖多美
    td.run_tradingItems(820,229,20,[1])       #貝南
    td.run_tradingItems(603,381,17,[2,6])     #聖喬治
    td.run_tradingItems(74,425,34,[4])      #獅子山
    td.run_tradingItems(657,57,30,[7],2)      #阿爾金
    
    #伊斯坦布爾
    td.search_port('伊斯坦布爾',85)
    td.buyGood([6])
    td.out_port()

    #基輔
    td.search_port('基輔',35)
    td.run_st(1)

    #貝魯特
    td.search_port('貝魯特',52)
    td.run_st(1)
    
    #雅法
    td.search_port('雅法',5)
    td.flag(20) #海盜旗使用
    td.run_st(0)
    
    #亞歷山大
    td.search_port('亞歷山大',20)    
    td.run_st(0)
    
    #威尼斯
    td.search_port('威尼斯',40)    
    td.run_st(0)
    
    td.run_trading(885,791,32)    #那不勒斯    
    td.run_trading(54,659,31,1)   #馬拉加    
    
    #南特
    td.search_port('南特',40)
    td.run_st(0)

    #漢堡
    td.search_port('漢堡',36)
    td.run_st(1)
    
    #波爾多
    td.search_port('波爾多',36)
    td.run_st(0)
    
    #塞維利亞
    td.search_port('塞維利亞',33)
    td.run_st(0)
    
    #瓦倫西亞
    td.search_port('瓦倫西亞',25)
    td.run_st(1)
    
    #馬賽
    td.search_port('馬賽',21)
    td.run_st(0)
    
    #雅典
    td.search_port('雅典',39)
    td.run_st(1,1)

    #卡利卡特
    td.search_port('卡利卡特',194)    
    td.buyGood([5,3,2])
    td.out_port()

    #返回天津衛
    td.search_port('天津衛',4)
    td.flag(112) #海盜旗使用
    td.selfGoods()
    
    time_end = time.time() - time_start   #執行所花時間
    print('歐非線貿易時間:{:.1f}'.format(time_end), 's')
    
#自動貿易(最後一港脫離卡死 time:760s)
def AT():
    td.autoTrading()
    time.sleep(757)
    
    #避免該死的漂流瓶...
    td.click_xy(1077,217,1)
    td.click_xy(757,65,1)
    
    td.click_xy(1533,466,3)
    td.click_xy(1349,789,2)
    td.click_xy(1483,154,2)
    td.press_sleep("m",2.5)
    td.click_xy(1373,823,8)
    td.selfGoods()