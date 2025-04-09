# 🧠 Rustalytics – Rust+ Real-Time Monitoring Bot

Rustalytics is a real-time monitoring bot for Rust servers using the official Rust+ companion system.  
It keeps your team updated automatically with in-game alerts for:

- 🚁 Patrol Helicopters  
- 🚢 Cargo Ship spawns  
- 💥 Explosions  
- 🎯 CH47 drops and Oil Rig detection  
- 🧍 Online/offline, AFK status, and deaths  
- ⏰ Server time, sunrise/sunset info  
- 💬 Team chat commands  

> Built for 24/7 deployment so you never miss a moment.

---

## 🛠 Features

- Tracks major world events and player activity
- Posts alerts directly in Rust+ team chat
- Detects CH47s landing at Oil Rigs
- Oil Rig 15-minute engagement timer
- AFK detection and online/offline status
- Fully automated with no manual intervention
- Designed for free cloud deployment (Railway/Render)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/PeterTech-Dev/Rustalytics.git
cd Rustalytics
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Add `config.json` and `server.json`

These files are needed for Rust+ API communication.  
They contain your device token, server info, and authentication details.

#### How to get them:

🧩 Install this Chrome Extension:  
👉 [RustPlus.py Link Companion (Chrome)](https://chrome.google.com/webstore/detail/rustpluspy-link-companion/gojhnmnggbnflhdcpcemeahejhcimnlf?hl=en)

It will automatically generate the required `config.json` and `server.json` files after you link with Rust+.

## 💬 Available Commands

Once deployed, use these in Rust+ team chat:

```plaintext
.help       → Show command list
.heli       → Time since last Patrol Heli
.bradley    → Time until Bradley respawn
.cargo      → Time since last Cargo Ship
.time       → Current server time & next sunrise/sunset
.team       → Online and AFK teammates
.offline    → Offline durations (if tracked)
.leader     → Promote the message sender to team leader
```

---

## 🙏 Special Thanks

This project wouldn't be possible without:

🧠 [`rustplus`](https://github.com/olijeffers0n/rustplus)  
By [**olijeffers0n**](https://github.com/olijeffers0n)

👏 Big thanks to the Rust+ community for unlocking this awesome functionality!

---

## 📜 License

This project is licensed under the **MIT License**.  
You're free to use, fork, and build on top of it!

---

## 🔗 Links

- GitHub: [github.com/PeterTech-Dev/Rustalytics](https://github.com/PeterTech-Dev/Rustalytics)
- RustPlus.py Library: [github.com/olijeffers0n/rustplus](https://github.com/olijeffers0n/rustplus)
- Chrome Extension (RustPlus.py Link):  
  [Install from Chrome Webstore](https://chrome.google.com/webstore/detail/rustpluspy-link-companion/gojhnmnggbnflhdcpcemeahejhcimnlf?hl=en)

---

## 👨‍💻 Author

Built with ❤️ by [PeterTech-Dev](https://github.com/PeterTech-Dev)  
Want to contribute? PRs and stars are always welcome ⭐
