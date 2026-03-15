from pathlib import Path
import os

def readfileAndfolder():
    path = Path('')   #empty islye hai ki jis folder me ye file hai usi folder ke data ko read karega
    items = list(path.rglob('*'))  #glob is used to read the data of folder and '*' is used to read all the data of folder
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


# first function for creating a file
def createFile():
    try:
        readfileAndfolder()
        name= input("Plese tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w" ) as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)

            print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    except Exception as err:
        print(f"An error occurred while creating the file: {err}")


# second function for reading a file
def readFile():
    try:
        readfileAndfolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(f"Content of the \nfile_name: '{name}':\n File_Data: {data}")
            
            print("Readed successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"An error occurred while reading the file: {err}")

# third function for updating a file
def updateFile():
    try:
        readfileAndfolder()
        name = input("Which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for Changing the name of file :- ")
            print("Press 2 for Overwriting the data of your file :-")
            print("Press 3 for Appending the file :-")
            response = int(input("Please enter your choice :- "))
            if response  == 1 :
                new_name = input("Please enter the new name of file :- ")
                p2 = Path(new_name)
                p.rename(p2)
                print(f"File name changed successfully to '{new_name}'.")

            elif response == 2:
                with open(p, "w")as fs:
                    data = input("What you want to write this is overwrite the data of file :- ")
                    fs.write(data)
                print("File data overwritten successfully.")
            elif response == 3:
                with open(p, "a")as fs:
                    data = input("What you want to write this is append the data of file :- ")
                    fs.write(" " + data)
                print("File data appended successfully.")
            else:
                print("Sorry you have entered wrong choice.")
        else:
            print(f"File '{name}' does not exist.")

    except Exception as err:
        print(f"An error occurred while updating the file: {err}")



# fourth function for deleting a file
def deleteFile():
    try:
        readfileAndfolder()
        name = input ("Which file you want to delete, Enter the name of file :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()  #unlink is used to delte the file..
        #    os.remove(name) #os.remove() is also used to delete the file, but it is not recommended because it can cause issues if the file is open or in use by another process.
            print(f"file '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")

    except Exception as err:
        print(f"An error occurred while deleting the file: {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please enter your choice :"))


if check == 1:
    createFile()
if check == 2:
    readFile()
if check == 3:
    updateFile()
if check == 4:
    deleteFile()
