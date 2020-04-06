def character_diamond(n):#n的最大值取决于character_list的长度
	character_list=list('-'.join(sorted(list('789456123QWERTYUIOPASDFGHJKLZXCVBNM~@%*+-/|'))))
	#str.join(list) 用str来连接list的每一项
	#sorted(list) 按照ASCII unicode 对list排序
	quarter_diamond=[[' 'for x in range(n+n-1)]for y in range(n)]#先创建菱形的左上四分之一
	for y in range(n):#在n行中
		for z in range(n*2-1):#在n*2-1层中
			for x in range(n*2-(2-z)-y*2,n*2-1):#在(n*2-(2-z)-y*2,n*2-1)范围内
				quarter_diamond[y][x]=character_list[n*2-2-z]#菱形的每个值为character_list中索引为n*2-2-z的值
	for y in range(n):#左右对称
		quarter_diamond[y].extend(reversed(quarter_diamond[y][0:-1]))
	quarter_diamond.extend(reversed(quarter_diamond[0:-1]))#上下对称
	for y in range(n*2-1):#打印菱形
		for x in range((n*2-1)*2-1):
			print(quarter_diamond[y][x],end='')
		print()
character_diamond(20)
