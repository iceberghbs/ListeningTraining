'''
文件：音源文件：指板音
1.开始运行程序
2.随机抽取mp3文件播放
    2.1 随机打开文件
    2.2 播放次数+时间间隔+播放提示音
    2.3 显示文件名
    2.4 关闭音频文件
'''
from playsound import playsound    #加载playsound包
import random
import time
Pitches=['C', 'G', 'D', 'A', 'E', 'B', 'bG', 'bD', 'bA', 'bE', 'bB', 'F']   #12个调
Octave=[2,3,4,5,6] #5个八度

def play():     #播放函数
    playsound('successful.mp3')
    P=random.randint(0,11)  #随机选取音名
    O=random.randint(0,4)   #随机选取音高
    note=str(Pitches[P])+str(Octave[O])     #合并为音符，连接字符串
    path=str("D:\文档\吉他谱\练耳音符\\")  #音符文件夹的绝对路径
    notefile=path + note + '.mp3' #指定音符文件地址
    t=0
    while t < 3:    #循环播放三遍
        playsound(notefile) #播放指定音符
        time.sleep(3)   #间歇3秒
        t=t+1
    playsound('successful.mp3')
    print(note)
