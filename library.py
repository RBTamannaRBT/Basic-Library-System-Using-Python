reg=input("Already registered? Y/N \n") 
book={
    'CSE':['java','python','c','c++','javascript','html','css'] ,
    'Math':['calculus','algebra','trigonometry','geometry'],
    'Physics':['conductor','current','collission','metaphysics'],
    'English':['literature','reading','writing','speaking','listening','grammer']
}
c=0
student={
    'rbt':{
        'name': 'rbt',
        'student_id':'18',
        'password':'123'
    }
}
if reg=='Y':
    user=input('Enter your user name \n')
    password=input('Enter your password \n')
    if student[user]['password']==password:
        print('Welcom to RBT Library')
        search=input('Would you like to watch book category? or search by name? please write category or name accordingly \n')
        if search=='category':
            print(list(book.keys()))
            cat=input('which category books you are looking for \n')
            print(book[cat])
            bname=input('which book do you want to read? \n')
            if bname in book[cat]:
                print('Here the book pdf will open and user will be able to read')
        else:
            bname=input('Please enter the book name looking for \n')
            if bname in book:
                print('Here the book pdf will open and user will be able to read')
            else:
                print('Sorry this book is not available in our library, You can check our categories. Thank you.')
    else: 
        print('wrong password')
else:
    print('Please register')
    name=input('Enter your name \n')
    student_id= input('Enter your id \n')
    user= input('Enter a unique user name \n')
    password=input('Enter a password and memorize it \n')
    if student_id and user not in student:
        student[user]={
            'name': name,
            'student_id': student_id,
            'password': password
        }
    else:
        print('already registered with this id or username')
        user=input('Enter your user name \n')
    password=input('Enter your password \n')
    if student[user['password']]==password:
        print('Welcom to RBT Library')
        search=input('Would you like to watch book category? or search by name? please write category or name accordingly \n')
        if search=='category':
            print(list(book.keys()))
            cat=input('which category books you are looking for \n')
            print(book[cat])
            bname=input('which book do you want to read? \n')
            if bname in book:
                print('Here the book pdf will open and user will be able to read')
        else:
            bname=input('Please enter the book name looking for \n')
            if bname in book:
                print('Here the book pdf will open and user will be able to read')
            else:
                print('Sorry this book is not available in our library, You can check our categories. Thank you.')
    else: 
        print('wrong password')

