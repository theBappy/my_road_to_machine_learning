# import os 
# directory_path = "G:\\Desktop\\python\\fundamentals"

# if os.path.exists(directory_path):
#     print(f"The directory '{directory_path}' exists.")
# else:
#     print(f"The directory '{directory_path}' does not exist.")

# import os

# new_directory = "new_dir.txt"
# try:
#     os.makedirs(new_directory)
#     print(f"Directory '{new_directory}' created successfully!")
# except OSError as e:
#     print(f"Error: Failed to create directory '{new_directory}'. {e}")

# import os
# os.mkdir('test')

# import os
# print(f"Current working directory: {os.getcwd()}")

# import os
# directory_path = os.getcwd()
# try:
#     contents = os.listdir(directory_path)
#     print(f"Contents of '{directory_path}'")
#     for item in contents:
#         print(item)
# except OSError as e:
#     print(f"Error: Failed ot list contents of directory '{directory_path}'. {e}")

# import os
# new_directory = r"G:\\Desktop\\python"
# try:
#     os.chdir(new_directory)
#     print(f"Current working directory changed to '{new_directory}'")
# except OSError as e:
#     print(f"Failed to change current working directory to '{new_directory}'. {e}")

# import os
# os.rmdir("test")

import os 
directory_path = "G:\\Desktop\python\\test"
try:
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
    print(f"Error: Failed to remove '{directory_path}'. {e}")


