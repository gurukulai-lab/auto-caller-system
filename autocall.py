import pandas as pd
import os
import time
import subprocess

# --- सेटिंग्स ---
EXCEL_FILE = "calling_list.xlsx"
GAP_TIME = 5 

def adb_command(cmd):
    """ADB कमांड चलाने के लिए फंक्शन"""
    subprocess.call(cmd, shell=True)

def make_call(number):
    """नंबर डायल करने का कमांड"""
    print(f"Dialing {number}...")
    # '.\' का मतलब है कि adb.exe इसी फोल्डर में है
    adb_command(f'.\\adb shell am start -a android.intent.action.CALL -d tel:{number}')

def end_call():
    """कॉल काटने का कमांड"""
    print("Ending call...")
    adb_command('.\\adb shell input keyevent 6')

# --- मुख्य प्रोग्राम ---
def start_calling():
    if not os.path.exists(EXCEL_FILE):
        print(f"Error: {EXCEL_FILE} फाइल नहीं मिली! कृपया चेक करें।")
        return

    # एक्सेल लोड करें
    df = pd.read_excel(EXCEL_FILE, dtype=str)

    print("\n--- AUTO CALLING SYSTEM STARTED ---")
    print("1. अपना फ़ोन USB से कनेक्ट करें।")
    print("2. फ़ोन में 'Auto Speaker' ऐप चालु रखें तो बेहतर है।")
    print("------------------------------------------------\n")

    for index, row in df.iterrows():
        name = row['Name']
        mobile = row['Mobile']
        
        # नंबर साफ़ करना (स्पेस, डैश या + हटाना)
        # लेकिन हम '91' खुद से नहीं जोड़ेंगे
        mobile = mobile.replace("-", "").replace(" ", "").replace("+", "")
        
        # [बदलाव] यहाँ से वो कोड हटा दिया जो '91' जोड़ रहा था

        print(f"\n[Call {index + 1}] Student: {name} | Number: {mobile}")
        
        # 1. नंबर डायल करें
        make_call(mobile)
        
        # 2. बात करें
        input(">>> बात पूरी होने पर 'ENTER' दबाएं, कॉल कट जायेगा...")
        
        # 3. कॉल काटें
        end_call()
        
        # 4. गैप
        print(f"Waiting {GAP_TIME} seconds for next call...")
        time.sleep(GAP_TIME)

    print("\nAll calls completed! Great Job.")

if __name__ == "__main__":
    start_calling()