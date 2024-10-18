# HadesTorChat V 1.0

![HadesTorChat Logo](https://github.com/haydenbanz/haydenbanz.github.io/blob/main/images/%20gitimage/87556654A.png?raw=true)

[![Python - HadesTorChat](https://img.shields.io/static/v1?label=Python&message=HadesTorChat&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge&&logo=python)](https://github.com/haydenbanz/HadesTorChat/tree/main)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=%233DA639&labelColor=%23e3e3e3&style=for-the-badge)](https://github.com/haydenbanz/HadesTorChat/blob/main/LICENSE)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&color=%230078D6&labelColor=%23e3e3e3&style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![Discord.py library](https://img.shields.io/static/v1?label=Discord.py&message=Library&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://pypi.org/project/discord.py/)
[![GitHub Issues](https://img.shields.io/github/issues/haydenbanz/HadesTorChat?style=for-the-badge)](https://github.com/haydenbanz/HadesTorChat/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haydenbanz/HadesTorChat?style=for-the-badge)](https://github.com/haydenbanz/HadesTorChat/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/haydenbanz/HadesTorChat?style=for-the-badge)](https://github.com/haydenbanz/HadesTorChat/stargazers)
![Profile Views](https://komarev.com/ghpvc/?username=haydenbanz&color=%232A3E87&labelColor=%236A7DA8&style=for-the-badge)
[![GitHub Download](https://img.shields.io/static/v1?label=Download&message=HadesTorChat&color=%242A3E87&labelColor=%236A7DA8&style=for-the-badge)](https://github.com/haydenbanz/HadesTorChat/releases)

# HadesTorChat: Secure chat application built for anonymous communication


## 📖 Description
HadesTorChat is a secure chat application built for anonymous communication over the Tor network. It allows users to send messages while maintaining privacy. The system uses Python for backend functionality and PyQt & Tkinter for the user interface. With features like message encryption and anonymous routing through a hidden service, it provides a platform for confidential discussions. It is designed for deployment on Kali Linux and includes an interactive, transparent UI overlay similar to Conky.

## Key Features
- **Anonymous Communication**: Utilizes the Tor network to ensure secure, anonymous messaging.
- **Secure Chat**: End-to-end encryption for all messages exchanged through the platform.
- **PyQt & Tkinter GUI**: Features a sleek, interactive user interface using PyQt.
- **Transparent UI Overlay**: Customizable and lightweight overlay for chat windows, inspired by Conky.
- **Cross-Platform Compatibility**: Can be deployed on Linux, with a focus on Kali Linux.
- **Tor Hidden Service**: Built on a .onion address for added privacy and anonymity.
- **Python-Powered**: Developed using Python, making it highly customizable and extendable.

## ⚠️ Disclaimer

HadesTorChat is designed for secure, anonymous communication over the Tor network. While every effort is made to protect your privacy, **no system is entirely immune to vulnerabilities**. Use this software responsibly, and be aware of the risks associated with online anonymity.

- 🛡️ **Data Security**: Ensure you are using the latest version for the best security practices.
- 🌐 **Network Privacy**: Tor may slow down your connection due to its anonymization techniques.
- 🔒 **Responsibility**: Users are responsible for their own actions while using HadesTorChat.

The creators of HadesTorChat are **not liable** for any misuse of the platform.<br>
Violations will be subject to legal action and may result in severe penalties.<br>
Please ensure all usage complies with applicable laws and regulations.<br>

## 🛠️ Prerequisites

Before installing and running **HadesTorChat**, make sure you have the following:

- 🐍 **Python 3.6+**: Download and install [Python](https://www.python.org/downloads/) if not already installed.
- 🧅 **Tor**: Ensure you have Tor installed and configured on your system.
- 📦 **Python Packages**: Install required Python libraries with:
  ```bash
  pip install -r requirements.txt
     ```
  - 💻 **Kali Linux (Recommended)**: Although **HadesTorChat** is cross-platform, Kali Linux is the recommended environment for maximum security. Other Linux distributions such as Ubuntu or Debian-based are also supported to run server.py. However, **HadesTorChat** only works on Linux, while the client-side can run on Windows, Linux, and macOS.

- 🔐 **PyQt & Tkinter**: Both PyQt and Tkinter are required for the graphical user interface (GUI) to function properly.

## 🔧 Configuration

### Server-Side Setup

1. **Install Tor** on your Linux server using the following command:

`
  pip install -r requirements.txt
`
Configure the Tor Hidden Service by editing the Tor configuration file (/etc/tor/torrc):
 -Uncomment the following line to enable the SOCKS port:

`
 SocksPort 9050  # Default: Bind to localhost:9050 for local connections.
`
-Add the hidden service configuration 

`
HiddenServiceDir /var/lib/tor/hidden_service_chat/
HiddenServicePort 9050 127.0.0.1:5000
`
-Retrieve the Onion URL: After restarting the Tor service, you can get your onion address by running:
`
sudo cat /var/lib/tor/hidden_service_chat/hostname
`

### Client-Side Setup
For the client-side, you need to update the following files to point to your onion service:
-Edit client.py, chat.py, and send.py to replace YOUR_ONION_URL with your actual .onion address:

## 🚀 Installation

1. **Clone the Repository**:
   Start by cloning the **HadesTorChat** repository:
   ```bash
   git clone https://github.com/haydenbanz/HadesTorChat
     cd HadesTorChat/server
   sudo service tor start 
   python server.py
    ```
-Run the Server: Navigate to the server folder and run server.py to start the chat server:
-Run the Client: You can choose between two client-side options:

  PyQt Overlay (Modern): Navigate to the client folder and run chat.py. This will create an interactive overlay on your home screen similar to Conky:
`
python chat.py
`
or  in below you can send messgaes in overlay
`
python send.py
`
  Tkinter Client (Old School): For a more traditional interface, run client.py:
  
`
python client.py
`


# HadesTorChat

Thank you for contributing to HadesConnect!

## 🌐 Support

[![Discord](https://img.shields.io/badge/Discord-CODE%20GLITCH%20Bot%20DISCORD%20SERVER%20NAME-%237289DA?style=for-the-badge&logo=discord)](https://discord.gg/ZFTCpAU53U)

Join our Discord server (Update Soon) for support, discussions, and updates related to DiscordGloom.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

**Unauthorized use is strictly prohibited.**

👤 0x_hayden  
📧 Email: cubedimension@protonmail.com  

## 🙏 Credits

This project is maintained by:

[<img src="https://avatars.githubusercontent.com/u/135024483?s=48&v=4" width="64" height="64" alt="Contributor Name">](https://github.com/code-glitchers)

### Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haydenbanz">](https://github.com/haydenbanz)  
[<img src="https://avatars.githubusercontent.com/u/144106684?s=64&v=4" width="64" height="64" alt="Glitchesminds">](https://github.com/Glitchesminds)

## ☕ Support

If you find this project helpful, consider buying us a coffee:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/hades)

## 🚫 Disclaimer

The creators of this project are not responsible for any misuse of the software or its content.
