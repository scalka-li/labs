class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
    def manage_project(self):
        return f"{self.name} управляет проектами, отдел {self.department}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    def perform_maintenance(self):
        return f"{self.name} выполняет тех обслуживание, область {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        if not self.team:
            return "В команде нет сотрудников"
        result = f"Команда {self.name}:\n"
        for employee in self.team:
            result += f"- {employee.get_info()}\n"
        return result

employee = Employee("Ла Ла", 123)
manager = Manager("Бла Бла", 1234, "Отдел")
technician = Technician("Ня Ня", 4321, "Специализация")
tech_manager = TechManager("Пу Пу-Пу", 321, "ИТ", "База")

print(employee.get_info())
print(manager.get_info())
print(technician.get_info())
print(tech_manager.get_info())

print(manager.manage_project())
print(technician.perform_maintenance())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())
