from matplotlib import pyplot as plt
import numpy as np

def one():
    labels = 'frogs','hogs','狗','logs'
    sizes=15,20,45,10
    colors='yellowgreen','gold','lightskyblue','lightcoral'
    explode=0.05,0.05,0,0
    #表示快之间的距离
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    #设置x,y轴的长度
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #用来正常显示中文
    plt.show()
    #labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    #autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    #shadow，饼是否有阴影
    #startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    #pctdistance，百分比的text离圆心的距离
    #patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性

def tow():
    fig = plt.figure()
    ax = fig.add_subplot(223,facecolor=(0.1843,0.3098,0.3098))  #facecolor设置背景颜色
    ax.set(xlim=[0.5,4.5],ylim = [-2,8],title = 'An Example',ylabel='Y-Axis',xlabel='X-Axis')
    plt.show()

def three():
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    print(type(ax1))
    plt.show()

def four():
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax2 = fig.add_axes([0.70,0.70,0.60,0.60])
    plt.show()
from pylab import *
def five():
    x = np.arange(-5.0,5.0,0.02)
    print(x)
    y1 = np.sin(x)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x,y1)
    plt.subplot(212)
    xlim(-5,5)
    ylim(-1,1)
    plt.plot(x,y1)
    plt.show()
def sixx():
    plt.figure(2)
    t = np.arange(0.,5.,0.02)
    plt.plot(t,t,'r--',t,t**2,'bs',t,t*20,'g^',t,t**3,'b')
    plt.show()
def seven():
    plt.figure(1)  # 第一张图
    plt.subplot(211)  # 第一张图中的第一张子图
    plt.plot([1, 2, 3])
    plt.subplot(212)  # 第一张图中的第二张子图
    plt.plot([4, 5, 6])

    plt.figure(2)  # 第二张图
    plt.plot([4, 5, 6])  # 默认创建子图subplot(111)

    plt.figure(1)  # 切换到figure 1 ; 子图subplot(212)仍旧是当前图
    plt.subplot(211)  # 令子图subplot(211)成为figure1的当前图
    plt.title('Easy as 1,2,3')  # 添加subplot 211 的标题
    plt.show()

def eight():
    xlabels = ['G1','G2','G3','G4','G5']
    means = [150,160,146,172,155]
    xpositions = np.arange(5)
    fig,axes = plt.subplots()
    width = 0.25
    p = axes.bar(xpositions,means,width,color=['r','y','b','g','k'],bottom =0)
    axes.set_title('test')
    axes.set_xticks(xpositions)
    axes.set_xticklabels(('G1','G2','G3','G4','G5'))#横坐标上值的标签
    plt.show()

def night():
    X = np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S = np.cos(X),np.sin(X)
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])   #设置X轴几号标签
    yticks([-1,+1])
    plot(X,C,label = "cosine")
    plot(X,S,label = "sin")
    legend(loc="upper left")          # 备注标签位置

    # 移动脊柱（设置轴位置）
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position("bottom")
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position("left")
    ax.spines["left"].set_position(('data',0))

    #给一些特殊的点做注释
    t = 2*np.pi/3
    plot([t,t],[0,np.cos(t)],color="blue",linestyle="--")
    scatter([t,],[np.cos(t),],15,color='blue')
    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+5, +30), textcoords='offset points', fontsize=11,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plot([t,t],[0,np.sin(t)],color="red",linestyle="--")
    scatter([t,],[np.sin(t),],15,color='red')
    annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=11,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    show()

def ten():
    figure(figsize=(9,6))
    n = 500
    X = np.random.normal(0,1,n)  #生成平均数为0，方差为1的一个数据集
    Y = np.random.normal(0,1,n)
    T = np.arctan2(X,Y)
    scatter(X,Y,s=25,c=T,alpha=.5,marker="o")
    # xlim(-1.5,1)
    # xticks(())
    # ylim(-1.5,1)
    # yticks(())
    # plot(Y)
    show()

def eleven():
    def f(x, y): return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
    n = 10
    x = np.linspace(-3, 3, 4 * n)   #返回均匀差值的列表，n控制个数
    y = np.linspace(-3, 3, 3 * n)
    X, Y = np.meshgrid(x, y)      #将两个一维数组变成二维矩阵
    imshow(f(X, Y))
    colorbar()
    show()
from mpl_toolkits.mplot3d import Axes3D
def three_D():
    fig = figure("3D")
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    plt.axis("equal")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

    show()


if __name__ == '__main__':
    # one()
    # tow()
    # three()
    # four()
    # five()
    # sixx()
    # seven()
    #eight()
    # night()
    # ten()
    # eleven()
    three_D()