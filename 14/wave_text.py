def build_wave(strs='example',height=3,width=2,smoothness=3,form='whole'):#设置默认波浪
	wave_strs=strs#自定义波浪字符串
	strs_len=len(strs)#获取字符串长度
	wave_height=strs_len*height#自定义波浪高度 值>0
	wave_width=strs_len*width#自定义波浪宽度 值>0
	wave_smoothness=smoothness#自定义波浪平滑度 值>0 值越大波浪越平滑
	wave_form=form#自定义波浪类型
	with open('wave_text.txt','w') as f:
		if wave_form=='whole':#整块型
			for h in range(wave_height):
				if h%2==0:
					direction=1#利用奇偶性判断波浪摆动方向
				elif h%2==1:
					direction=-1
				for w in range(wave_width):
					for s in range(wave_smoothness):
						if direction==1:
							f.write(' '*w+wave_strs+'\n')
						if direction==-1:
							f.write(' '*(wave_width-w)+wave_strs+'\n')
		elif wave_form=='discr':#离散型
			wave_array=[[' 'for x in range(wave_width)] for y in range(strs_len+width+4)]#初始化离散型数组
			for y in range(strs_len):#先添加数组左上角的字符串
				for x in range(strs_len-y):
					wave_array[y][x]=wave_strs[x]
			n=0#每个字符开始移动的初始行数
			for x in range(strs_len):#对于字符串中的每个字符
				incre=0#每个字符的横向移动增量
				for y in range(n,len(wave_array)):#在字符的纵向移动范围中
					try:
						if wave_array[y][(strs_len-x)+(int((incre+1)*incre/2)-1)]==' ':#如果数组为空 就赋予对应的值
							wave_array[y][(strs_len-x)+(int((incre+1)*incre/2)-1)]=wave_strs[-x-1]
							#(strs_len-x)为字符横向移动初始索引 (int((incre+1)*incre/2)-1)为横向移动增量规律
						else:
							raise Exception#否则引发异常
					except Exception as e:#如果将要赋值的地方不为空 或者 移动超出数组横向范围
						if y>=strs_len:#如果纵向索引比字符长度大
							wave_array[y][-x-1]=wave_strs[-x-1]#赋予对应字符串的字符
					incre+=1#控制横向移动增量
				n+=1#控制移动行数
			for h in range(wave_height):
				for wave_line in wave_array:#写入上部分
					for s in range(wave_smoothness):
						for char in wave_line:
							f.write(char)
						f.write('\n')
				for wave_line in list(reversed(wave_array)):#写入下部分
					for s in range(wave_smoothness):
						for char in wave_line:
							f.write(char)
						f.write('\n')

		elif wave_form=='rotat':#旋转型
			#--------------此部分和离散型相同--------------
			wave_array=[[' 'for x in range(wave_width)] for y in range(strs_len+width+4)]#初始化离散型数组
			for y in range(strs_len):#先添加数组左上角的字符串
				for x in range(strs_len-y):
					wave_array[y][x]=wave_strs[x]
			n=0#每个字符开始移动的初始行数
			for x in range(strs_len):#对于字符串中的每个字符
				incre=0#每个字符的横向移动增量
				for y in range(n,len(wave_array)):#在字符的纵向移动范围中
					try:
						if wave_array[y][(strs_len-x)+(int((incre+1)*incre/2)-1)]==' ':#如果数组为空 就赋予对应的值
							wave_array[y][(strs_len-x)+(int((incre+1)*incre/2)-1)]=wave_strs[-x-1]
							#(strs_len-x)为字符横向移动初始索引 (int((incre+1)*incre/2)-1)为横向移动增量规律
						else:
							raise Exception#否则引发异常
					except Exception as e:#如果将要赋值的地方不为空 或者 移动超出数组横向范围
						if y>=strs_len:#如果纵向索引比字符长度大
							wave_array[y][-x-1]=wave_strs[-x-1]#赋予对应字符串的字符
					incre+=1#控制横向移动增量
				n+=1#控制移动行数
			#--------------此部分和离散型相同--------------
			for n in range(strs_len):#添加上部分
				wave_array.insert(n,wave_strs[:n+1]+' '*(wave_width-n-1))
			reversed_array=[]
			for line in wave_array:#把wave_array里的每项反向后在填充到reversed_array中
				reversed_array.append(list(reversed(line)))
			wave_mid=[]#旋转波浪中间部分
			for y in range(len(wave_array)-strs_len*2):#wave_array的下部分填充到旋转波浪中间部分
				wave_mid.append([])
				for x in range(wave_width):
					wave_mid[y].append(wave_array[strs_len*2+y][x])
			for y in range(len(wave_mid)):#reversed_array的上部分覆盖到旋转波浪中间部分
				for x in range(wave_width):
					if wave_mid[y][x]==' ':
						wave_mid[y][x]==reversed_array[y][x]
			result_array=[]
			for y in range(strs_len*2):#把wave_array wave_mid reversed_array 需要的部分填充到result_array
				result_array.append(wave_array[y])
			for y in range(len(wave_mid)):
				result_array.append(wave_mid[y])
			for y in range(strs_len,len(reversed_array)):
				result_array.append(reversed_array[y])
			for y in range(len(result_array)-strs_len,len(result_array)):#旋转表面修改
				for x in range(wave_width):
					if result_array[y][x]==' ':
						for z in range(x):
							result_array[y][z]=wave_strs[-z]
						break
			for h in range(wave_height):#输出
				for wave_line in range(strs_len,len(result_array)):#写入上部分
					for s in range(wave_smoothness):
						for char in range(wave_width):
							f.write(result_array[wave_line][char])
						f.write('\n')
	print('字符波浪wave_text.txt已生成')
build_wave()
#build_wave(strs='This is a tremendous wave',height=3,width=3,smoothness=3,form='whole')
#build_wave(strs='CharactersWave',height=3,width=8,smoothness=4,form='discr')
#build_wave(strs='TrixedWave',height=3,width=6,smoothness=3,form='rotat')
#仅供参考
