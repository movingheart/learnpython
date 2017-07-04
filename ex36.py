# -*- coding:utf-8 -*-

def zhaomama(num):
    if num == 3:
        print u"是想找妈妈吗？yes or no"
        res = raw_input("> ")
        if res == "yes":
            print u"再等等吧，过几天妈妈就回来了！"
        else:
            print u"来唱歌吧，门前大桥下，游过一群鸭，快来快来数一数，2、4、6、7、8 ......"

def lelechifan():
    print u"乐乐哭了？他想干啥？"
    print u"""\t1. 吃饭
    \t2. 睡觉
    \t3. 其他"""
    select = raw_input("> ")
    if int(select) == 1:
        print u"乐乐该吃饭了吗？yes or no"
        select_eat = raw_input("> ")
        if select_eat == "yes":
            print u"""
            吃什么？\n1.小米粥\n2.馒头
            """
            fan = raw_input("> ")
            if fan == "1":
                print u"你选择的小米粥，那可是很健康的食物哦！"
                exit(0)
            elif fan == "2":
                print u"你选择的是馒头，看来你还是挺爱吃面食的"
                exit(0)
            else:
                print u"不知你想吃啥，告诉妈妈吧！"
        elif select_eat == "no":
            print u"那你接着玩吧！但是可别哭哦！"
        else:
            print u"没明白你的意思！"
    elif int(select) == 2:
        print u"来吧，妈妈哄你睡觉！"
    elif int(select) == 3:
        print u"我也不知道你想干啥"
        zhaomama(3)
        
        

if __name__ == "__main__":
    lelechifan()
