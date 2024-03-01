import subprocess
import os

# pre_processing :
folder_path = "../../worldometer/Results/data" 

# Get all file names in the folder
file_names = ["../../worldometer/Results/data/"+f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# # List of day files
# day_files = ["../../worldometer/Results/table_data.txt"] 
input_mappings = [2,8,4,6,12,11,13,3,5,7]
# # Run the commands for each day and pipe the output

# command = f"python mapper.py {day_files[0]} 2 | python combiner.py  | python reducer.py 3 > network.txt"
# # Execute the entire command
# subprocess.run(command, shell=True)
country_mappings = {} 
f = open("../../worldometer/Results/table_data.txt")
for line in f : 
    line = line.strip().split("\t")
    country_mappings[str(line[1]).strip().lower()] = int(line[0])
f.close

def menu():
    print("************************************")
    while True :
        country = input("\nEnter Name of the Country : ")
        if country not in country_mappings : 
            print("Invalid Country")
            break 
        while True :
            choice = input("\nChoose an option(1-10)(Other Numbers/Texts to Exit):\n"
                            "1. Total cases\n"
                            "2. Active cases\n"
                            "3. Total deaths\n"
                            "4. Total recovered\n"
                            "5. Total tests\n"
                            "6. Death/million\n"
                            "7. Tests/million\n"
                            "8. New case\n"
                            "9. New death\n"
                            "10. New recovered\n"
                            "Enter the corresponding number (1-10): "
                        )
            if not choice.isdigit() and not (1 <= int(choice) <= 10) :
                print("Invalid Choice\n")
                break
            index = input_mappings[int(choice) - 1]
            # Create the first process
            first_command = f"python mapper.py {file_names[0]} {index} "
            first_process = subprocess.Popen(first_command, shell=True, stdout=subprocess.PIPE)

            # Create subsequent processes in a loop, connecting input and output
            for file_name in file_names[1:]:
                command = f"python combiner.py && python mapper.py {file_name} {index}"
                process = subprocess.Popen(command, shell=True, stdin=first_process.stdout, stdout=subprocess.PIPE)
                first_process = process  # Update first_process to connect subsequent processes

            # Create the last process with the reducer command
            last_command = f"python reducer.py {country_mappings[country]}"
            last_process = subprocess.Popen(last_command, shell=True, stdin=first_process.stdout, stdout=subprocess.PIPE)

            # Wait for the last process to finish and get the output
            output, _ = last_process.communicate()

            # Print the output if needed
            print("\n" + output.decode())
 
menu()

# index = 2
# country = 'india'

# # Create the first process
# first_command = f"python mapper.py {file_names[0]} {index} "
# first_process = subprocess.Popen(first_command, shell=True, stdout=subprocess.PIPE)

# # Create subsequent processes in a loop, connecting input and output
# for file_name in file_names[1:]:
#     command = f"python combiner.py && python mapper.py {file_name} {index}"
#     process = subprocess.Popen(command, shell=True, stdin=first_process.stdout, stdout=subprocess.PIPE)
#     first_process = process  # Update first_process to connect subsequent processes

# # Create the last process with the reducer command
# last_command = f"python reducer.py {country_mappings[country]} > network.txt"
# last_process = subprocess.Popen(last_command, shell=True, stdin=first_process.stdout, stdout=subprocess.PIPE)

# # Wait for the last process to finish and get the output
# output, _ = last_process.communicate()

# # Check for errors or print output
# if last_process.returncode == 0:
#     print("Command executed successfully.")
# else:
#     print(f"Error executing command. Exit code: {last_process.returncode}")

# # Print the output if needed
# print("Command output:", output.decode())