class EmpIdDescriptor():
    def __get__(self, obj, owner):
          return self.__empid
    def __set__(self, obj, value):
          if hasattr(obj, 'empid'):
               raise ValueError("'empid' is read only attribute")
          if not isinstance(value, int):
               raise TypeError("'empid' must be an integer.")
          self.__empid = value

class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value

class Employee():
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
        

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)
e1.empname = 'Williams'
print(e1.empid, '-', e1.empname)
#e1.empid = 76347322 
