#Expense tracker
#Category wise expenses
#Functions to add expenses, sum, category wise breakdown



def add_expense():
    exp_amount=int(input("Enter the amount  "))
    exp_category=str(input("Enter the category  "))
    if exp_category not in expenses:
        expenses[exp_category]=[]
    expenses[exp_category].append(exp_amount)
        
def sum_expenses():
    choice2=int(input("1 for total sum \n2 for sum by category"))
    if choice2 == 1:
        sum=0
        for category in expenses:
            for i in expenses[category]:
                sum += i
        return sum
    if choice2 ==2:
        li=[]
        sum=0
        print( )
        cat=str(input("Choose the category you want to check "))
        if cat in expenses:
            for i in expenses[cat]:
                sum += i
        else:
            print("Category not present")
        return sum


def make_choice(choice):
    
    match choice:
        case '1':
            add_expense()
            return 
        case '2':
            sum=sum_expenses()
            print(sum)
            return 
        case '3':
            print(expenses)
            return 
        case 'q':
            print("Shutting down. Thank You")
            return 
        case _:
            print("Wrong choice. Try again")
            return 
        
expenses={}
choice='0'
while choice != 'q':
    print("##Expense Tracker##")
    print("1 to Add Expenses")
    print("2 to Sum Expenses")
    print("3 to Show Expenses")
    choice=str(input("Press q to quit\nEnter your choice:"))
    make_choice(choice)