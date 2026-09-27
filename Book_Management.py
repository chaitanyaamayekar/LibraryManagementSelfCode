import json 
from pathlib import Path
import random
import string

class BookManagement:
    database = 'book.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No database found!")
    except Exception as err:
        print(f"Error occured as:{err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data,indent=4))

    @classmethod
    def __idgenerate(cls):
         alpha = random.choices(string.ascii_uppercase, k=2)
         digit = random.choices(string.digits, k=2)
        
         id_no = alpha + digit
         random.shuffle(id_no)
        
         return "B" + "".join(id_no)

    def AddBook(self):
        try:
            print("Enter the following details--")
            book_info ={
                "id" : BookManagement.__idgenerate(),
                "Title": input("Book Title: "),
                "Author": input("Author: "),
                "Category" : input("Category: "),
                "Copies" : int(input("Total Copies: ")),
                "Available" : int(input("Available: "))
            }
            for i in book_info:
                print(f"{i}:{book_info[i]}")
            BookManagement.data.append(book_info)
            BookManagement.__update()
            print("Book added successfully!")
        except Exception as err:
            print(f"Error occured as :{err}")

    def ViewBook(self):
        if not BookManagement.data[0]:
            print("No books found!")
            return
        print("-" * 118)
        print(f"{'id':<10}{'Title':<35}{'Author':<25}{'Category':<25}{'Copies':<10}{'Available':<10}")
        print("-" * 118)
        for i in BookManagement.data:
            print(
                f"{i['id']:<10}"
                f"{i['Title']:<35}"
                f"{i['Author']:<25}"
                f"{i['Category']:<25}"
                f"{i['Copies']:<10}"
                f"{i['Available']:<10}"
            )
        print("-" * 118)


    def SearchBook(self):
        try:
            print("Press the number to perform that operation")
            print("1. Title")
            print("2. Author")
            print("3. Category")
            opt = int(input("Which search You want to perform: "))
            if opt == 1:
                title = input("Enter Title of Book You Want: ")
                search = [i for i in BookManagement.data if i['Title'].lower() == title.lower()]

                if not search:
                    print("No such title found")
                else:
                    print("-" * 118) 
                    print( 
                        f"{'id':<10}" 
                        f"{'Title':<35}" 
                        f"{'Author':<25}" 
                        f"{'Category':<25}" 
                        f"{'Copies':<10}" 
                        f"{'Available':<10}" 
                    )
                    print("-" * 118)
                    for i in search:
                        print( 
                            f"{i['id']:<10}" 
                            f"{i['Title']:<35}" 
                            f"{i['Author']:<25}" 
                            f"{i['Category']:<25}" 
                            f"{i['Copies']:<10}" 
                            f"{i['Available']:<10}" 
                        )
                    print("-" * 118)   
                
            if opt == 2:
                author = input("Enter Author of Book You Want: ")
                search = [i for i in BookManagement.data if i['Author'].lower() == author.lower()]
                
                if not search:
                    print("No such Author found")
                else:
                    print("-" * 118) 
                    print( 
                        f"{'id':<10}" 
                        f"{'Title':<35}" 
                        f"{'Author':<25}" 
                        f"{'Category':<25}" 
                        f"{'Copies':<10}" 
                        f"{'Available':<10}" 
                    )
                    print("-" * 118)
                    for i in search:
                        print( 
                            f"{i['id']:<10}" 
                            f"{i['Title']:<35}" 
                            f"{i['Author']:<25}" 
                            f"{i['Category']:<25}" 
                            f"{i['Copies']:<10}" 
                            f"{i['Available']:<10}" 
                            )
                    print("-" * 118) 

            if opt == 3:
             category = input("Enter Category of Books You Want: ")
             search = [i for i in BookManagement.data if i['Category'].lower() == category.lower()]
                            
             if not search:
                print("No such Category found!")
             else:
                print("-" * 118) 
                print( 
                    f"{'id':<10}"
                    f"{'Title':<35}" 
                    f"{'Author':<25}" 
                    f"{'Category':<25}" 
                    f"{'Copies':<10}" 
                    f"{'Available':<10}" 
                    )
                print("-" * 118)
                for i in search:
                    print( 
                        f"{i['id']:<10}" 
                        f"{i['Title']:<35}" 
                        f"{i['Author']:<25}" 
                        f"{i['Category']:<25}" 
                        f"{i['Copies']:<10}" 
                        f"{i['Available']:<10}" 
                        )
                print("-" * 118)             
        except Exception as err:
            print(f"{err}")

    def UpdateBook(self):
        try:
            bookid = input("Enter Book ID to be updated: ")
            bookex = [ i for i in BookManagement.data if i['id'].lower() == bookid.lower()]

            if bookex == False:
                print("No Book Record Found, Recheck the ID.")
                return
            else:
                print("Following can be updated\n\n Title | Author | Category |")
                new_data ={
                    "Title": input("Book Title: "),
                    "Author": input("Author: "),
                    "Category" : input("Category: "),
                    }
                if new_data['Title'] == "":
                    new_data['Title'] = bookex[0]['Title'] 
                if new_data['Author'] == "":
                    new_data['Author'] = bookex[0]['Author']
                if new_data['Category'] =="":
                    new_data['Category'] = bookex[0]['Category']
                new_data['id'] = bookex[0]['id']
                new_data['Copies'] = bookex[0]['Copies']
                new_data['Available'] = bookex[0]['Available']
                for i in new_data:
                    if new_data[i] == bookex[0][i]:
                        continue
                    else:
                        bookex[0][i] = new_data[i]

                BookManagement.__update()
                print("Data Updated Successfully!")
        except Exception as err:
            print(f"{err}")

    def DeleteBook(self):
        try:
            bookid = input("Enter Book ID to be deleted: ")
            bookTitle = input("Enter The Title of Book to br deleted")
            bookex = [ i for i in BookManagement.data if i['id'] == bookid and i['Title'] == bookTitle]
            opt = input("Press Y to Delete\nPress N to Cancel Deletion.")
            if opt == 'N' or opt == 'n':
                pass
            else:
                index = BookManagement.data.index(bookex[0])
                BookManagement.data.pop(index)
                print("Account Deleted successfully !")
                BookManagement.__update()
        except Exception as err:
            print(f"{err}")

    def BookAvailability(self):
        pass 

    def TrackBook(self):
        pass

book = BookManagement()

print("--------------_BOOK_MANAGEMENT_--------------")
print(" (Press the number to perform the operation) ")
print("1. Add Book")
print("2. Veiw all Books")
print("3. Search Books")
print("4. Update Book Info")
print("5. Delete Book Record")
print("6. Check Book Availability")
print("7. Track Book copies")

check = int(input("Enter Operation Number: "))

if check == 1:
    book.AddBook()
if check == 2:
    book.ViewBook()
if check == 3:
    book.SearchBook()
if check == 4:
    book.UpdateBook()
if check == 5:
    book.DeleteBook()
if check == 6:
    book.BookAvailability()
if check == 7:
    book.TrackBook()