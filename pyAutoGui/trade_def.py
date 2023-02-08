import time
import pyautogui as pag
import keyboard

#pyautogui.press+sleep組合鍵
def press_sleep(key,t):
    pag.press(key)
    time.sleep(t)

#點擊座標組合鍵
def click_xy(x,y):
    pag.moveTo(x,y)
    time.sleep(0.3)
    pag.click()

#購買指定商品 buy = [itemDict指定商品]
itemDict = {1:[238,217],2:[521,210],3:[246,357],4:[508,361], 5:[246,504],6:[542,504],7:[240,646],8:[527,646]}
def buyGood(buy):
    g = 0
    for i in buy:
        click_xy(itemDict[i][0],itemDict[i][1])
        time.sleep(0.5)
        click_xy(1157,244)
        time.sleep(1)
        if g == 0:
            press_sleep("num3",1)
        g = 1

#交易介面
def trading(x = None):
    press_sleep("num0",6)
    press_sleep("num1",6)
    if x == 1:
        press_sleep("num4",6)
    pag.press("num7")

#出港介面
def out_port():
    time.sleep(2.5)
    press_sleep("num2",4)

#導航介面
def navigation(t):
    time.sleep(2)
    press_sleep("num3",2)
    pag.press("space")
    time.sleep(t)

#縮小地圖
def zoomOutMap(t):
    time.sleep(3)
    for i in range(t):
        time.sleep(1.2)
        pag.press("num9")
    time.sleep(2)

#點擊下一個港口+合併縮小地圖
def next_port(x,y,zoom = None):
    if zoom == None:        
        click_xy(x,y)
    else:
        zoomOutMap(zoom)
        click_xy(x,y)

#搜尋港口+導航至下一個港口
def search_port(p,t):
    click_xy(490,110)
    time.sleep(1)    
    keyboard.write(p)
    time.sleep(1)
    click_xy(650,110)
    time.sleep(1)
    click_xy(650,110)
    time.sleep(2.5)
    next_port(793,473)
    navigation(t)

#出售貨物
def selfGoods(x = None):
    time.sleep(3)
    press_sleep("num0",5)
    press_sleep("space",1)
    press_sleep("num8",1)
    pag.press("num7")
    if x == 1:
        time.sleep(3)
        press_sleep("m",2)

#使用海盜旗
def flag():
    time.sleep(6)
    click_xy(933,840)

#跑商流程合併(推薦品)
def run_trading(x,y,t,zoom = None):
    next_port(x,y,zoom)
    navigation(t)
    trading()
    out_port()

#跑商流程合併(指定商品)
def run_tradingItems(x,y,t,buy,zoom = None):
    next_port(x,y,zoom)
    navigation(t)
    press_sleep("num0",5)
    buyGood(buy)
    pag.press("num7")
    out_port()

#買賣合一
def run_st(t = None):
    selfGoods(1)    
    trading(t)
    out_port()    

#自動貿易(遊戲內建功能(18mins))
def autoTrading():
    time.sleep(4)
    press_sleep("m",2)
    click_xy(1533,460)
    time.sleep(2)
    click_xy(1340,676)
    time.sleep(2)
    click_xy(1281,796)