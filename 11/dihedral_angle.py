import math#引入math模块 计算角度用
class point(object):#定义空间点类
	"""docstring for point"""
	def __init__(self,x,y,z,name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
class plane(object):#定义平面类
	"""docstring for plane"""
	def __init__(self, A,B,C,name):
		self.points=[A,B,C]#一个平面三个点
		self.points_name=[A.name,B.name,C.name]#点的名字
		self.name = name#平面的名字
		self.n=[]#平面的法向量
	def isplane(self):#判断这三个点是否能构成平面
		coors=[[],[],[]]#三个点的xyz坐标分别放在同一个列表用来比较
		for _point in self.points:#对于每个点
			coors[0].append(_point.x)
			coors[1].append(_point.y)
			coors[2].append(_point.z)
		for coor in coors:
			if coor[0]==coor[1]==coor[2]:#如果三个点的x或y或z坐标相等 则不能构成平面
				return print('Points:',*self.points_name,'cannot form a plane')
	def normal(self):#获得该平面的法向量
		self.isplane()#获得该平面的法向量前提是能构成平面
		A,B,C=self.points#对应三个点
		AB=[B.x-A.x,B.y-A.y,B.z-A.z]#向量AB
		AC=[C.x-A.x,C.y-A.y,C.z-A.z]#向量AC
		B1,B2,B3=AB#向量AB的xyz坐标
		C1,C2,C3=AC#向量AC的xyz坐标
		self.n=[B2*C3-C2*B3,B3*C1-C3*B1,B1*C2-C1*B2]#已知该平面的两个向量,求该平面的法向量的叉乘公式
	def angle(self,P2):#两个平面的夹角
		x1,y1,z1=self.n#该平面的法向量的xyz坐标
		x2,y2,z2=P2.n#另一个平面的法向量的xyz坐标
		cosθ=((x1*x2)+(y1*y2)+(z1*z2))/(((x1**2+y1**2+z1**2)**0.5)*((x2**2+y2**2+z2**2)**0.5))#平面向量的二面角公式
		degree=math.degrees(math.acos(cosθ))
		if degree>90:#二面角∈[0°,180°] 但两个平面的夹角∈[0°,90°]
			degree=180-degree
		return print('平面',self.name,P2.name,'的夹角为'+str(round(degree,5))+'°')
		#round(数值,四舍五入位数) math.degrees(弧度)将弧度转换为角度 math.acos(数值)返回该数值的反余弦弧度值

#测试
print('-'*25)
A=point(0,0,1,'A')#六个点
B=point(1,0,1,'B')
C=point(1,1,0,'C')
P1=plane(A,B,C,'P1')#p1平面
D=point(0,1,1,'D')
E=point(1,1,1,'E')
F=point(0.5,0,0,'F')
P2=plane(D,E,F,'P2')#p2平面
P1.normal()#求平面p1 p2的法向量
P2.normal()
P1.angle(P2)#求平面p1 p2的夹角

print('-'*25)
G=point(2,0,0,'G')#六个点
H=point(0,0,0,'H')
I=point(0,3,3**0.5,'I')
P3=plane(G,H,I,'P3')#p3平面
J=point(2/3,4/3,0,'J')
K=point(0,0,0,'K')
L=point(0,3,3**0.5,'L')
P4=plane(J,K,L,'P4')#p4平面
P3.normal()#分别求平面p3 p4的法向量
P4.normal()
P3.angle(P4)#求平面p3 p4的夹角

print('-'*25)
M=point(0,1,0,'M')#六个点
N=point(0,0,0,'N')
O=point(1,1,1,'O')
P5=plane(M,N,O,'P5')#p1平面
Q=point(0,0,2,'Q')
R=point(0,0,0,'R')
S=point(1,1,1,'S')
P6=plane(Q,R,S,'P6')#p2平面
P5.normal()#求平面p1 p2的法向量
P6.normal()
P5.angle(P6)#求平面p1 p2的夹角

print('-'*25)
T=point(12.6,-1,63,'T')#六个点
U=point(0,7,8,'U')
V=point(11,9,83.2,'V')
P7=plane(T,U,V,'P7')#p1平面
W=point(45,2,13,'W')
X=point(9,10,-56,'X')
Y=point(0.5,-7,1,'Y')
P8=plane(W,X,Y,'P8')#p2平面
P7.normal()#求平面p1 p2的法向量
P8.normal()
P7.angle(P8)#求平面p1 p2的夹角
