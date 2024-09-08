import os
import shutil

# macOS username
username = 'your_username'

# Define the base directory where the "Effects" and "Generators" folders are located
base_directory = f"/Users/{username}/Documents/Image-Line/FL Studio/Presets/Plugin database"

# List of folders to process
folders = ["Effects", "Generators"]

# Define a function to read the vendor name from a binary file
def read_vendor_name(file_path):
    # Open the file in binary read mode
    with open(file_path, "rb") as f:
        # Read the whole file content
        data = f.read()
        # Find the index of the last 7 empty bytes (14 hex digits)
        index = data.rfind(b"\x00" * 7)
        if index == -1:
            return "Unknown"  # Return 'Unknown' if pattern not found
        # Extract the vendor name as a string after the empty bytes
        vendor_name = data[index + 7:].decode(errors="ignore").strip()
        # Return the vendor name
        return vendor_name

# Define a function to copy a file to a new folder named after the vendor
def copy_to_vendor_folder(file_path, vendor_name):
    # Get the file name from the file path
    file_name = os.path.basename(file_path)
    # Create a new folder path with the output folder and the vendor name
    new_folder = os.path.join(output_folder, vendor_name)
    # Create the new folder if it does not exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    # Create a new file path with the new folder and the file name
    new_file = os.path.join(new_folder, file_name)
    # Copy the file to the new file path
    shutil.copy(file_path, new_file)
    print(f"Copied {file_name} to {new_folder}")

for x in folders:
    # Print the current folder being processed
    print(f"Currently processing {x}")

    # Check and define the path to the input folder for macOS
    input_folder = os.path.join(base_directory, "Installed", x, "New")

    if os.path.isdir(input_folder):
        print(f"{x} Input Folder - Found at {input_folder}")
    else:
        print(f"{x} Input Folder - Not found at {input_folder}, skipping.")
        continue

    # Define the output folder path
    output_folder = os.path.join(base_directory, "Installed", x)

    # Check if output folder exists, if not create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Move only files, skip if it's a directory
        if os.path.isfile(file_path):
            # Read the vendor name from the file
            vendor_name = read_vendor_name(file_path)
            # Copy the file to the vendor-specific folder
            copy_to_vendor_folder(file_path, vendor_name)
        else:
            print(f"Skipped {filename} as it is not a file.")