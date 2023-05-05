#Wilson Xu, section 03, assignment 11 part 2

#construct a new Smartphone
class Smartphone:
    def __init__(self, capacity, name):
        self.capacity = capacity# store our capacity
        self.name = name# store our name
        self.apps = {}# store our apps
        self.report()# when a phone gets created, we need to call the report method

  # add a new app to the smartphone given an appname (string) and an appsize (integer)
    def add_app(self, appname, appsize):
        if appname in self.apps:
            print("Cannot add app: app already installed")
        elif appsize < 0:
            print("Cannot add app: size cannot be negative")
        elif appsize > self.get_available_space():
            print("Cannot add app: not enough available space")
        else:
            self.apps[appname] = appsize
            print(f"App {appname} was added successfully")

# removes an app from the phone based on appname (string)
    def remove_app(self, appname):
        if appname not in self.apps:
            print("Cannot remove app: app not currently installed")
        else:
            del self.apps[appname]# delete
            print(f"App {appname} was removed successfully")

 # resets the phone (removes all apps, gives the phone a name of "Untitled")
    def reset(self):
        self.apps = {}
        self.name = "Untitled"
        print("Phone has been reset")

# renames the phone
    def rename(self, new_name):
        self.name = new_name
        print("Phone has been renamed")

 # checks to see if an app is installed based on appname (string)
    def has_app(self, appname):
        return appname in self.apps

# returns the current space available on the phone (integer)
    def get_available_space(self):
        used_space = sum(self.apps.values())
        return self.capacity - used_space #substract

# prints a detailed report that describes the following
    def report(self):
        used_space = sum(self.apps.values())
        available_space = self.get_available_space()
        app_count = len(self.apps)
        print(f"Name: {self.name}")
        print(f"Storage capacity: {self.capacity} GB")
        print(f"Used space: {used_space} GB")
        print(f"Available space: {available_space} GB")
        print(f"Apps installed: {app_count}")
        if app_count > 0:
            for app, size in sorted(self.apps.items()):
                print(f"* {app} ({size} GB)")



#Main Program User Input
#a program that asks the user to create a new phone and then allows them to use all of the features in your class.
while True:
    size = input("Size of your new smartphone (32, 64 or 128 GB): ")
    if size.isdigit():
        size = int(size)
        if size in (32, 64, 128):#Size of your new smartphone (32, 64 or 128 GB)
            break
    print("Invalid size, try again")

name = input("Smartphone name: ")
print("Smartphone created!")
phone = Smartphone(size, name)


while True:
    action = input("\n(r)eport, (a)dd app, r(e)move app, re(s)et, re(n)ame or (q)uit: ").lower()
    if action == 'r':
        phone.report()
    elif action == 'a':
        app_name = input("App name to add: ")
        app_size = int(input("App size in GB: "))
        phone.add_app(app_name, app_size)
    elif action == 'e':
        app_name = input("App name to remove: ")
        phone.remove_app(app_name)
    elif action == 's':
        phone.reset()
    elif action == 'n':
        new_name = input("Enter a new name for your phone: ")
        phone.rename(new_name)
    elif action == 'q':
        print("Goodbye!") # end program
        break
    else:
        print("Invalid command, try again")



