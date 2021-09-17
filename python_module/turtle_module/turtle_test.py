"""
turtle -海龟绘图
https://docs.python.org/zh-cn/3/library/turtle.html#turtle.fillcolor

"""
import turtle

# 画布，Screen
# turtle.Screen().setup(width=400,height=400, startx=400, starty=200)   # 设置主窗口的大小和位置，默认画布大小（400,300）
# turtle.screensize(canvwidth=4000, canvheight=3000, bg='green')    # 设置画布的大小（注意滚动条）和背景颜色


# 海龟/画笔，Turtle，默认有一个坐标原点为画布中心的坐标轴，坐标原点上有一只面朝x轴正方向小乌龟
# turtle.hideturtle() # 隐藏海龟形状
# turtle.showturtle() # 显示海龟形状
# turtle.penup() # 提起画笔，海龟飞行不留下痕迹
# turtle.pendown() # 放下画笔，海龟爬行留下痕迹
# turtle.pensize(width=10)  # 设置画笔宽度
# turtle.pencolor('red')  # 设置画笔颜色

# turtle.setheading(45)   # 设置海龟初始方向
# turtle.seth(to_angle=45)
# turtle.right(30)  # 顺时针旋转海龟
# turtle.left(30)   # 逆时针旋转海龟

# turtle.forward(100)  # 朝着海龟正方向移动
# turtle.backward(100) # 朝着海龟反方向移动
# turtle.back(100)   # 朝着海龟反方向移动
# turtle.setx(100) # 将海龟沿着x轴移动到指定位置
# turtle.sety(100) # 将海龟沿着xy轴移动到指定位置
# turtle.goto(100,200) # 绝对值坐标，将画笔移动到目标坐标位置
# turtle.circle(radius=100,extent=145,steps=5) # 沿着海龟方向，圆心在左侧/右侧，顺时针/逆时针旋转画圆/圆弧/正多边形，半径radius，步长steps,角度extent，
# turtle.home()   # 重置海龟位置为（0,0），方向朝东

# turtle.fillcolor('blue')  # 设置填充颜色
# turtle.color('red','green') # 同时设置画笔颜色和填充颜色
# turtle.begin_fill() # 开始填充
# turtle.circle(100)
# turtle.end_fill()   #结束填充

# turtle.dot(10,'red')    # 绘制一个指定直径和颜色的圆点


# 绘图结束
# turtle.Screen().exitonclick()   # 鼠标点击绘图窗口会关闭
# turtle.mainloop()
# turtle.done()



# 爱心
import turtle
turtle.fillcolor('red')
turtle.begin_fill()
turtle.left(40)
turtle.forward(100)
turtle.circle(50,210)
turtle.right(135)
turtle.circle(50,210)
turtle.forward(100)
turtle.end_fill()
turtle.Screen().exitonclick()