from random import *
import os #引入必要模块
class supermarket():#定义超市
	def __init__(self):
		#初始化超市物品字典
		self.goods_dicts={
						'food':{
								'candy':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'latiao':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'fruit':{
										'grape':{'num':0,
												'price':0,
												'code':'0000',
												},
										'banana':{'num':0,
												'price':0,
												'code':'0000',
												},
										'apple':{
												'green apple':{
															'num':0,
															'price':0,
															'code':'0000',
															},
												'red apple':{
															'num':0,
															'price':0,
															'code':'0000',
															},
												},
										},
								},
						'clothes':{
								'shirt':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'trousers':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'vest':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'underwear':{
											'purple underwear':{
																'num':0,
																'price':0,
																'code':'0000',
																},
											'red purple':{
														'num':0,
														'price':0,
														'code':'0000',
														},
											},
								},
						'furniture':{
								'stool':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'chair':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'table':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'cabinet':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'bed':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								},
						'office':{
								'pen':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'book':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'paper':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								'computer':{
										'num':0,
										'price':0,
										'code':'0000',
										},
								},

						}
		#初始化操作指令字典
		self.commands_dicts={
							'O':{
								'prompt':'显示所有指令',
								'order':self.show_commands
								},
							'S':{
								'prompt':'显示所有商品',
								'order':self.show_goods
								},
							'P':{
								'prompt':'显示购物单',
								'order':self.show_cart
								},
							'C':{
								'prompt':'清空购物单',
								'order':self.clear_cart
								},
							'A':{
								'prompt':'编辑购物单',
								'order':self.edit_goods
								},
							'F':{
								'prompt':'提交购物单',
								'order':self.submit_cart
								},
							'E':{
								'prompt':'离开超市',
								'order':self.exit_sp
								},
							}
		self.nums_list=[]#初始化物品数量列表
		self.nums_change_list=[]#初始化物品改变数量列表
		self.prices_list=[]#初始化物品价格列表
		self.codes_list=[]#初始化物品条码列表
		self.names_list=[]#初始化物品名字列表
		self.code_num=1#初始化物品条码值
		self.wallet=randint(30,200)#初始化钱包值
		self.welcome='欢迎光临Trix超市!请输入操作指令:'
		self.bye='谢谢光临Trix超市!'
		self.goods_cart_dict={}#初始化购物单字典
		self.good_cart_nums_list=[]#初始化购物单物品数量列表
	def sp_in(self):#超市初始化
		def goods_attributes_loops(loops_dicts):#函数循环处理超市物品字典
			for loop_dict_name,loop_dict in loops_dicts.items():
				if not isinstance(list(loop_dict.values())[0],dict):#如果list(loop_dict.values())的第一个值不是dict类型 isinstance(值,类型)判断值的类型
					loop_dict['num']=randint(0,20)#物品随机数量
					loop_dict['price']=round(uniform(1,50),1)#物品随机价格 round(值,四舍五入的位数)四舍五入 uniform(range)随机小数
					loop_dict['code']=str(self.code_num).zfill(4)#物品条码 str.zfill(位数)补零
					self.nums_list.append(loop_dict['num'])#将数量 价格 条码分别添加到对应的列表
					self.nums_change_list.append(loop_dict['num'])
					self.prices_list.append(loop_dict['price'])
					self.codes_list.append(loop_dict['code'])
					self.names_list.append(loop_dict_name)
					self.code_num+=1
				else:
					goods_attributes_loops(loop_dict)#控制函数循环
		goods_attributes_loops(self.goods_dicts)
		print(self.welcome)
	def show_commands(self):#显示指令
		for letter,letter_dict in self.commands_dicts.items():
			print('|{0}:{1}'.format(letter,letter_dict['prompt']),end='')#str.format()格式化输出
		print('|')
	def command_detect(self):#指令检测
		input_letter=input('').upper().strip()#将接收的输入转为大写去头尾空格
		if input_letter not in self.commands_dicts:#如果接收值不在指令字典中
			print('请输入正确指令!')
			self.show_commands()
		else:
			self.commands_dicts[input_letter]['order']()#如果接收值在指令字典中就调用该字母对应的指令
	def show_goods(self):#显示物品
		def print_classes_loops(loops_dicts):#函数循环处理显示物品
			global types_row#全局化变量types_row
			for loop_dict_key,loop_dict_value in loops_dicts.items():
				if not isinstance(list(loop_dict_value.values())[0],int):#如果list(loop_dict_value.values())的第一个值不是int类型
					loop_dict_key=loop_dict_key+':'#显示物品的格式化输出
					types_row='|{:20s}|{:8s}|{:8s}|{:8s}|'.format(loop_dict_key.upper(),'NUM','PRICE','CODE')#显示物品属性名字
					print('—'*len(types_row))
					print(types_row)
					print_classes_loops(loop_dict_value)#控制函数循环
				else:#如果list(loop_dict_value.values())的第一个值不是int类型
					#格式化打印物品属性
					print('|{:20s}|{:<8d}|{:<8.1f}|{:8s}|'.format(loop_dict_key.title(),loop_dict_value['num'],loop_dict_value['price'],loop_dict_value['code']))
		print_classes_loops(self.goods_dicts)
		print('—'*len(types_row))
		self.show_commands()
	def show_cart(self):#显示购物单
		line_length=len('|||||')+20+8+8+8#格式化输出购物单
		global good_total_price#全局化变量good_total_price
		good_total_price=0
		for good_name,good_attributes in self.goods_cart_dict.items():
			good_total_price+=int(good_attributes[0])*float(good_attributes[1])#总价计算
		print('—'*line_length)
		print('|{:20s}|{:8s}|{:8s}|{:8s}|'.format('CLASS','NUM','PRICE','CODE'))#显示物品属性名字
		for good_name,good_attributes in self.goods_cart_dict.items():
			cart_types_row='|{:20s}|{:<8d}|{:<8.1f}|{:8s}|'.format(good_name.title(),good_attributes[0],good_attributes[1],good_attributes[2])
			print(cart_types_row)#格式化打印物品属性
		print('—'*line_length)
		print('|Wallet:{0:>13.1f}{1}{2:>20.1f}|'.format(float(self.wallet),'|Total:',good_total_price))
		print('—'*line_length)
		self.show_commands()
	def clear_cart(self):#清空购物单
		self.goods_cart_dict.clear()
		self.show_commands()
	def edit_goods(self):#编辑购物单
		input_edits_list=input('请输入编辑物品的数量及条码(格式:NUM CODE ···):\n').split(' ')
		if len(input_edits_list)%2!=0:#判断长度
			print('请输入正确格式!')
			self.show_commands()
			return#不正确格式返回
		for n in range(int(len(input_edits_list)/2)):#对输入的 数量大小和条码正误判断
			if int(input_edits_list[n*2])<0 or (int(input_edits_list[n*2])>self.nums_list[self.codes_list.index(input_edits_list[n*2+1])]) or (input_edits_list[n*2+1] not in self.codes_list):
				print('请输入正确数量或条码!')
				self.clear_cart()
				return#不正确格式返回
			correspond_index=self.codes_list.index(input_edits_list[n*2+1])#对应索引值等于输入值中的条码在超市物品条码列表中的索引
			self.good_cart_nums_list.append(0)#先在self.good_cart_nums_list中添加0做计算的占位值
			#self.goods_cart_dict={'物品名字':[数量,价格,条码],'物品名字':[数量,价格,条码]···}
			self.goods_cart_dict[self.names_list[correspond_index]]=[int(input_edits_list[n*2]),self.prices_list[correspond_index],input_edits_list[n*2+1]]
			self.good_cart_nums_list[n]=self.goods_cart_dict[self.names_list[correspond_index]][0]#购物单物品数量列表中的第n个值等于goods_cart_dict中物品名字的数量
			self.nums_change_list[correspond_index]=self.nums_list[correspond_index]-self.good_cart_nums_list[n]#数量改变列表等于超市物品初始时的数量减去输入的对应物品数量
		def goods_nums_change_loops(loops_dicts):#函数循环处理物品数量改变
			for loop_dict in loops_dicts.values():
				if not isinstance(list(loop_dict.values())[0],dict):#如果list(loop_dict.values())的第一个值不是dict类型
					if loop_dict['num']!=self.nums_change_list[self.codes_list.index(loop_dict['code'])]:#如果超市的物品数量不等于改变量
						loop_dict['num']=self.nums_change_list[self.codes_list.index(loop_dict['code'])]
				else:
					goods_nums_change_loops(loop_dict)#控制循环
		goods_nums_change_loops(self.goods_dicts)
		self.show_cart()
	def submit_cart(self):#提交购物单
		if good_total_price<=self.wallet:#物品总价小于钱包值
			self.wallet=self.wallet-good_total_price
			self.show_cart()
			self.goods_cart_dict.clear()
			print('你可以选择继续购买或者离开超市')
		else:
			self.show_cart()
			print('你没有足够的钱来买这么多东西!请删除一些物品!')
	def exit_sp(self):#离开超市
		print(self.bye)
		os._exit(0)#退出程序
trix_sp=supermarket()#超市实例化
trix_sp.sp_in()#超市初始化
trix_sp.show_commands()#显示指令
while True:#在循环中处理
	trix_sp.command_detect()#检测指令
