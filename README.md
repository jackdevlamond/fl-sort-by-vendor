FL Studio Preset Organizer

This Python script helps organize FL Studio plugin presets by categorizing files based on vendor names. It processes the “Effects” and “Generators” folders located in the FL Studio plugin database, reading vendor names from binary files and copying them into vendor-specific folders.

Features

	•	Reads Vendor Names: Extracts vendor names from binary files.
	•	Organizes Files: Copies files into folders named after their vendors.
	•	Handles Multiple Folders: Processes both “Effects” and “Generators” folders.

How It Works

	1.	Base Directory Configuration: The script sets up the base directory where the “Effects” and “Generators” folders are located.
	2.	Vendor Name Extraction: Reads the vendor name from binary files by locating the pattern of empty bytes followed by the vendor name.
	3.	File Copying: Copies files into new folders named after their vendor, creating the necessary directories if they do not exist.
	4.	Processing Feedback: Outputs status messages indicating the progress and actions taken.

Example

If the script finds a file with a vendor name “SampleVendor”, it will copy that file into a folder named "SampleVendor" within the corresponding "Effects" or "Generators" folder.

Troubleshooting

	•	Ensure that the paths and username are correctly set.
	•	Verify that the “Installed” directory and subdirectories exist as expected.
