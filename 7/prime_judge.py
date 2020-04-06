from random import *
#素数
prime_list=[]
def if_prime(x):#判断x是否为素数
	n=2
	while n<x:
		if x%n==0:#如果x/2无余数直接返回
			return
		if x%n!=0:#如果x/2有余数
			n+=1#就测试下一个除数值
			if n==x-1:#如果x/(x-1)仍然有余数
				prime_list.append(str(x))#那么x就为素数 素数列表添加该值
for x in range(1000,10000):#对100~1000范围内每个值测试
	if_prime(x)
print('在1000~10000范围内,有{0}个素数,分别为:{1}'.format(len(prime_list),' '.join(prime_list)))
#''.join(list)表示用''连接list中的每个值
