
class visitorManagementSystem:
    company = "Kaizentrix Global Solutions"

    def __init__(self):   #here i created the properties which need to be stored in heap since if should be initially present before assigning any values to it
        #If not initialized the properties here you will get an attribute error bcz outside visitor check in during the check out we cannot use it
        #Bcz pvm ended up executing a method activation response holding these variables will be deleted
        self.id = ""
        self.name = ""
        self.mob_no = ""
        self.to_meet = ""
        self.department = ""  
        self.purpose = ""
        self.entry_time = 0  #entry time starts from zero
        self.exit_time = None   # none--> nothing we cannot consider the exit time before we check in that is before entry time
        self.checked_in = False   #make check in false bcz the we are not sure that user will check in, they may check guidelines also

    def visitorCheckIn(self, id, name, mob, meet, department, purpose, entry_time):
        self.id = id
        self.name = name
        self.mob_no = mob
        self.to_meet = meet
        self.department = department
        self.purpose = purpose
        self.entry_time = entry_time
        self.checked_in = True

        print("\nVisitor checked in successfully!")
        print("Welcome,", self.name)


    def visitorCheckOut(self, exit_time):
        if not self.checked_in:
            print("Please check in first.")
            return

        self.exit_time = exit_time
        duration = self.exit_time - self.entry_time

        print("\n======= Visitor Summary =======")
        print("Visitor ID       :", self.id)
        print("Visitor Name     :", self.name)
        print("Company          :", self.company)
        print("Mobile           :", self.mob_no)
        print("Person to Meet   :", self.to_meet)
        print("Department       :", self.department)
        print("Purpose          :", self.purpose)
        print("Entry Time       :", self.entry_time)
        print("Exit Time        :", self.exit_time)
        print("Visit Duration   :", duration, "Hours")

        self.checked_in = False
        print("\nVisit completed successfully!")
        print("Thank you. Visit again!")


    def visitorGuidelines(self):
        print("\n======= Visitor Guidelines =======")
        print("1. Wear your Visitor ID Card.")
        print("2. Photography and videography is not allowed.")
        print("3. Follow company security rules.")
        print("4. Smoking and drinking alcohol is prohibited.")
        print("5. Collect your visitor card for the valid visit.")
        print("6. Return your Visitor Pass before leaving.")
        print("7. Report to Reception while exiting.")
        print("8. Use dustbins and help us for clean environment.")
        print("===="*30)


print("****"*40)
print("KAIZENTRIX GLOBAL SOLUTIONS")
print("Corporate visitor management system")
print("****"*40)



f1 = visitorManagementSystem()

while True:  #While true it should ask every time the choices whether the visitor will proceed with any of the choices

    print("\n1. Visitor Check-In \n2. Visitor Check-Out \n3. Visitor Guidelines \n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter your Visitor ID: ")
        name = input("Enter your name: ")
        mob = input("Enter your mobile number: ")
        meet = input("Enter the person you want to meet: ")
        department = input("Enter the department: ")
        purpose = input("Enter the purpose of your visit: ")
        entry_time = int(input("Enter entry time (0-23): "))

        if entry_time < 0 or entry_time > 23:
            print("Invalid entry time.")
            continue

        f1.visitorCheckIn(id, name, mob, meet,department, purpose, entry_time)  #call the check-in method with the reference variable of the object/class


    elif choice == "2":
        if not f1.checked_in:    #Sandhya ma'am told no need but without checking in how user can checkout..?
            print("Please check in first.")
            continue

        while True:
            exit_time = int(input("Enter exit time (0-23): "))
        
            if exit_time < 0 or exit_time > 23 or exit_time<f1.entry_time:   #Like visitor should enter the valid exit time that is between 0 to 23 and they cannot exit before they actually checked in time
                print("Invalid exit time.")
                continue
            f1.visitorCheckOut(exit_time)  #Go for visitor checkout method and execute the provided code
            break

    elif choice == "3":
        f1.visitorGuidelines()

    elif choice == "4":
        print("Thank you for using KGS Visitor Management System.")
        break

    else:
        print("Invalid choice. Please select the option among 1,2,3,4.")
