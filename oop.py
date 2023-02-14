class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')


class Driver:
    number_of_drivers = 0
    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking

class Race:
    def __init__(self, name, driver_limit, drivers=[]):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = drivers

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)
            return True
        else:
            return False
          
    def get_average_ranking(self):
        total = 0
        for driver in self.drivers:
            total += driver.get_ranking()
        return total / len(self.drivers)

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

s0 = Driver('Dale Earnhardt', 29, 100)
s1 = Driver('Lewis Hamilton', 36, 83)
s2 = Driver('Eliud Kipchoge', 36, 95)
s3 = Driver('Sebastian Vettel', 34, 76)
s4 = Driver('Ayrton Senna', 34, 99)

my_course.add_driver(s0)
my_course.add_driver(s1)
my_course.add_driver(s2)
my_course.add_driver(s3)
my_course.add_driver(s4)



my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())
print(my_course.get_average_ranking())

