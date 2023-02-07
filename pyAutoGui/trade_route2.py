#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#貿易路線2(歐非線(天津衛出發))
def runEA():
    time_start = time.time() #開始計時
    time.sleep(4)
    out_port()

    run_tradingItems(896,889,32,[1,2,3,4,6]) #應天府
    run_tradingItems(739,813,70,[7],5) #班格爾馬辛

    #莫三比克
    search_port('莫三比克',1)
    flag() #海盜旗使用
    time.sleep(96)
    press_sleep("num0",5)
    buyGood([3,5,8])
    pag.press("num7")
    out_port()

    run_tradingItems(438,881,27,[4,6],1)   #索法拉
    run_tradingItems(787,631,15,[4,5])     #納塔爾
    run_tradingItems(120,710,35,[2,5])     #開普敦
    run_tradingItems(659,53,28,[6],2)      #卡里比布
    run_tradingItems(788,57,25,[3],1)      #本格拉
    run_tradingItems(517,48,35,[4],2)      #聖多美
    run_tradingItems(820,229,20,[1])       #貝南
    run_tradingItems(603,381,17,[2,6])     #聖喬治
    run_tradingItems(74,425,32,[3,4])      #獅子山
    run_tradingItems(657,57,30,[7],2)      #阿爾金
    run_trading(1406,123,85,4)             #伊斯坦布爾

    #基輔
    search_port('基輔',35)
    run_st()

    #貝魯特
    search_port('貝魯特',1)
    flag() #海盜旗使用
    time.sleep(35)
    run_st()

    run_trading(771,541,25)    #雅法    
    run_trading(457,621,20)    #亞歷山大
    run_trading(429,56,40,3)   #威尼斯
    run_trading(885,791,32)    #那不勒斯
    run_trading(257,288,25)    #馬賽
    run_trading(453,887,25)    #馬拉加
    run_trading(794,93,40,2)   #南特

    #漢堡
    search_port('漢堡',36)
    run_st()

    #雅典
    search_port('雅典',90)
    run_st(1)

    #卡利卡特
    search_port('卡利卡特',1)
    flag() #海盜旗使用
    time.sleep(197)
    press_sleep("num0",5)
    buyGood([2,5])
    pag.press("num7")
    out_port()

    #返回天津衛
    search_port('天津衛',118)
    selfGoods()

    time_end = time.time()          #結束計時
    time_c= time_end - time_start   #執行所花時間
    print('歐非線貿易時間:{:.1f}'.format(time_c), 's')

