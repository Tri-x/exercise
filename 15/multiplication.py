def multi_table(n):
	num=n+1
	for y in range(1,num):#每行
		for x in range(1,y+1):#每列
			value='{}x{}={}'.format(y,x,y*x)#当前值
			print('{}'.format(value),end=' '*(len(str(n))+len(str(x))+2+len(str(n*x))-len(value)+2))#n的长度+x的长度+两个符号的长度-当前值的长度+间距
		print()#换行
multi_table(25)
