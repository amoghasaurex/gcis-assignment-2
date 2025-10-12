
def check_limit(borrowerd):
    """
    This functions checks if the number of borrowed books 
    is within the limit and return appropriate message.
    """

    if borrowerd <= 3:
        return "Withing Limit"
    elif borrowerd <= 6:
        return "Over limit: Fine $5"
    elif borrowerd > 6:
        return "Over limit: Fine $10"
    else:
        return "Error: Invalid number of books"

def process_borrowers(filename):
    """
    This function goes through each line of the file and then 
    it proccesses the number of borrowed books for each student.
    """

    try:
        with open(filename , 'r') as f:
            for line in f:
                line  = line.strip()
                parts = line.split(',')

                if len(parts) >=2:
                    name = parts[0].strip()
                    books  = parts[1].strip()

                    if books.isdigit():
                        books_num = int(books)
                        status = check_limit(books_num)
                        print(f"{name}: {status}" , end="\n\n") 
                    else:
                        print(f"Error: Non-numeric value for {name}")   
    except:
        print("Error the file entered is not found.")



def calculate_average_books(filename):

    """
    this function calculates the average number of the 
    borrowed by the students and gives an average value.
    """
    
    try:
        with open(filename, "r") as f:
            total = 0
            count = 0

            for line in f:
                line = line.strip()
                parts = line.split(',')

                if len(parts) >= 2:
                    books = parts[1].strip()
                    if books.isdigit():
                        books_num = int(books)
                        if books_num >= 0:
                            total += books_num
                            count += 1
            if count > 0:
                average = total / count
                average_final = round(average, 2)
                print(f"The average number of borrowed books are: {average_final}")
    except:
        print("Error the file entered is not found.")



def count_over_limit(filename):
    """

    This function counts the number of students 
    who have exceeded the borrowing limit.

    """

    try:
        with open(filename , "r") as f:
            count = 0

            for line in f:
                line = line.strip()
                parts = line.split(',')

                if len(parts) >= 2:
                    books = parts[1].strip()
                    if books.isdigit():
                        books_num = int(books)
                        if books_num > 3:
                            count += 1
            
            print(f"The number of students who are over the limit is: {count}")

    except:
        print("Error the file entered is not found.")



def main():
    while True:
        filename = input("Enter the filename: ")
        try:

            test = open(filename, "r")
            test.close()

            print("\n -----Processing the borrowers-----\n")
            process_borrowers(filename)

            print("\n -----Calculating the average number of borrowed books-----\n")
            calculate_average_books(filename)

            print("\n -----Counting the number of students over the limit-----\n")
            count_over_limit(filename)
            break

        except:
            print("Error the file entered is not found. Please try again.")


if __name__ == "__main__":
    main()

