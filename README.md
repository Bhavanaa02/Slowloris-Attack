## Slowloris DoS Attack Automation

##  Project Overview
This project automates the **Slowloris Denial-of-Service (DoS) attack**, which works by sending **partial HTTP requests** to a target web server and keeping multiple connections open indefinitely. The goal is to **exhaust the server's resources**, preventing legitimate users from accessing the service.  

The project focuses on:
- **DoS attack mechanisms & connection persistence**
- **Multi-threading for efficient execution**
- **Error handling & real-time logging**
- **Customizable attack parameters via command-line arguments**

---

##  Installation & Setup
### 1️ Clone the Repository
```bash
git clone https://github.com/Bhavanaa02/Slowloris-Attack.git
cd Slowloris-Attack
```

### 2️ Install Required Dependencies
```bash
pip install requests
```

### 3️ Run the Script
You can **run the script with default settings** or **customize parameters**.

####  Default Mode (localhost attack)
```bash
python slowloris.py
```
🔹 Targets `127.0.0.1:8080` with `100` connections and `10s` intervals.  

#### Custom Mode (User-defined target)
```bash
python slowloris.py <target> <port> <connections> <interval>
```
**Example:**
```bash
python slowloris.py 192.168.1.10 80 200 5
```
🔹 Attacks **`192.168.1.10`** on **port `80`** with **200 connections**, sending keep-alive headers every **5 seconds**.  

---

##  Attack Methodology
1. **Opens multiple connections** to the target server.
2. **Sends partial HTTP headers** but never completes the request.
3. **Keeps connections open** by periodically sending small data chunks.
4. **Exhausts server connection slots**, preventing real users from accessing the service.

---

##  Stopping the Attack
Press **CTRL + C** to immediately stop the script.

---

##  Error Handling & Logging
The script includes:
✔ **Real-time status updates** (logs open & failed connections).  
✔ **Error handling for connection failures** (`try-except` blocks).  
✔ **Automatic reconnection if a connection drops**.  
✔ **Prevents crashes from invalid user input** (e.g., non-numeric values).  

---

## Mitigation Techniques (How to Defend)
Servers can **prevent Slowloris attacks** by:
- **Limiting connection timeouts** (e.g., Nginx `client_body_timeout`).
- **Using Reverse Proxies** like Cloudflare.
- **Enforcing Rate Limiting** to block multiple slow requests.
- **Dropping slow connections** after a set timeout.


