class Employee:
    def __init__(self, name, emp_number):
        self.name = name
        self.emp_number = emp_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_emp_number(self):
        return self.emp_number

    def set_emp_number(self, emp_number):
        self.emp_number = emp_number


class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift, hourly_rate):
        super().__init__(name, emp_number)
        self.shift = shift
        self.hourly_rate = hourly_rate

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate


# create a list of ProductionWorker objects
workers = [
    ProductionWorker("John Doe", "123", 1, 20.0),
    ProductionWorker("Jane Smith", "456", 2, 22.0),
    ProductionWorker("Bob Johnson", "789", 1, 18.0),
]

# traverse the list and print out the content of the 3 ProductionWorker objects
for worker in workers:
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_emp_number())
    print("Shift:", worker.get_shift())
    print("Hourly Rate:", worker.get_hourly_rate())
    print()
