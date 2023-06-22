import welly
import os

# Prompt the user to input the LAS filename
filename = input("Enter the name of the LAS file in the /Data directory: ")

# Load the LAS file
if not os.path.isfile('Data/'+filename+'.las'):
    print("LAS file not found. Please check the filename.")
    exit()
else:
  project = welly.read_las('Data/'+filename+'.las', use_normal_engine_for_wrapped=True)

print(project[0])    
