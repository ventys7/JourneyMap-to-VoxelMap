# JourneyMap-to-VoxelMap

This Python script is a utility to convert Minecraft waypoints from the JourneyMap format (.dat) into the VoxelMap format (.points).

⚠️ Important Disclaimer
Project Status: This repository is no longer maintained and will not receive any further updates. You are free to fork, modify, and use the code as you wish.
Known Issues: The waypoint color converter is currently not working as intended. Waypoints may appear with default colors regardless of their original settings.
Platform: This script has only been tested on macOS. Compatibility with Windows or Linux is not guaranteed but likely.
Credits: The logic for this converter was inspired by the JourneymapToVoxelmap repository made by AoNoAsgard: https://github.com/AoNoAsgard/JourneymapToVoxelmap.

🛠 Requirements
To run this script, you need:
- Python 3 installed on your system.
- The nbtlib library to handle Minecraft's NBT file format.
You can install the required dependency using pip:
- pip install nbtlib

🚀 How to Use
1. Setup Folders
- Place the main.py script in a folder. The script will automatically look for or create an input/ and output/ directory.

2. Add your Data
- Copy your JourneyMap WaypointData.dat file into the input/ folder.

3. Run the Script
- Open your terminal in the project directory and execute:
  python3 main.py

4. Collect Output
- Your converted waypoints will be generated in the output/ folder as a file named journey_from_dat.points. You can then move this file into your VoxelMap waypoints directory.

📝 Technical Details
Data Handling: The script loads uncompressed NBT files (gzipped=False).
Sanitization: Names are automatically cleaned to remove characters like ,, #, and : which are incompatible with the VoxelMap format.
Output Structure: The generated file includes the necessary headers (subworlds, seeds, etc.) required for VoxelMap to recognize the data.
