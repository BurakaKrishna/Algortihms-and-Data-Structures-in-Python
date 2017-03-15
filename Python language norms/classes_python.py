class classFoo(object):
	@classmethod
	def hello(cls):
		print("hello from %s" % cls.__name__)

classFoo.hello()
classFoo().hello()
# no need of class instance/object for the classmethod
# arguments passed in it are cls 

class staticFoo(object):
    @staticmethod
    def hello(cls):
        print("hello from %s" % cls.__name__)
staticFoo.hello(classFoo().__class__)
staticFoo.hello(classFoo)
# no need of class instance/object for the staticmethod and it is not bound
# no arguments

class instanceFoo(object):
	def hello(self):
		print("hello from %s" % self.__class__.__name__)
instanceFoo().hello()