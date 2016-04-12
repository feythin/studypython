#/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
	# 静态字段 
	live = True

	def __init__(self, name, age, sex):
		# 动态字段 只有对象可以访问，类不能访问
		self.name = name
		self.age = age
		self.sex = sex

	# 动态方法 只有对象可以访问，类不能访问
	def run(self):
		print 'running...'

	# 静态方法 好处：可以直接引用，不用创建对象
	@staticmethod
	def eat():
		print 'eat'

	# 属性装饰器
	@property
	def job(self):
		return self.__job

	@job.setter
	def job(self, value):
		if not isinstance(value, str):
			raise TypeError('must be string')
		self.__job = value


	@property
	def pay(self):
		self.__pay = 50000
		return self.__pay


	'''
	注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
	还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
	'''

feythin = Person('feythin', 18, 'man')
print feythin.live
print Person.live
print feythin.name
feythin.run()
feythin.eat()
Person.eat()
feythin.job = 'iter'
print feythin.job
print feythin.pay
