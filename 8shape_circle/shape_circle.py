def circle(r):
	#空心圆
	hollow_quarter_circle_rd=[[' 'for x in range(r*2+1)]for y in range(r+1)]#创建圆的右下角四分之一的列表
	hollow_half_circle_right=[]#创建圆的右半边的列表
	hollow_whole_circle=[]#创建整个圆的列表
	for y in range(r+1):#填充四分之一圆
		half_chord=round((r**2-y**2)**0.5)#half_chord 弦长的一半 利用勾股定理y^2+x^2=r^2
		hollow_quarter_circle_rd[y][half_chord*2]='o'#竖向填充
		hollow_quarter_circle_rd[half_chord][y*2]='o'#横向填充
	for y in range(r+1):#将圆的右下角四分之一沿x轴对称翻转填充到圆的右半边的列表内
		hollow_half_circle_right.append(hollow_quarter_circle_rd[-y-1])
	for y in range(r+1):#填充圆的右下角四分之一到圆的右半边的列表内
		hollow_half_circle_right.append(hollow_quarter_circle_rd[y])
	for y in range(r*2+2):#将圆的右半部分沿y轴对称翻转填充到整个圆的列表内
		hollow_whole_circle.append(hollow_half_circle_right[y])
		hollow_whole_circle[y]=hollow_whole_circle[y][::-1]#填充后每行列表翻转
		hollow_whole_circle[y]+=' '#填充最中间的一列
	for y in range(r*2+2):#将圆的右半部分填充到整个圆的列表
		hollow_whole_circle[y].extend(hollow_half_circle_right[y])
	for y in range(r*2+2):#打印出圆
		for x in range(r*4+3):
			print(hollow_whole_circle[y][x],end='')
		print()
	print()
	#实心圆
	quarter_circle_rd=[[' 'for x in range(r*2+1)]for y in range(r+1)]#创建圆的右下角四分之一的列表
	half_circle_right=[]#创建圆的右半边的列表
	half_circle_right_x_coordinate=[]#创建圆的右半边的x值列表
	whole_circle=[]#创建整个圆的列表
	for y in range(r+1):#填充四分之一圆
		half_chord=round((r**2-y**2)**0.5)#half_chord 弦长的一半 利用勾股定理y^2+x^2=r^2
		quarter_circle_rd[y][half_chord*2]='o'#竖向填充
		quarter_circle_rd[half_chord][y*2]='o'#横向填充
	for y in range(r+1):#将圆的右下角四分之一沿x轴对称翻转填充到圆的右半边的列表内
		half_circle_right.append(quarter_circle_rd[-y-1])
	for y in range(r+1):#填充圆的右下角四分之一到圆的右半边的列表内
		half_circle_right.append(quarter_circle_rd[y])
	for y in range(r*2+2):#获取圆的右半边的x值
		for x in range(r*2+1):
			if half_circle_right[y][x]=='o':
				half_circle_right_x_coordinate.append(x)
				break#对于每一行取到第一个值就退出x的循环
	for y in range(r*2+2):#填充内部
		for x in range(half_circle_right_x_coordinate[y]):
			half_circle_right[y][x]='o'
	for y in range(r*2+2):#填充两个符号中间的空格 o o→ooo
		for x in range(r*2+1-2):
			if half_circle_right[y][x]=='o' and half_circle_right[y][x+2]=='o':#如果有两个连着的o
				half_circle_right[y][x+1]='o'#两个o中间的空格变为o
	for y in range(r*2+2):#将圆的右半部分沿y轴对称翻转填充到整个圆的列表内
		whole_circle.append(half_circle_right[y])
		whole_circle[y]=whole_circle[y][::-1]#填充后每行列表翻转
		whole_circle[y]+='o'#填充最中间的一列
	for y in range(r*2+2):#将圆的右半部分填充到整个圆的列表
		whole_circle[y].extend(half_circle_right[y])
	for y in range(r*2+2):#打印出圆
		for x in range(r*4+3):
			print(whole_circle[y][x],end='')
		print()
circle(20)
