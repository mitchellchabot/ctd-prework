
# Book Recommendation

name = input("What is your name?")


book_type = str(input("What type of book do you want to read? (fiction / non-fiction)"))
book_genre = str(input("What genre of book do you want to read? (history / romance / science)"))
pages = int(input("What is the maximum amount of pages youd like to read?"))
recommendation = ""

if book_type == "fiction":
    if pages <= 200:
        if book_genre == "history":
            recommendation = "Of Mice and Men"
        if book_genre == "romance":
            recommendation = "Breakfast At Tiffany's"
        if book_genre == "science":
            recommendation = "Hitchhiker Guide to the Galaxy"
    elif pages > 200:
        if book_genre == "history":
            recommendation = "War and Peace"
        if book_genre == "romance":
            recommendation = "The Fault in our Stars"
        if book_genre == "science":
            recommendation = "1984"
            
# Book Recomendations for Non-Fiction
elif book_type == "non-fiction":
    if pages <= 200:
        if book_genre == "history":
            recommendation = "The Art of War"
        if book_genre == "romance":
            recommendation = "The Last Lecture"
        if book_genre == "science":
            recommendation = "On the Orgin of Species"
    elif pages > 200:
        if book_genre == "history":
            recommendation = "All Quite on the Western Front"
        if book_genre == "romance":
            recommendation = "Wild"
        if book_genre == "science":
            recommendation = "A Breif History of Time"
else:
    print("Unrecognizable: Sorry, please try again with criteria stated")

print(" ")
print("--------------")
print (" ")
print("Hi, " + name + "! Since you like " + book_type + " and " + book_genre + ",")
print("we reccomend the book " + recommendation)
