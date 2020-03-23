def shape_print(n):
	#实心等腰三角形
	for y in range(n):
		for x in range(n-y-1):#先循环打印空格 形成一个倒直角三角形 range()中的值是形成的规律
			print(' ',end='')
		for z in range(y*2+1):#再循环打印X 形成一个等腰三角形 range()中的值是形成的规律
			print('X',end='')
		print()
	print()#间隔
	#空心等腰三角形
	for y in range(n):
		for x in range(n-y-1):#先循环打印空格 形成一个倒直角三角形 range()中的值是形成的规律
			print(' ',end='')
		for x in range(1):#再循环打印左腰边
			print('X',end='')
		for z in range(y*2-1):#再循环打印内部空格 形成内部的等腰三角形 range()中的值是形成的规律
			if y<n-1:
				print(' ',end='')
		for x in range(1):#再循环打印右腰边
			if 0<y<n-1:
				print('X',end='')
			if y==n-1:#再循环打印底边
				print('X'*y*2,end='')
		print()
	print()
	#实心菱形
	solid_diamond=['' for y in range(n*2-1)]#由于菱形上下两部分相同 用列表的方法
	for y in range(n):
		for x in range(n-y-1):#先循环打印空格 形成一个倒直角三角形
			solid_diamond[y]+=' '
		for z in range(y*2+1):#再循环打印X 形成一个等腰三角形
			solid_diamond[y]+='X'
		solid_diamond[-y-1]=solid_diamond[y]#下半部分等于上半部分
	for y in range(n*2-1):#打印实心菱形
		print(solid_diamond[y])
	print()
	#空心菱形
	hollow_diamond=['' for y in range(n*2-1)]#由于菱形上下两部分相同 用列表的方法
	for y in range(n):
		for x in range(n-y-1):#先循环打印空格 形成一个倒直角三角形
			hollow_diamond[y]+=' '
		for x in range(1):#再循环打印左腰边
			hollow_diamond[y]+='X'
		for z in range(y*2-1):#再循环打印内部空格 形成内部的等腰三角形
			if y<n-1:
				hollow_diamond[y]+=' '
		for x in range(1):#再循环打印右腰边
			if 0<y<n-1:
				hollow_diamond[y]+='X'
			if y==n-1:#再循环打印底边
				hollow_diamond[y]+=' '*(y*2-1)+'X'
		hollow_diamond[-y-1]=hollow_diamond[y]#下半部分等于上半部分
	for y in range(n*2-1):#打印实心菱形
		print(hollow_diamond[y])
	print()
	#实心梯形
	solid_trapezium=[['X' for x in range(n*3)] for y in range(n)]#由于梯形近似矩形 用列表的方法
	for y in range(n):
		for x in range(n-y-1):#再循环替换成空格 形成梯形左边的倒直角三角形
			solid_trapezium[y][x]=' '
		for x in range(n*2+y+1,n*3):#再循环替换成空格 形成梯形右边的倒直角三角形
			solid_trapezium[y][x]=' '
		for x in range(n*3):#打印实心梯形
			print(solid_trapezium[y][x],end='')
		print()
	print()
	#空心梯形
	hollow_trapezium=[['X' for x in range(n*3)] for y in range(n)]#由于梯形近似矩形 用列表的方法
	for y in range(n):
		for x in range(n-y-1):#再循环替换成空格 形成梯形左边的倒直角三角形
			hollow_trapezium[y][x]=' '
		for x in range(n*2+y+1,n*3):#再循环替换成空格 形成梯形右边的倒直角三角形
			hollow_trapezium[y][x]=' '
		for x in range(n-y,n*2+y):#再循环替换成空格 形成梯形中间的空心
			if 0<y<n-1:
				hollow_trapezium[y][x]=' '
		for x in range(n*3):#打印实心梯形
			print(hollow_trapezium[y][x],end='')
		print()
	print()
	#实心正六边形
	solid_regular_hexagon=[[' 'for x in range(2*(n-1)+(n+(n-1)))] for y in range(n+(n-1)*2)]#初始化六边形列表
	solid_rapezium_symmetry=[[]for x in range(n+(n-1)*2)]#初始化六边形对称列表
	for y in range(n*3-2):
		for x in range((n-1)*2,(n-1)*2+(n+(n-1)),2):#先循环形成六边形中间的矩形
			solid_regular_hexagon[y][x]='X'
		for x in range(n-1-int(y/2),(n-1-int(y/2))+(y+n)):#再循环形成六边形左边的梯形
			if y<(n-1)*2 and y%2==0:
				solid_regular_hexagon[x][y]='X'
	for y in range(n*3-2):#再循环复制六边形左边的梯形对称到右边
		solid_rapezium_symmetry[y].extend(solid_regular_hexagon[y][:(n-1)*2])#六边形对称列表添加六边形左边梯形
		solid_regular_hexagon[y].extend(solid_rapezium_symmetry[y][::-1])#将梯形对称翻转
		for x in range(4*(n-1)+(n+(n-1))):#打印实心正六边形
			print(solid_regular_hexagon[y][x],end='')
		print()
	print()
	#空心正六边形
	hollow_regular_hexagon=[[' 'for x in range(2*(n-1)+(n+(n-1)))] for y in range(n+(n-1)*2)]#初始化六边形列表
	hollow_rapezium_symmetry=[[]for x in range(n+(n-1)*2)]#初始化六边形对称列表
	for y in range(n*3-2):
		for x in range((n-1)*2,(n-1)*2+(n+(n-1)),2):#先循环形成六边形中间的空心矩形
			if y==0 or y==n*3-2-1:
				hollow_regular_hexagon[y][x]='X'
		for x in range(n-1-int(y/2),(n-1-int(y/2))+(y+n)):#再循环形成六边形左边的空心梯形
			if (y<(n-1)*2 and y%2==0) and (x==n-1-int(y/2) or x==(n-1-int(y/2))+(y+n)-1):
				hollow_regular_hexagon[x][y]='X'
	for y in range(n-1,n*2-1):#填充六边形最左边
		hollow_regular_hexagon[y][0]='X'
	for y in range(n*3-2):#再循环复制六边形左边的梯形对称到右边
		hollow_rapezium_symmetry[y].extend(hollow_regular_hexagon[y][:(n-1)*2])#六边形对称列表添加六边形左边梯形
		hollow_regular_hexagon[y].extend(hollow_rapezium_symmetry[y][::-1])#将梯形对称翻转
		for x in range(4*(n-1)+(n+(n-1))):#打印空心正六边形
			print(hollow_regular_hexagon[y][x],end='')
		print()
	print()
shape_print(5)
