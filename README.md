# 🛡️ Linux Security & Compliance Auditor

> A lightweight, colorful CLI tool designed to perform rapid security audits on Linux systems. Built for cybersecurity students, system administrators, and IT professionals.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview (აღწერა)
**Linux Security & Compliance Auditor** არის პითონზე დაწერილი მსუბუქი, კონსოლური (CLI) ინსტრუმენტი, რომელიც ეხმარება სისტემის ადმინისტრატორებსა და უსაფრთხოებით დაინტერესებულ პირებს, სწრაფად შეამოწმონ ლინუქს გარემოს ძირითადი უსაფრთხოების პარამეტრები. 

პროექტი შექმნილია სასწავლო მიზნებისთვის და იყენებს თანამედროვე ტერმინალის ვიზუალიზაციის ბიბლიოთეკას (`rich`), რაც შედეგებს წარმოუდგენლად თვალსაჩინოს და ლამაზს ხდის.

---

## 🚀 Key Features (ძირითადი ფუნქციები)
* **SSH Root Login Check:** ამოწმებს, დაშვებულია თუ არა სერვერზე `root` მომხმარებლით პირდაპირი შესვლა (`PermitRootLogin`).
* **Active Port Monitoring:** სკანირებს და ითვლის აქტიურ მოსმენილ პორტებს (`ss` ბრძანების გამოყენებით).
* **System Updates Status:** აკონტროლებს კრიტიკული უსაფრთხოების განახლებების სტატუსს (Debian/Ubuntu სისტემებისთვის).
* **Rich TUI Integration:** ტერმინალში გამოაქვს ფერადი ცხრილები, პანელები და სტატუსის დონეები.

---

## ⚙️ Installation & Usage (ინსტალაცია და გაშვება)

მიჰყევი ამ მარტივ ნაბიჯებს შენს ლინუქს სისტემაზე (მაგალითად Ubuntu / Kali Linux):

### 1. Clone the repository (კოდის ჩამოტვირთვა)
```bash
git clone [https://github.com/zarkuuu11/inux-security-auditor.git](https://github.com/zarkuuu11/inux-security-auditor.git)
cd inux-security-auditor
