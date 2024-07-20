##class Car:
##    model = "BMW"
##    color = "white"
##    def speedChange(self,v):
##        print("speedChange",v)
##        self.speed = v
##bmw = Car()
##bmw.speedChange(20)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##class Car:
##    model = "BMW"
##    color = "white"
##bmw = Car()
##benz=Car()
##benz.model= "Benz"
##benz.color = "Black"
##print(benz.model)
##print(benz.color)
##print(bmw.model)
##print(bmw.color)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##class Car:
##    count = 0
##    speed =0
##    def speedChange(self,v):
##        Car.count+= 1
##        self.speed = v
##bmw = Car()
##benz = Car()
##bmw.speedChange(100)
##print("bmw speed :", bmw.speed)
##print('number of speedChange : ' ,Car.count)
##benz.speedChange(120)
##print("benz speed :", benz.speed)
##print('number of speedChange : ' ,Car.count)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##class Car:
##    def __init__(self,model,color):
##        self.model = model
##        self.color = color
##    def info(self):
##        print("model :",self.model,",color :",self.color)
##bmw = Car("BMW",'white')
##bmw.info()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##class Car:
##    def __init__(self,model,color,wheel):
##        self.model = model
##        self.color = color
##        self.wheel = wheel
##    def info(self):
##        print("model :",self.model,",color :",self.color,",wheel:",self.wheel)
##bmw = Car("BMW",'white',4)
##bmw.info()
##benz = Car("Benz",'Black',4)
##benz.info()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##class Car:
##    def __init__(self,model,color):
##        self.model = model
##        self.color = color
##    def info(self):
##        print("model :",self.model,",color :",self.color)
##class CarDrive(Car):
##    def speedChange(self,v):
##        self.speed = v
##        print("speedChange:",self.speed)
##bmw = CarDrive("BMW",'white')
##bmw.info()

##class Character:
##    def __init__(self,name,weapon):
##        self.name = name
##        self.weapon = weapon
##        def intro(self):
##            print("name :",self.name)
##            print("weapon :",self.weapon)
##lugo = Character("Lugo","gun")
##intro(lugo)


