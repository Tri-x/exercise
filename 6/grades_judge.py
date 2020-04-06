from random import *
def judge_grade():
	grades_dict={
					'chinese':0,
					'math':0,
					'english':0,
					'biology':0,
					'chemistry':0,
					'physics':0,
					'total':0,
					}#初始成绩字典
	for subject,grades in grades_dict.items():#随机成绩
		if subject=='chinese'or subject=='math'or subject=='english':
			grades_dict[subject]=randint(1,150)
		if subject=='biology'or subject=='chemistry'or subject=='physics':
			grades_dict[subject]=randint(1,100)
	for grades in grades_dict.values():#总分累加
		grades_dict['total']+=grades
	grades_dict['total']=int(grades_dict['total']/2)#加了两次所以要除以二
	for subject,grades in grades_dict.items():#不同学科不同成绩类型
		if subject=='chinese'or subject=='math'or subject=='english':
			if grades>120:
				grades_dict[subject]=[grades,'A']
			if 120>=grades>90:
				grades_dict[subject]=[grades,'B']
			if 90>=grades>60:
				grades_dict[subject]=[grades,'C']
			if 60>=grades:
				grades_dict[subject]=[grades,'D']
		if subject=='biology'or subject=='chemistry'or subject=='physics':
			if grades>80:
				grades_dict[subject]=[grades,'A']
			if 80>=grades>60:
				grades_dict[subject]=[grades,'B']
			if 60>=grades>40:
				grades_dict[subject]=[grades,'C']
			if 40>=grades:
				grades_dict[subject]=[grades,'D']
		if subject=='total':
			if grades>650:
				grades_dict[subject]=[grades,'A']
			if 650>=grades>500:
				grades_dict[subject]=[grades,'B']
			if 500>=grades>350:
				grades_dict[subject]=[grades,'C']
			if 350>=grades:
				grades_dict[subject]=[grades,'D']
	print('|{0:10s}|{1:5s}|{2:5s}|'.format('Subject','Grade','Level'))#格式化输出
	for subject,grades in grades_dict.items():
		print('|{0:10s}|{1:<5d}|{2:5s}|'.format(subject.title(),grades[0],grades[1]))
judge_grade()
