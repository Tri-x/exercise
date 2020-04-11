print('请输入几个点的横纵坐标,程序将会返回这几个点是否在同一条直线上')
def coor_nums():#获得每个值的横纵坐标
	int_list=[]#初始化坐标列表
	wrong_list=[]#初始化错误列表
	judgement=''#判断是否需要修正坐标值
	while True:
		nums=input('应以x1 y1 x2 y2...的格式输入:\n')
		num_list=nums.split()
		if len(num_list)%2!=0:#如果输入的坐标长度不是偶数 说明输入错误
			print('请输入每个点的横纵坐标')
			continue
		for n in num_list:#对输入的每个值
			try:
				num=float(n)
				int_list.append(num)#尝试将输入的值转为浮点类型添加到坐标列表中
			except Exception as e:#如果发生异常
				print('你输入的第'+str(num_list.index(n)+1)+'个值为:'+n+',它不是数字 请按照要求输入')#提示修改
				wrong_list.append([num_list.index(n),n])#将错误坐标值的索引和错误坐标值都添加到错误列表
				int_list.append(n)#同时也将错误坐标值添加到坐标列表 便于修改
				judgement='need'#判断为need 即需要修改
		return int_list,wrong_list,judgement
int_list,wrong_list,judgement=coor_nums()
def adjust(wrong_list):#调整错误列表并且修改对应坐标列表
	right_list=[]#初始化修改后的列表
	for wrong_num in wrong_list:#对于每个错误值
		while True:#循环修改直到修改正确
			right_num_input=input('正在修改第{}个值,原值为:{},现值为:\n'.format(wrong_num[0]+1,wrong_num[1]))
			try:
				right_num=float(right_num_input)
				right_list.append([wrong_num[0],right_num])#将修改值添加到正确列表
				break
			except Exception as e:
				print('修改值仍然错误,请再次修改')
				continue
	return right_list
def k_line_judge(int_list,wrong_list,judgement):#判断输入点是否在同一条直线
	if judgement=='need':#如果为need则需要调整初次输入的坐标值
		right_list=adjust(wrong_list)
		for n in right_list:
			int_list[n[0]]=n[1]#把每个修改后的值赋予坐标列表
	point_judge=list(set(int_list))
	if len(point_judge)==1:#如果输入的每个值相同 说明是同一个点
		return print('所有点是同一个点 为({},{})'.format(point_judge[0],point_judge[0]))
	k_list=[]#初始化直线斜率列表
	for n in range(3,len(int_list),2):#处理坐标列表
		try:
			k=(int_list[n]-int_list[n-2])/(int_list[n-1]-int_list[n-3])#斜率公式k=(y2-y1)/(x2-x1)
			k_list.append(k)#尝试向斜率列表中增加每两个点的斜率
		except ZeroDivisionError as e:#如果出现了x2-x1=0的情况 暂时先略过
			pass
		if n==len(int_list)-1 and len(k_list)==0:#如果循环到最后 直线斜率列表长度仍然为0
			return print('所有点在直线x={}上'.format(int_list[0]))#说明输入的坐标都在直线x=x1上
	set_k_list=list(set(k_list))
	if len(set_k_list)==1 and set_k_list[0]==0:#如果直线斜率列表长度为1 并且k=0 说明输入坐标都在y=y1上
		print('所有点在直线y={}上'.format(int_list[1]))
	elif len(set_k_list)==1 and set_k_list[0]!=0:#如果直线斜率列表长度为1 并且k不等于0
		line_k=set_k_list[0]#说明在一条y=kx+b的直线上
		line_b=int_list[1]-int_list[0]*line_k#b=y-kx
		if float(line_b)<=0:#分为b>0和b<=0两种打印情况
			print('所有点在直线y={}x{}上'.format(round(line_k,5),line_b))
		else:
			print('所有点在直线y={}x+{}上'.format(round(line_k,5),line_b))
	elif len(set_k_list)!=1:#如果斜率列表长度不为1说明不在同一条直线上
		print('所有点不在同一条直线上')
k_line_judge(int_list,wrong_list,judgement)
