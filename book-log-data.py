# import pandas
import pandas as pd
def load_data():
    """ This function loads the CSV file that was previously created from the first run of this script.
    The first run of this script uses the commented out line to create the DataFrame.
    If running this script for the first time, comment out the pd.read_csv command and run the second line of code
    instead that makes a new Pandas DataFrame."""
    book_log = pd.read_csv("book-log-data.csv")
    #book_log = pd.DataFrame(columns=['Title', 'Author', 'Pages', 'Month_Read', 'Year_Read', 'Personal_Rating'])
    return book_log
def get_info(book_log):
    """This function takes user inputs regarding all of the book information that aligns with the columns of the DataFrame.
    After asking for information, it confirms that what was input was correct, and if so, adds it as a new entry to the
    existing DataFrame book_log. If not correct, will ask to re-enter the information again."""
    while True:
        title = str(input("Enter the title of the book: "))
        author = str(input("Enter the first and last name of the author: "))
        page = int(input("Enter the page count: "))
        month = str(input("Enter the full name of the month you finished the book: "))
        year = int(input("Enter the year you finished the book: "))
        rating = float(input("From 0-5, enter your personal book rating: "))
        confirm = input(f"You entered {title}, {author}, {page}, {month}, {year}, {rating}. Is this all correct? (y/n): ")
        if confirm == 'y':
            new_entry = pd.DataFrame({'Title': [title], 'Author': [author], 'Pages': [page], 'Month_Read': [month], 'Year_Read': [year], 'Personal_Rating': [rating]})
            book_log = pd.concat([book_log, new_entry], ignore_index=True)
            return book_log
        elif confirm == 'n':
            print("Re-enter book information")
        else:
            print("Invalid. Please reply 'y' or 'n'.")
def save_entry(book_log):
    """This function saves the new entry to the CSV file to continue to add new rows of information to the correspoding
    columns."""
    book_log.to_csv("book-log-data.csv", index = False)

# Data Pipeline
# 1. Create or Import CSV File
# 2. Collect user input data and confirm it is correct
# 3. Save new information as a new row in the DataFrame
# 4. Print the DataFrame to view past entries and new addition
book_log = load_data()
book_log = get_info(book_log)
save_entry(book_log)
print(book_log)
