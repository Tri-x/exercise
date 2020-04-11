def get_num():#获取一个数字
	while True:#循环输入 直到用户输入一个正确值
		user_strs=input('请输入一个整数数字:\n')
		try:
			num=int(user_strs)#尝试把字符整数化
		except Exception as e:#如果出错
			print('只能输入整数数字')#提示
			continue#从头开始
		return num
number=get_num()#得到一个数字
class NumberError(Exception):pass#自定义异常
def strs_print(num):
	print('请输入'+str(num)+'个字符串:')#要求输入num个字符串
	i=1#第i个字符串
	while i<=num:
		brief='第'+str(i)+'个字符串:'
		str_input=input(brief)#提示
		try:
			str_list=str_input.split()#尝试以空格将输入值分割成两个字符串
			if len(str_list)!=2:#如果长度不为2
				raise NumberError('只能输入两个字符')#自定义异常提示
		except NumberError as ne:
			print(ne)
			continue#从头开始
		try:
			n1=int(str_list[0])
			n2=int(str_list[1])
		except ValueError as ve:#尝试把字符整数化
			print('只能输入数字')
			continue
		try:
			n=n1/n2
		except ZeroDivisionError as zd:#被除数不能为0
			print('第二个字符不能为0')
			continue
		print('结果:',str_list[0],'/',str_list[1],'=',str(n))
		i+=1#控制i值
strs_print(number)
