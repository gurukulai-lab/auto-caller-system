📞 Auto Caller System

An automated calling system built using Python that dials phone numbers from an Excel file and performs call actions using ADB (Android Debug Bridge).

🚀 Features
📲 Automatic calling from Excel list
🤖 Fully automated dialing using ADB
⏱️ Custom delay between calls
📊 Easy number management via Excel file
🔁 Loop-based calling system

🛠️ Tech Stack
Python
Pandas
ADB (Android Debug Bridge)
Subprocess & OS modules

📂 Project Structure
Auto_Caller/
│── autocall.py
│── calling_list.xlsx
│── README.md

▶️ How It Works
Load phone numbers from Excel file
Connect Android device via ADB
Automatically dial numbers
Wait for defined time
End call press enter and move to next number

⚙️ Setup Instructions
Install Python dependencies:
pip install pandas
Install ADB and connect your Android device
Enable USB Debugging on your phone
Place your Excel file with numbers

▶️ Run the Script
python autocall.py

📌 Requirements
Python 3.x
ADB installed and configured
Android device connected
Excel file with phone numbers

⚡ Use Cases
📢 Bulk calling system
🔔 Automated reminders
📞 Notification system
🧪 Testing call automation

⚠️ Disclaimer
This project is for educational purposes only.
Use responsibly and ensure compliance with local laws and regulations.

👨‍💻 Author
Built by GurukulAI Lab 🚀
