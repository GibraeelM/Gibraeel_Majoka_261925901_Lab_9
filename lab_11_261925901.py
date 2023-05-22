class Shape:
    def __init__(self, sides):
        self.sides = sides

    def ComputeArea(self):
        pass

class Square(Shape):
    def __init__(self, side_len):
        super().__init__(4)
        self.side_length = side_len

    def ComputeArea(self):
        return self.side_length * self.side_length
    
class Triangle(Shape):
    def __init__(self,height,base):
        super().__init__(3)
        self.height = height
        self.base = base

    def ComputeArea(self):
        area = 0.5 * self.base * self.height
        return area
    
def main():
    continue_op = True
    objs = []
    while continue_op:
        choice = input("1: Create Square, 2: Create Triangle, 3: Create Shape, 4: Quit")
        if choice == '1':
            side_len = float(input("Enter length of side: "))
            objs.append(Square(side_len))
        
        elif choice == '2':
            base = float(input("Enter base size: "))
            height = float(input("Enter height of the triangle: "))
            objs.append(Triangle(height,base))

        elif choice == '3':
            num_sides = int(input("Enter number of sides"))
            objs.append(Shape(num_sides))

        elif choice == '4':
            continue_op = False

        else:
            print("Please select a valid option")

    for obj in objs:
        print(obj.ComputeArea())

main()

    
#--------------Task 2------------
class Employee:
    def __init__(self, EmpName, EmpID, Salary):
        self.name = EmpName
        self.ID = EmpID
        self.salary = Salary

    def  SalaryStatus(self):
        print(self.salary)

class BuildingManager(Employee):
    def __init__(self,EmpName, EmpID):
        super().__init__(EmpName, EmpID, Salary=10_000)
        
class ProcurementManager(Employee):
    def __init__(self,EmpName, EmpID):
        super().__init__(EmpName, EmpID, Salary=12_000)

class LogisticsManager(Employee):
    def __init__(self,EmpName, EmpID):
        super().__init__(EmpName, EmpID, Salary=15_000)

def main():
    objs = []
    objs.append(BuildingManager('a',2))
    objs.append(Employee('v',3,2121))
    objs.append(ProcurementManager('oij',9))
    objs.append(LogisticsManager('efa',1))

    for obj in objs:
        obj.SalaryStatus()

main()

