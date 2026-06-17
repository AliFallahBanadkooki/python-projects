import csv 

class Task():
    def __init__(self , name , descript , prior):
        self.name =name 
        self.descript = descript
        self.prior = prior

class Todo():
    def __init__(self):
        self.LIST = []
    
    def add (self , act):
        self.LIST.append(act)
        return "task is added to the list"
    
    def remove (self , act ):
        for i in self.LIST:

            if i.name == act :
                self.LIST.remove(i)
                return "task is removed from the list"
        return f"ERROR : {act} is  not found in the list!"
    
    def show(self):
        if len(self.LIST) == 0 :
            return "no task found in the list"
        else:
            result = ""
            for i in self.LIST:
                result += (f"Name: {i.name} | "
                f"Description: {i.descript} | "
                f"Priority: {i.prior}")
            return result
                
    def save(self):
        with open ("TODOLIST.csv" , "w") as f:
            csvw = csv.writer(f)
            csvw.writerow(["name" , "description" , "priority"])
            for n in self.LIST:
                csvw.writerow([n.name , n.descript , n.prior])

todo = Todo()


while True:
    h_input = int(input("-------------\n1.Add a task \n2.Remove a task \n3.Show all tasks \n4.Save \n5.Exit! \nwrite your choice: "))

    if h_input == 1:
        name = input("please write your task : ")
        descript = input("description: ")
        prior = input("what's the priority? (High/mid/low)")
        the_task = Task(name , descript , prior)
        print(todo.add(the_task))
    elif h_input ==  2:
        Rname = input("please write your task to remove : ")
        print(todo.remove(Rname))
    elif h_input == 3:
        print(todo.show())
    elif h_input == 4:
        print(todo.save())
    elif h_input == 5:
        print(todo.save())
        print("Goodbye!")
        break
    #exiting the program will auotomatically saves the todo list
    else:
        print("INVALID CHOICE!")
