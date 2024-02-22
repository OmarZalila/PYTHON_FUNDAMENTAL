class User :
    def __init__(self , first_name , last_name , email , age ):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"{self.first_name} {self.last_name} {self.email} {self.age}")
    def enroll(self):
        self.is_rewards_member=True
        self.gold_card_points=200
    def spend_points(self, amount):
        self.gold_card_points-=amount




person = User("joe","doe","joe@gmail.com",30)
person_1 = User("killy","bran","killy@gmail.com",30)
person_2 = User("stephan","bernard","stephan@gmail.com",30)
person.display_info()
person.enroll()
print(person.is_rewards_member)
print(person.gold_card_points)
person.spend_points(50)
print(person.gold_card_points)
person_2.enroll()
person_2.spend_points(80)
person.display_info()
person_1.display_info()
person_2.display_info()
