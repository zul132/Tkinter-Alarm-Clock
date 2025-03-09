# ⏰ Tkinter-Alarm-Clock

A **GUI-based alarm clock** desktop app built using **Python** and **Tkinter**. This was my very first **Coding Project**, submitted as part of my **12th Standard CBSE Computer Science Lab Examination**.

## ✨ Features
- **Simple GUI Interface**: Built using Tkinter for an easy-to-use experience.
- **12-Hour Format**: Users can set alarms in AM/PM format.
- **Notification Alerts**: Displays pop-up messages when the alarm is set and when it rings.
- **Beeping Alarm**: Uses the Winsound module to produce a beeping sound when the alarm goes off.
- **No Additional Dependencies**: Uses built-in Python modules, making installation simple.

## ⚙️ Project Setup
### 📋 Prerequisites
- Python installed on your PC (version 3.x recommended).

### 📥 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Tkinter-Alarm-Clock.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Tkinter-Alarm-Clock
   ```
3. Install the necessary modules:
   - **Windows/macOS**: Tkinter is included by default, so no additional installation is required.
   - **Linux**: You may need to install Tkinter separately:
     ```sh
     sudo apt-get install python3-tk
     ```
4. Run the application:
   ```sh
   python app.py
   ```

## 🚀 How It Works
1. Open the application.
2. Enter the time when you want the alarm to ring in the **HOURS** and **MINUTES** fields.
3. Select **AM/PM** from the dropdown menu.
4. Click on **SET ALARM** to activate the alarm.
5. You will receive a notification confirming the alarm has been set.
6. When the time matches, another notification will appear with the message **"WAKE UP SLEEPY HEAD"**, and a beeping sound will play.

## 📦 Modules Used
- **Tkinter**: For GUI creation.
- **Datetime**: To check the current time.
- **Winsound**: To play alarm sounds.
- **Messagebox (from Tkinter)**: To display notifications.
- **Ttk (from Tkinter)**: To create labels, buttons, and combobox elements.

## ⚠️ Limitations & Further Development Areas
- The alarm only works in **12-hour format**. Entering time in military format may cause errors.
- The beeping **cannot be stopped manually**; it plays for a set duration.
- No option to **customize alarm sounds**.
- The app **continuously checks the time**, which may cause high CPU usage.

