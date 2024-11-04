def mainfunc():
 book_titles = []
 for i in range(10):
    title = input(f"Enter the title of book {i + 1}: ")
    New_title=title[0].upper() + title[1:]
    book_titles.append(New_title)
    print(New_title)

mainfunc()
    
 