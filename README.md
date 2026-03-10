# 🛡️ Nexus-Vault

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Security](https://img.shields.io/badge/Encryption-AES--256-brightgreen.svg)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Nexus-Vault** is a professional-grade file encryption utility designed for speed, security, and ease of use. It uses industrial-strength AES-256 encryption via the PBKDF2 key derivation function to ensure your files remain private and secure.

## ✨ Features
- **Industrial Strength Security**: AES-256-CBC encryption.
- **Robust Key Derivation**: PBKDF2 with SHA-256 and 100,000 iterations.
- **Modern CLI**: Beautiful text-based user interface powered by `Rich`.
- **Secure Password Generator**: Built-in entropy-based generator for high-security vault passwords.
- **Lightweight**: Zero fluff, just high-performance security.

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/ShubhamCodeWave/Nexus-Vault.git
cd Nexus-Vault

# Install dependencies
pip install -r requirements.txt
```

## 🛠 Usage

### 🎲 Generate a Secure Password
```bash
python -m nexus_vault.cli generate --length 32
```

### 🔒 Lock a File
```bash
python -m nexus_vault.cli lock path/to/your/file.txt
```

### 🔓 Unlock a File
```bash
python -m nexus_vault.cli unlock path/to/your/file.txt.nvlt
```

## 🔐 Security Details
Nexus-Vault uses a unique 16-byte salt for every encryption operation. Even if you use the same password for different files, the resulting encrypted data will be completely different. The salt is stored alongside the encrypted data in the `.nvlt` file.

## 👨‍💻 Developer
**Shubham Sharma**
- GitHub: [@ShubhamCodeWave](https://github.com/ShubhamCodeWave)
- Website: [shubham-sharma.great-site.net](https://shubham-sharma.great-site.net)

---
*Developed for professionals who value privacy.*
