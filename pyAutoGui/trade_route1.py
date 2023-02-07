#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#貿易路線(東南亞+日本線(天津衛出發))
def runSA_JP():
    time_start = time.time() #開始計時
    
    #商品販售1(天津衛出發)
    pag.press("m")
    time.sleep(1.5)
    out_port()

    run_trading(942,745,25) #淮安

    #基隆
    next_port(871,886,1)
    navigation(1)
    flag() #海盜旗使用
    time.sleep(21)
    trading()
    out_port()

    run_trading(900,880,57,4) #安汶
    run_trading(613,778,22)   #帝利
    run_trading(141,377,30)   #泗水
    run_trading(419,209,25)   #巴領旁

    #汶萊
    next_port(1301,81)
    navigation(28)
    selfGoods()
    out_port()

    run_trading(1005,60,55,4) #長崎
    run_trading(1131,391,30)  #京都
    run_trading(1005,75,40,1) #札幌
    run_trading(306,457,25)   #符拉迪沃斯托克
    run_trading(674,887,25,1) #釜山
    run_trading(624,265,30)   #平壤

    #返回天津衛
    next_port(388,462)
    navigation(21)
    selfGoods()    
    
    time_end = time.time()          #結束計時
    time_c= time_end - time_start   #執行所花時間
    print('東南亞+日本線貿易時間:{:.1f}'.format(time_c), 's')

