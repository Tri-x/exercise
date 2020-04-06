class point(object):#定义平面点类
	"""docstring for point"""
	def __init__(self,x,y,name):
		self.x = x
		self.y = y
		self.name = name
	def distance(self,p2):#两点距离公式
		self.d=((self.x-p2.x)**2+(self.y-p2.y)**2)**0.5
		return self.d
	def getd(self,p2):#获取两点距离
		self.distance(p2)
		print('The distance of ({},{}) and ({},{}) is {} '.format(self.x,self.y,p2.x,p2.y,self.d))
	def istriangle(self,p2,p3):#判断这三点能否形成一个三角形
		self.l_list=[]#先获取这三点构成的三条线段的长度
		self.l_list.append(self.distance(p3))
		self.l_list.append(p2.distance(p3))
		self.l_list.append(self.distance(p2))
		self.l_list.sort()#线段长度由小到大排序
		if (self.l_list[0]+self.l_list[1]>self.l_list[2]) and (self.l_list[1]+self.l_list[2]>self.l_list[0]) and (self.l_list[2]+self.l_list[0]>self.l_list[1]):#长度判断
			return 'can'
		else:
			return 'can not'
	def getresult(self,p2,p3):#获取能否形成三角形的结果
		result=self.istriangle(p2,p3)
		print('Points:',self.name,p2.name,p3.name,result,'form a triangle')
	def whichtriangle(self,p2,p3):#判断是哪种三角形
		result=self.istriangle(p2,p3)
		if result=='can not':
			return print('Points:',self.name,p2.name,p3.name,result,'form a triangle')
		if self.l_list[0]**2+self.l_list[1]**2>self.l_list[2]**2:#锐角
			print('Points:',self.name,p2.name,p3.name,result,'form a acute triangle')
		elif self.l_list[0]**2+self.l_list[1]**2==self.l_list[2]**2:#直角
			print('Points:',self.name,p2.name,p3.name,result,'form a right triangle')
		elif self.l_list[0]**2+self.l_list[1]**2<self.l_list[2]**2:#钝角
			print('Points:',self.name,p2.name,p3.name,result,'form a obtuse triangle')
#测试
p1=point(12,-5,'p1')
p2=point(16,18,'p2')
p3=point(9,7,'p3')
p1.getd(p2)
p1.getresult(p2,p3)
p1.whichtriangle(p2,p3)
print()

p5=point(0,3,'p5')
p6=point(4,0,'p6')
p7=point(0,0,'p7')
p5.getd(p6)
p5.whichtriangle(p6,p7)
print()

p8=point(10,3,'p8')
p9=point(4,3,'p9')
p10=point(-9,0,'p10')
p8.getd(p9)
p8.whichtriangle(p9,p10)
