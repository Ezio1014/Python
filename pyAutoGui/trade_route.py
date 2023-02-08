import time
import pyautogui as pag
import imp

import trade_def as td
#imp.reload(trade_def)

#貿易路線(東南亞+日本線(天津衛出發))
def runSA_JP():
    time_start = time.time() #開始計時
    
    #商品販售1(天津衛出發)
    td.pag.press("m")
    time.sleep(1.5)
    td.out_port()

    td.run_trading(942,745,25) #淮安

    #基隆
    td.next_port(871,886,1)
    td.navigation(1)
    td.flag() #海盜旗使用
    time.sleep(20)
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
    td.selfGoods()
    td.out_port()
    
    #長崎
    td.search_port('長崎',55)
    td.trading()
    td.out_port()
    
    td.run_trading(1131,391,30)  #京都
    td.run_trading(1005,75,40,1) #札幌
    td.run_trading(306,457,25)   #符拉迪沃斯托克
    td.run_trading(674,887,25,1) #釜山
    td.run_trading(624,265,30)   #平壤

    #返回天津衛
    td.next_port(388,462)
    td.navigation(21)
    td.selfGoods()    
    
    time_end = time.time()          #結束計時
    time_c= time_end - time_start   #執行所花時間
    print('東南亞+日本線貿易時間:{:.1f}'.format(time_c), 's')
    
#貿易路線2(歐非線(天津衛出發))
def runEA():
    
    time_start = time.time() #開始計時
    time.sleep(4)
    td.out_port()

    td.run_tradingItems(896,889,32,[3,1,2,4,6]) #應天府
    td.run_tradingItems(739,813,70,[7],5) #班格爾馬辛

    #莫三比克
    td.search_port('莫三比克',1)
    td.flag() #海盜旗使用
    time.sleep(93)
    td.press_sleep("num0",5)
    td.buyGood([3,5,8])
    td.pag.press("num7")
    td.out_port()

    td.run_tradingItems(438,881,27,[4,6],1)   #索法拉
    td.run_tradingItems(787,631,15,[4,5])     #納塔爾
    td.run_tradingItems(120,710,35,[2,5])     #開普敦
    td.run_tradingItems(659,53,28,[6],2)      #卡里比布
    td.run_tradingItems(788,57,25,[3],1)      #本格拉
    td.run_tradingItems(517,48,35,[4],2)      #聖多美
    td.run_tradingItems(820,229,20,[1])       #貝南
    td.run_tradingItems(603,381,17,[2,6])     #聖喬治
    td.run_tradingItems(74,425,32,[4,3])      #獅子山
    td.run_tradingItems(657,57,30,[7],2)      #阿爾金
    
    #伊斯坦布爾
    td.search_port('伊斯坦布爾',85)
    td.trading()
    td.out_port()

    #基輔
    td.search_port('基輔',35)
    td.run_st()

    #貝魯特
    td.search_port('貝魯特',10)
    td.flag() #海盜旗使用
    time.sleep(30)
    td.run_st()

    td.run_trading(771,541,25)    #雅法    
    td.run_trading(457,621,20)    #亞歷山大
    td.run_trading(429,56,40,3)   #威尼斯
    td.run_trading(885,791,32)    #那不勒斯    
    td.run_trading(54,659,31,1)   #馬拉加
    td.run_trading(552,478,17,1)  #賽維利亞
    
    #南特
    td.search_port('南特',35)
    td.run_st()

    #漢堡
    td.search_port('漢堡',36)
    td.run_st()

    #雅典
    td.search_port('雅典',90)
    td.run_st(1)

    #卡利卡特
    td.search_port('卡利卡特',1)
    td.flag() #海盜旗使用
    time.sleep(197)
    td.press_sleep("num0",5)
    td.buyGood([5,2])
    td.pag.press("num7")
    td.out_port()

    #返回天津衛
    td.search_port('天津衛',118)
    td.selfGoods()
    
    time_end = time.time()          #結束計時
    time_c= time_end - time_start   #執行所花時間
    print('歐非線貿易時間:{:.1f}'.format(time_c), 's')