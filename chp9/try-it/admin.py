from user import User
class Privilege: 
    def __init__(self):
        self.privileges = ['Add post', 'Delete post', 'Ban user']

    def show_privileges(self):
        print("Privileges: ")
        for privi in self.privileges:
            print(f"\t{privi}")

class Admin(User):
    def __init__(self):
        self.privilege = Privilege()