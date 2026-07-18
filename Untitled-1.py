###################################
# ATM Machine With While Loop
###################################

# balance = 39933
# pincode = 3333

# # Ask user for PIN
# user_pin = int(input("Enter your PIN code: "))

# if user_pin == pincode:
#     print("Login successful!")

#     while True:
#         print("\n===== ATM MENU =====")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Balance Enquiry")
#         print("4. Funds Transfer")
#         print("5. Bill Payment")
#         print("6. Exit")

#         choice = int(input("Enter your choice: "))

#         # 1. Deposit
#         if choice == 1:
#             deposit_amount = int(input("Enter deposit amount: "))
#             balance += deposit_amount
#             print("Deposit successful!")
#             print("Updated Balance:", balance)

#         # 2. Withdraw
#         elif choice == 2:
#             withdraw_amount = int(input("Enter withdrawal amount: "))

#             if withdraw_amount <= balance:
#                 balance -= withdraw_amount
#                 print("Withdrawal successful!")
#                 print("Updated Balance:", balance)
#             else:
#                 print("Insufficient balance!")

#         # 3. Balance Enquiry
#         elif choice == 3:
#             print("Your current balance is:", balance)

#         # 4. Funds Transfer
#         elif choice == 4:
#             receiver_iban = input("Enter receiver IBAN: ")
#             transfer_amount = int(input("Enter transfer amount: "))

#             if transfer_amount <= balance:
#                 balance -= transfer_amount
#                 print("Funds transferred successfully!")
#                 print("Transferred to:", receiver_iban)
#                 print("Remaining Balance:", balance)
#             else:
#                 print("Insufficient balance!")

#         # 5. Bill Payment
#         elif choice == 5:
#             print("\nAvailable Bills:")
#             print("1. PTCL")
#             print("2. LESCO")
#             print("3. SUI-Gas")

#             bill_choice = int(input("Select bill type: "))
#             bill_amount = int(input("Enter bill amount: "))

#             if bill_amount <= balance:
#                 balance -= bill_amount

#                 if bill_choice == 1:
#                     print("PTCL bill paid successfully!")
#                 elif bill_choice == 2:
#                     print("LESCO bill paid successfully!")
#                 elif bill_choice == 3:
#                     print("SUI-Gas bill paid successfully!")
#                 else:
#                     print("Invalid bill type!")

#                 print("Remaining Balance:", balance)

#             else:
#                 print("Insufficient balance!")

#         # Exit
#         elif choice == 6:
#             print("Thank you for using ATM!")
#             break

#         else:
#             print("Invalid option!")

#         # Continue or Exit
#         again = input("\nDo you want to continue? (yes/no): ")

#         if again.lower() != "yes":
#             print("Thank you for using ATM!")
#             break

# else:
#     print("Invalid PIN code!")








#     folder = ['main.py', 'hello.mp3', 'main.docx', 'for.py']

# pdf = []
# mp3 = []
# py = []
# docx = []

# # 4. Find all files of a particular extension
# for file in folder:
#     if file.endswith(".pdf"):
#         pdf.append(file)
#     elif file.endswith(".mp3"):
#         mp3.append(file)
#     elif file.endswith(".py"):
#         py.append(file)
#     elif file.endswith(".docx"):
#         docx.append(file)

# print("PDF files:", pdf)
# print("MP3 files:", mp3)
# print("Python files:", py)
# print("DOCX files:", docx)


# # 1. Search a file
# search = input("\nEnter file name to search: ")

# if search in folder:
#     print("File found!")
# else:
#     print("File not found!")


# # 2. Remove a file
# remove = input("\nEnter file name to remove: ")

# if remove in folder:
#     folder.remove(remove)
#     print("File removed successfully")
# else:
#     print("File not found!")

# print("Current files:", folder)


# # 3. Rename a file
# old_name = input("\nEnter file name to rename: ")

# if old_name in folder:
#     new_name = input("Enter new file name: ")
#     index = folder.index(old_name)
#     folder[index] = new_name
#     print("File renamed successfully")
# else:
#     print("File not found!")

# print("Current files:", folder)


# # 5. Sort all files alphabetically
# folder.sort()

# print("\nFiles sorted alphabetically:")
# print(folder)

# # declare 
# def sum (a,b):
#     print(f"sum of {a} and {b} is {a+b}")
    

# def mul(x1,y1):
#         print (f"multiplication of {x1} and {y1} will be {x1 * y1}")

# # call 
# for index in range(5):
#    sum(677,12)  
#    mul(10,5)

# ###############
# balance= 10000000
# def deposit(amount):
#      balance = balance + amount
# print= balance

