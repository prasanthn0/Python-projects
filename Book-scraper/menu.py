from app import books # can import variables too

USER_CHOICE="""Enter one of the following

-- 'a' : To see best rated books ,
-- 'b' : To see cheapest books ,
-- 'n' : To see the book next in catalogue ,
-- 'q' : To exit !

Enter your choice :  """



def best_books():
    best_books=sorted(books, key=lambda x:x.rating  * -1 )[:10]  #sorting will be in ascending order hence * -1
    for book in best_books:
        print(book)
    return

def lowest_rated_books():
    low=sorted(books,key=lambda x:x.rating)[:10]
    for book in low:
        print(book)
    return

def cheapest_books():
    cheapest_books=sorted(books,key=lambda x:x.price)[:10]
    for book in cheapest_books:
        print(book)
    return

def costly_books():
    costly_books=sorted(books,key=lambda x:x.price)[:10]
    for book in costly_books:
        print(book)
    return


#multiple sorting
def rating_price_sort():
    bookies=sorted(books,key=lambda x : (x.rating*-1,x.price) )[:10] #sorts by rating first and same star books are sorted by price.
    for book in bookies:
        print(book)

book_generator=(x for x in books)
def next_book():
    print(next(book_generator))

def menu():
    selection= input(USER_CHOICE)
    while selection != 'q':
        if selection == 'a':
            best_books()
        elif selection == 'b':
            cheapest_books()
        elif selection == 'n':
            next_book()
        else :
            print('Enter a valid command')


        selection = input(USER_CHOICE)

menu()