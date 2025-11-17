# baggyunit-multi-tool
A tool for checking is a website is up and also can scan your ip address

Overview

Baggyunit Multi-Tool is a lightweight Python command-line utility created for learning cybersecurity, networking, and Python scripting.
It includes simple scanners and system tools that teach the fundamentals of:

Python CLI tools

Network scanning logic

HTTP requests

System information gathering

Using arguments & menus

Ethical hacking basics

Perfect for students and beginners learning how to build real security tools.

Features
🔹 1. IP Scanner

Displays:

Operating system

Local network routing

Basic system info

🔹 2. Website Status Scanner

Checks:

If a website is reachable

HTTP status codes

Error handling

🔹 3. Interactive Menu (No arguments needed)

When no command-line arguments are provided, the tool launches in beginner-friendly menu mode.

🔹 4. Argument Mode (Advanced users)

Use:

python sys.py s https://example.com
python sys.py p

Installation & Setup
Step 1 — Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

Step 2 — Install required dependencies
pip install requests

Step 3 — Run the tool
python sys.py

Usage Examples
► Run IP Scanner
python sys.py -ip

► Run Website Status Checker
python sys.py -sC <https://website.com>

► check usage
python sys.py -h

► Run in menu mode

Just execute:

python sys.py


You’ll be prompted to choose a tool.
