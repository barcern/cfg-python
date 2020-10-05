# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth
# Century, Seventies")

# Get user input
book_year = input("In which year was this book written? ")
book_year_int = int(book_year)

# First loop to find century
if book_year_int >= 1900:
    century = "Nineteenth Century"
elif book_year_int >= 1800:
    century = "Eighteenth Century"

# Second loop to find decade
if book_year[2] == '0':
    decade = "Noughties"
elif book_year[2] == '1':
    decade = "Tens"
elif book_year[2] == '2':
    decade = "Twenties"
elif book_year[2] == '3':
    decade = "Thirties"
elif book_year[2] == '4':
    decade = "Fourties"
elif book_year[2] == '5':
    decade = "Fifties"
elif book_year[2] == '6':
    decade = "Sixties"
elif book_year[2] == '7':
    decade = "Seventies"
elif book_year[2] == '8':
    decade = "Eighties"
else:
    decade = "Nineties"

output = century + ', ' + decade
print(output)