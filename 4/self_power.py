#self power 自幂数 自幂数是指一个n位数,它的每个位上的数字的n次幂之和等于它本身 1~10位的自幂数都有各自的名称
self_power_dict={
						'1':'独身数',
						'2':'没有自幂数',
						'3':'水仙花数',
						'4':'四叶玫瑰数',
						'5':'五角星数',
						'6':'六合数',
						'7':'北斗七星数',
						'8':'八仙数',
						'9':'九九重阳数',
						'10':'十全十美数',
						}
def self_power(n):#n为位数
	if n==2:
		return print('两位数没有自幂数')
	nums_range=[str(10**(n-1)),str(10**n-1)]#数字范围
	print('在{}范围内,{}有:'.format('~'.join(nums_range),self_power_dict[str(n)]),end='')#格式化输出
	for num in range(10**(n-1),10**n):
		number_list=[]#每位数字的列表
		for x in range(n):#每位数字的位数
			number_list.append(int(str(num)[x])**n)#在数字列表中添加每位数字的n次方值
		if num==sum(number_list):#如果数字等于数字列表每位数字总和
			print(num,end=' ')
self_power(3)#这种算法运算较慢 仅供参考
