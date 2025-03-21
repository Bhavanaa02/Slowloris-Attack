# 🛡️ Slowloris DoS Attack Automation

## 🔧 Installation & Setup
### ** 1️ Clone the Repository**
```bash
git clone https://github.com/your-username/Slowloris-Attack.git
cd Slowloris-Attack
```

### ** 2️ Install Required Dependencies**
```bash
pip install requests
```

---

##  Usage Guide
### **Basic Attack Command**
```bash
python slowloris.py <target> -p <port> -c <connections> -i <interval>
```
### **Example**
```bash
python slowloris.py 127.0.0.1 -p 8080 -c 100 -i 10
```
🔹 **127.0.0.1** → Target server (localhost for testing)  
🔹 **8080** → Target port  
🔹 **100 connections** → Number of concurrent attack threads  
🔹 **10 sec interval** → Time between partial request sends  

### **Available Command-Line Options**
| Option            | Description                                  | Default |
|------------------|----------------------------------------------|---------|
| `<target>`       | Target server IP or domain                   | -       |
| `-p, --port`     | Target port                                  | 80      |
| `-c, --connections` | Number of open connections               | 500     |
| `-i, --interval` | Time interval between partial requests (sec) | 15      |

---

##  Attack Methodology
1. **Open multiple connections** to the target server.
2. **Send partial HTTP headers** instead of complete requests.
3. **Maintain active connections** by periodically sending small data chunks.
4. **Exhaust server connection slots**, preventing legitimate users from accessing it.

---

##  Detecting Server Vulnerability
To check if a target is **vulnerable**:
```bash
python slowloris.py <target> -p 80 -c 10 -i 10
```
✔ If connections **stay open** indefinitely, the server **may be vulnerable**.  
❌ If connections **are dropped quickly**, the server **has mitigation in place**.

---

##  How to Stop the Attack?
Press **CTRL + C** to stop the script.

---

## 🛠️ Mitigation Techniques
Servers can **prevent Slowloris attacks** by:
- **Limiting connection timeouts** (e.g., Nginx `client_body_timeout`).
- **Using Reverse Proxies** like Cloudflare.
- **Restricting IP requests** (rate limiting).
- **Dropping slow connections**.

---
  
This project is for **educational use only**.
```

---
