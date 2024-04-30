from django.shortcuts import render,HttpResponse,redirect
import mysql.connector as sql
from django.contrib import messages


m=sql.connect(host="localhost",user="root",passwd="Jitu_srp#121",database='website')
                                            # SIGNUP VIEW  
def SignupPage(request):
    fn,ln,r,em,pwd='','','','',''
    if request.method=="POST":
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="role":
                r=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,r,em,pwd)
        cursor.execute(c)
        m.commit()
        return redirect('login')

    return render(request,'sign_up.html')


#                                          LOGIN VIEW

def LoginPage(request):
    em,pwd,re='','',''
    if request.method=="POST":
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="role":
                re=value
        
        c="select * from users where email='{}' and password='{}' and role='{}'".format(em,pwd,re)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            messages.success(request, 'You have been logged in successfully!')
            first_name = t[0][0]
            return render(request,"home.html",context = {'first_name': first_name})

    return render(request,'login.html')


                                    # HOME VIEWS
    
def HomePage(request):
    return render(request, 'home.html')

                                    # HOME VIEWS
    
def AddBook(request):
    return render(request, 'add_book.html')

                                    # LOGOUT VIEWS

def LogoutPage(request):
    return redirect('login')

                                    # ADD_BOOK VIEWS

def AddBook(request):
    if request.method == "POST":
        cursor = m.cursor()
        d = request.POST
        book_id = d.get("bookId")
        book_name = d.get("bookName")
        book_detail = d.get("detail")
        author = d.get("author")
        publication = d.get("publication")
        branch = d.get("branch")
        price = d.get("price")
        quantity = d.get("quantity")
        book_photo = d.get("bookPhoto")

        query = "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (book_id, book_name, book_detail, author, publication, branch, price, quantity, book_photo)
        cursor.execute(query, values)
        m.commit()
        return redirect('book_report')

    return render(request, 'add_book.html')


def BookReport(request):
    cursor = m.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render(request, 'book_report_admin.html', {'books': books})