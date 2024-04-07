import unicodedata
import datetime
import uuid
import os
import time

# Function to remove accents from characters
def remove_accents(input_str):
    return ''.join(c for c in unicodedata.normalize('NFD', input_str) if not unicodedata.combining(c))

#Filter folders inside a specific path
def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        if files:
            print("🗄You can use the following files:")
            for i, file in enumerate(files, start=1):
                print(f"{i}: {file}")
        else:
            print("🚮The folder is empty. Write n to use default folder.")
    except FileNotFoundError:
        print("Folder not found!")

# Function to handle the files  
def file_handler(file_path, output_file):

    #Get Keywords
    keywords = []
    while True:
                keyword = input("🔑Enter the keyword you want to search for (enter 'n' to exit): ")
                if keyword.lower() == 'n':
                    break
                else:
                    keywords.append(keyword)
    try:
        found_data = False  # Flag to track if any data was found
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Process each line
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as output:
                    for line in lines: 
                        # Check if any keyword in the list is present in the line
                            if any(remove_accents(keyword.lower()) in remove_accents(line.lower()) for keyword in keywords):
                                found_data = True
                                # Write the line to the output file
                                output.write("🎯HIT: " + line)
                                print("🎯HIT: " + line)
        if not found_data:
            print("💤 No data was found")            
    except FileNotFoundError:
            print("File not found!")
    except Exception as e:
            print("Error occurred:", e)

def email():
    while True:

        folder_path = './Notepads' # Default Folder_Path
        list_files_in_folder(folder_path) #Lists the Folder Files

        # Prompt user to select a file
        file_number = input("Select a file by entering its number (or '0' to use default): ")
        os.system('cls')
        if file_number.lower() == '0':
            file_path = './Default/email.txt'  # Default path to your text file
            print(f"📁The following path is gonna be used: {file_path}")
        else:
            try:
                file_number = int(file_number)
                files = os.listdir(folder_path)
                if 1 <= file_number <= len(files):
                    selected_file = files[file_number - 1]
                    file_path = os.path.join(folder_path, selected_file)
                    file_path = file_path.replace('\\', '/')
                    print(f"📁The following path is gonna be used: {file_path}")
                else:
                    print("❌Invalid file number. Using default file.")
                    file_path = './Default/email.txt'  # Default path to your text file
            except ValueError:
                print("❌Invalid input. Using default file.")
                file_path = './Default/email.txt'  # Default path to your text file

        #Decide the txt name -> Auto  or Specific 
        custom_filename = input("Specific Filename? Write it/n: \n")
        if len(custom_filename.lower()) > 1:
            output_file = './Notepads/Email_' + custom_filename + '.txt'  # Custom Output file name
            os.system('cls')
            print(f"📁The following path is gonna be used: {file_path}\n📑File is gonna be saved as: {output_file}")
        else:
            unique_filename = f'output_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_{uuid.uuid4().hex[:8]}.txt'
            output_file = './Notepads/' + unique_filename  # RNG Output file name

        #Check if File name already exists
        if os.path.exists(output_file):
            print(f"File '{output_file}' already exists. \nPlease choose another file name. \n")
            continue

        file_handler(file_path, output_file)

        #Sleep Xs duration
        print("\n -------- --- ------ \nClearing the screen\n -------- --- ------ ")
        time.sleep(1)
        os.system('cls')

        #Use again the program
        try_again = input("Do you want to use email again❓ y/n \n")
        if try_again.lower() != 'y':
            os.system('cls')
            break

def phone(): 
     while True:

        folder_path = './Notepads' # Default Folder_Path
        list_files_in_folder(folder_path) #Lists the Folder Files

        # Prompt user to select a file
        file_number = input("Select a file by entering its number (or '0' to use default): ")
        os.system('cls')
        if file_number.lower() == '0':
            file_path = './Default/phone.txt'  # Default path to your text file
            print(f"📁The following path is gonna be used: {file_path}")
        else:
            try:
                file_number = int(file_number)
                files = os.listdir(folder_path)
                if 1 <= file_number <= len(files):
                    selected_file = files[file_number - 1]
                    file_path = os.path.join(folder_path, selected_file)
                    file_path = file_path.replace('\\', '/')
                    print(f"📁The following path is gonna be used: {file_path}")
                else:
                    print("❌Invalid file number. Using default file.")
                    file_path = './Default/phone.txt'  # Default path to your text file
            except ValueError:
                print("❌Invalid input. Using default file.")
                file_path = './Default/phone.txt'  # Default path to your text file

        #Decide the txt name -> Auto  or Specific 
        custom_filename = input("Specific Filename? Write it/n: \n")
        if len(custom_filename.lower()) > 1:
            output_file = './Notepads/Phone_' + custom_filename + '.txt'  # Custom Output file name
            os.system('cls')
            print(f"📁The following path is gonna be used: {file_path}\n📑File is gonna be saved as: {output_file}")
        else:
            unique_filename = f'output_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_{uuid.uuid4().hex[:8]}.txt'
            output_file = './Notepads/' + unique_filename  # RNG Output file name
            os.system('cls')
            print(f"📁The following path is gonna be used: {output_file}\n📑File is gonna be saved as: {unique_filename}")
        #Check if File name already exists
        if os.path.exists(output_file):
            print(f"File '{output_file}' already exists. \nPlease choose another file name. \n")
            continue

        file_handler(file_path, output_file)

        #Sleep Xs duration
        print("\n -------- --- ------ \nClearing the screen\n -------- --- ------ ")
        time.sleep(1)
        os.system('cls')

        #Use again the program
        try_again = input("Do you want to use phone again❓ y/n \n")
        if try_again.lower() != 'y':
            os.system('cls')
            break      

def main():
    while True:
        answer = input("Email(0) or Phone(1)?\n")

        if answer.lower() == "0" or answer.lower() == "email":
            os.system('cls')
            email()
        else:
            os.system('cls')
            phone()
        try_again = input("End program❓ y/n \n")
        os.system('cls')
        if try_again.lower() == 'y':
            os.system('cls')
            break      
main()