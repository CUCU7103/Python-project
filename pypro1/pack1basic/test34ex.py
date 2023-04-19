from abc import abstractmethod, ABCMeta


class Employee(metaclass=ABCMeta): # 추상 클래스로 설정하였다.
           
        def __init__(self,irum,nai):
            self.irum = irum
            self.nai = nai 
        
        
        @abstractmethod
        def pay(self):
            pass
        
        @abstractmethod
        def data_print(self):
            pass
        def irumnai_print(self):
            print('이름 {}, 나이 {}'.format(self.irum,self.nai),end =' ')
        
        
 
class Tempopary(Employee):
        
        def __init__(self,irum,nai,ilsu,ildang):
            super().__init__(irum, nai)
            self.ilsu = ilsu
            self.ildang =ildang
        
        def pay(self):
            mypay = self.ilsu * self.ildang
            return mypay
            # return = self.ilsu * self.ildang
        def data_print(self):
            super().irumnai_print()
            # print('이름 {} , 나이 {} , 월급 {}'.format(self.irum,self.nai,self.pay()))
            print(', 월급 {}'.format(self.pay()))
        
        
t = Tempopary('홍길동',25,20,15000)
t.data_print()

class Regular(Employee):
    
    def __init__(self, irum, nai, salary):
        self.salary = salary
        super().__init__(irum, nai)
     
    def pay(self):
        return self.salary
     
    def data_print(self):
        print('이름 {}, 나이 {}, 급여 {}'.format(self.irum, self.nai, self.pay()))

        
r = Regular('한국인', 27,3500000)
r.data_print()

class Salesman(Regular):
    rpay = 0
    def __init__(self,irum,nai,salary,sales,commission):
        self.sales = sales
        self.commission = commission
        super().__init__(irum,nai,salary)
        
        
    def pay(self):
        return super().pay() + self.sales * self.commission
        
        # spay = self.sales * self.commission
        # rpay = self.salary + spay
        # return rpay
        
    def data_print(self):
        super().irumnai_print()
        print(" 수령액 {}".format(self.pay()))
        
s = Salesman('손오공',29,1200000,5000000,0.25)
s.data_print()
    
    
           
