try:
    # Attempting to print a variable that hasn't been defined
    print(user_name)

except NameError as error:
    # This block runs only if a NameError occurs
    print("Caught an error!")
    print(f"Details: {error}")
    
    # Provide a fallback solution
    user_name = "Guest"
    print(f"Fallback user name set to: {user_name}")

print("The program successfully kept running!")
