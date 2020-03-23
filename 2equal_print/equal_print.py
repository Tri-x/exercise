def equal_print(num):
	#num>2 且 num为奇数
	equal_list=[[''for n in range(num)]for n in range(num)]#列表初始化
	if num%2!=1:#如果num不为奇数 返回
		return print('数字必须大于2且为奇数')
	y=0#y是竖轴 x是横轴 范围是num
	x=num//2#坐标初始值为equal_list[0][num//2] //表示除法运算后向小值取整
	for n in range(1,num*num+1):#n是坐标代表的值
		equal_list[y][x]=n#赋值
		y=y-1
		x=x+1#坐标向右上方移动
		if y<0 and x>num-1:#如果竖轴方向移出了边界 而且 横轴方向也移出了边界
			y=y+2#竖轴值相对向下移一格
			x=x-1#横轴值相对不变
		if y<0 and x<num:#如果竖轴方向移出了边界 但 还在横轴范围内
			y=num-1#竖轴值等于竖轴方向最大值 横轴值不变
		if x>num-1 and y>-1:#如果横轴方向移出了边界 但 还在竖轴范围内
			x=0#横轴值等于横轴方向最小值 竖轴值不变
		if y>-1 and x<num and equal_list[y][x]!='':#如果在竖轴和横轴范围内 但 右上方已经有一个值填充
			y=y+2#竖轴值相对向下移一格
			x=x-1#横轴值相对不变
	#格式化打印出列表
	for n in range(num):
		for m in range(num):
			print(str(equal_list[n][m]).zfill(len(str(num*num))),end=' ')#str.zfill(num)指定num位数填充0
		print()
	#检测是否相等
	detect_value_list=[0 for n in range(4)]
	for n in range(num):
		detect_value_list[0]+=equal_list[0][n]#横排
		detect_value_list[1]+=equal_list[n][0]#纵列
		detect_value_list[2]+=equal_list[n][n]#左上至右下
		detect_value_list[3]+=equal_list[n][num-n-1]#右上至左下
	print(detect_value_list)
equal_print(5)
