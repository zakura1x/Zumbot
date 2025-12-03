# Zumbot

## 🚀 What is Zumbot

**Zumbot** is an automation tool that automatically wakes up your computer, joins a scheduled Zoom meeting, and logs a “time in” to Viber.  
It’s useful for users who want to automate attendance or check-in tasks (e.g., online classes, meetings), especially when you might be unavailable to manually log in.

## 📄 Features

- Automatically wake your computer (resume from sleep/hibernate)  
- Automatically join a Zoom meeting at a scheduled time  
- Automatically log a “time in” to Viber (or simulate check-in)  
- Schedule-driven: once configured, no manual action needed  
- Lightweight and simple — no heavy UI required  

## 🛠️ Getting Started / Installation

> These instructions assume you are on Windows (or the OS as targeted by this project).  

1. Clone this repository  
   ```bash
   git clone https://github.com/zakura1x/Zumbot.git
   cd Zumbot

2. Install required dependencies (see requirements.txt)
    pip install -r requirements.txt

3. (If applicable) Run setup.bat to configure initial setup — e.g. register the script to run at system startup or schedule the wake-up.

4. Configure your schedule / meeting details / Viber credentials (if required). This may involve editing a config file or script (update paths, times, meeting IDs/passwords, login info).

5. Start the main script (or ensure scheduler is active).

6. Let the script run — it should wake the computer, join Zoom, and log to Viber automatically at the scheduled time.

🎯 Usage Example
# Example command to manually start the bot
python main.py


Ensure your computer is allowed to wake up via scheduled task / wake timers.

Make sure Zoom and Viber credentials are valid and accessible.

Verify your schedule is correct (date, time, meeting ID/password, etc).

⚠️ Important Notes & Limitations

Your computer must be configured to allow wake-up / scheduled wake timers.

Zoom and Viber credentials must be correct and may require prior login or stored session.

Use responsibly — do not violate any attendance policy or misuse automation for dishonest purposes.

📂 Project Structure (roughly)
/Zumbot
  /scripts       ← main scripts to schedule, wake, join meeting, log to Viber
  /utils         ← helper utilities (e.g. time parsing, login handling)
  requirements.txt
  setup.bat      ← optional setup script (Windows)
  README.md      ← this file

🤝 Contributing

Contributions are welcome! If you want to:

Add support for other operating systems

Improve reliability (e.g. better wake/sleep handling, Zoom/Viber edge cases)

Add logging, error handling, notifications

Add scheduling UI, or config file parsing

… feel free to open an issue or submit a pull request.

📚 License & Credits

Original author / maintainer: zakura1x
