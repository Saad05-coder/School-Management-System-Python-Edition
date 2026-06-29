from school_lib import *

def main():
    while True:
        # keep asking until login succeeds
        role = ""
        while role == "":
            role = login()

        print(f"\n========================================")
        print(f"   WELCOME, {role}!")
        print(f"========================================")

        staying_in_menu = True

        while staying_in_menu:
            print("\n----------------------------------------")
            if role == "Admin":
                print("[1] Add User")
                print("[2] Remove User")
                print("[3] Toggle Status")
                print("[4] Stats")
                print("[5] LOGOUT")
            else:
                print("[1] Add Student")
                print("[2] Search")
                print("[3] Update")
                print("[4] Delete")
                print("[5] Report")
                print("[6] LOGOUT")
            print("----------------------------------------")

            choice = input("Enter choice: ")

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice)

            if role == "Admin":
                if   choice == 1: add_user()
                elif choice == 2: remove_user()
                elif choice == 3: toggle_user_status()
                elif choice == 4: view_statistics()
                elif choice == 5:
                    print("Logging out...")
                    staying_in_menu = False
                else:
                    print("Invalid choice.")
            else:
                if   choice == 1: add_student_record()
                elif choice == 2: search_student()
                elif choice == 3: update_student()
                elif choice == 4: delete_student()
                elif choice == 5: generate_report()
                elif choice == 6:
                    print("Logging out...")
                    staying_in_menu = False
                else:
                    print("Invalid choice.")

        print("\nReturning to Login Screen...\n")

main()