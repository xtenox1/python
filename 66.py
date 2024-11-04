class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'Company name: {self.name}, Location: {self.location}'


class InternetCompany(Company):
    def __init__(self, name, location, services, subscription_price):
        super().__init__(name, location)
        self._services = services
        self._subscription_price = subscription_price

    def get_name(self):
        return self.name
    def get_services(self):
        return self._services
    def get_subscription_price(self):
        return self._subscription_price
    def add_service(self, service):
        self._services.append(service)
    @staticmethod
    def display_info():
        print("This is an internet service company.")
    def display_company_details(self):
        print(f"Company Name: {self.get_name()}")
        print(f"Location: {self.location}")
        print(f"Services: {self.get_services()}")
        print(f"Subscription Price:{self.get_subscription_price()}")
    def total_users(self, towers):
        total = 0
        for tower in towers:
            total += len(tower._users)
        return total

    def display_towers_info(self, towers):
        print("Tower Information:")
        for tower in towers:
            tower.display_tower_details()
            tower.display_users()
            print("*" * 30)
class InternetTower:
    def __init__(self, tower_name, tower_height, tower_capacity, subscription_types):
        self._tower_name = tower_name
        self._tower_height = tower_height
        self._tower_capacity = tower_capacity
        self._subscription_types = subscription_types
        self._users = []

    def get_tower_name(self):
        return self._tower_name

    def get_tower_height(self):
        return self._tower_height

    def get_tower_capacity(self):
        return self._tower_capacity

    def add_user(self, user, subscription_type):
        if len(self._users) < self._tower_capacity:
            if subscription_type in self._subscription_types:
                self._users.append((user, subscription_type))
                print(f"User {user} with subscription type {subscription_type} was added to {self._tower_name}.")
            else:
                print(f"Subscription type {subscription_type} is not available in {self._tower_name}.")
        else:
            print("Cannot add new user, the tower is full.")

    def remove_user(self, user):
        for i in self._users:
            if i == user:
                self._users.remove(i)
                print(f"User {user} was removed from {self._tower_name}.")
                return
        print(f"User {user} is not found in {self._tower_name}.")

    def display_users(self):
        if self._users:
            print(f"Users in {self._tower_name}:")
            for user, subscription_type in self._users:
                print(f"- {user} (Subscription type: {subscription_type})")
        else:
            print(f"No users in {self._tower_name}.")
    def display_tower_details(self):
        print(f"Tower Name: {self.get_tower_name()}")
        print(f"Tower Height: {self.get_tower_height()} meters")
        print(f"Tower Capacity: {self.get_tower_capacity()} users")
        print(f"Available Subscription Types: {self._subscription_types}")

class AdvancedInternetTower(InternetTower):
    def __init__(self, tower_name, tower_height, tower_capacity, subscription_types, technology):
        super().__init__(tower_name, tower_height, tower_capacity, subscription_types)
        self._technology = technology

    def get_technology(self):
        return self._technology

    def display_tower_details(self):
        super().display_tower_details()
        print(f"Technology Used: {self.get_technology()}")
company1 = Company('compny', 'Basra')

company = InternetCompany("Fast Internet Company", "Riyadh", "High-Speed Internet", 50.0)

tower1 = InternetTower("City Tower", 20, 5, ["Basic", "Premium"])

tower2 = AdvancedInternetTower("High-Tech Tower", 25, 8, ["Basic", "Premium"], "5G")

tower1.add_user("abbas", "Basic")
tower1.add_user("ali", "Premium")
tower1.add_user("ahmed", "Basic")

tower2.add_user("moha1", "Premium")
tower2.add_user("moha2", "Basic")

InternetCompany.display_info()

company.display_company_details()

company.display_towers_info([tower1, tower2])

tower1.remove_user("abbas")
tower2.remove_user("moha1")

total_users = company.total_users([tower1, tower2])
print(f"Total number of users in both towers: {total_users}")