
import re
class Foodorder:
    users = []
        
    def __init__(self):
        self.status =" "
        self.user_details = {}
        self.food_info = {1:{"Name1":"Tandoori chicken","Quantity1":4,"Price1":240,"Discount1":0},2:{"Name2":"Vegan Burger","Quantity2":1,"Price2":320,"Discount2":0},3:{"Name3":"Truffle Cake","Quantity3":500,"Price3":900,"Discount3":0}}
   
    def admin_login(self,username,password):
        username = "admin"
        password = 12345678
        if username == "admin" and password ==12345678:
            print("Logged in successfully!!".center(100,'*'))
            ans = True
            while ans:
                choice = int(input("\n1. Show Food details\n2. Add Food\n3. Edit Food\n4. Stock\n5. Exit"))
                if choice ==1:
                    self.show_food()
                elif choice ==2:
                    self.add_food()
                elif choice ==3:
                    self.edit_food()
                elif choice ==4:
                    self.stock()
                elif choice ==5:
                    ans = False
            else:
                print("Something Went Wrong!!!!!!".center(100,"!")) 
        else:
            print("something went wrong".center(100,"*"))
    
    def show_food(self):
        print(self.food_info)
    def stock(self):
        print("The stock in restaurent:",1500)
        
    def add_food(self):
        a={}
        self.food_info[int(input('Enter the food_id'))]=a
        a["Name"]=input()
        a["Quantity"]= input()
        a["Price"] = input()
        a["Discount"]=input()
        
    def edit_food(self):
        x=int(input("Enter the id of Food item you want to Edit:"))
        if x not in self.food_info:
            print("There is no food item in this id")
            x=int(input("Enter the id of Food item you want to Edit:"))
        else:
            ans = True
            while ans:
                choice =int(input("\n1. Change the Name\n2. Change the quantity\n3. Change the price\n4. Change discount\n5. Delete the food item from the menu\n6. Exit"))
                if choice ==1:
                    self.food_info[x]["Name"]=input("Enter the name:")
                elif choice ==2:
                    self.food_info[x]["Quantity"] = input("Enter the Quantity:")
                elif choice==3:
                    self.food_info[x]["Price"] = input("Enter the Price:")
                elif choice ==4:
                    self.food_info[x]["Discount"]= input("Enter the Discount")
                elif choice ==5:
                    del self.food_info[x]
                elif choice ==6:
                    ans =False
           
        
    def register(self):
        if self.status!='R' or self.status!='L':
            print('Press R to register')
            self.status = input('Press R'.center(30,'*'))
            if self.status == 'R':
                Full_name = input('Enter your Full_name:').upper()
                Number = int(input('Enter your Phone_number:'))      
                Address=input('Enter your Address:')
                Email = input('Enter your Email_Address:')
                password = input('Enter your Password:')
                if len(password)<7:
                    print('\nPassword too short! \nPassword should contain at least 8 characters!')
                    password = input('Enter your Password:')
                if (re.search("[a-zA-Z]+[0-9]+.*@#",password)):
                    print('\nPassword must begin with an alphabet,must contain one special character and one or more digit.\nPlease re-enter your Password!!')
                    password = input('Enter your Password:')
                details = [Full_name,Number,Address,Email,password]
                print(details)
                Foodorder.users.append(details)
            self.user_details = Foodorder.users
            if self.user_details:
                return True
            return False
            
    def get_name(self):
        return self.name
    def set_name(self,Full_name):
        self.name = Full_name
        
    def get_number(self):
        return self.number
    def set_number(self,Number):
        self.number = Number
        
    def get_address(self):
        return self.address
    def set_name(self,Address):
        self.address = Address
        
    def get_email(self):
        return self.email
    def set_name(self,Email):
        self.email = Email
        
    def get_password(self):
        return self.password
    def set_name(self,password):
        self.password = password
                 
    def login(self):
        get = True
        self.status = input('Press L'.center(30,'*'))
        if self.status == 'L':
            Email = input('Enter your Email_Address:')
            Password = input('Enter your Password:')
            for i in self.user_details:
                if i[3]!=Email:
                    if i[4]!= Password:
                        print('You are not Registered,Please Register'.center(100,'*'))
                else:
                    print('Welcome to our Foodyzone Restaurant'.center(100,'-'))
                    while get:
                        self.choice = int(input('\n1. Place New Order\n2. History\n3. Update Profile\n4. Exit\nEnter the Number:'))
                    
                        if self.choice == 1:
                            self.order_list()
                        
                        elif self.choice == 2:
                            self.Order_history()
                        
                        elif self.choice ==3:
                            self.update()
                        
                        elif self.choice == 4:
                            get = False
                        
                        else:
                            print('\nNot Valid Choice, Try Again')
    def order_list(self):
        self.list_of_order ={}
        choice = True
        while choice:
            choose = int(input("\n1. Show Food Details\n2. Place order\n3. Exit\n Enter the Number"))
            if choose ==1:
                print(self.food_info)
            elif choose==2:
                for k in self.food_info:
                    print(k)
                    for a in self.food_info[k]:
                        print(a,":",self.food_info[k][a])
                    
                x=int(input("Enter the id of Food item you want to Order:"))
                if x in self.food_info:
                    self.list_of_order |= self.food_info[x]
                    print(self.food_info[x])
                    print("Your order has been successfully ordered!!!")
                    
                else:
                    print("There is no food item in this id")
                    x=int(input("Enter the id of Food item you want to Edit:"))
                    return
            elif choose == 3:
                choice = False
                    
            
                    
    def Order_history(self):
        print('Your order history'.center(100,'-'))
        print(self.list_of_order)
                
            
        
    def update(self):
        print('Your Profile'.center(100,'-'))
        print(Foodorder.users)
        for i in Foodorder.users:
            del i[0:3]
           
            Full_name = input("Enter your name:")
            Number = int(input('Enter your number:'))
            Address = input('Enter your address:')
            
            i.insert(0,Full_name)
            i.insert(1,Number)
            i.insert(2,Address)
            print(i)
            
            
    def menu(self):
        ans = True
        while ans:
            self.choice = int(input('\n1. Register\n2. Login\n3. Admin login\n0. Exit\nEnter the Number corresponding to what you want to choose:'))
            if self.choice == 1:
                self.register()
                
            elif self.choice == 2:
                self.login()
                
            elif self.choice==3:
                username = input("Enter username:")
                password = input("Enter your password")
                self.admin_login(username,password)
                
            elif self.choice == 0:
                ans = False
                
            else:
                print('\nNot Valid Choice, Try Again')
            
        
        
obj = Foodorder()
obj.menu()

