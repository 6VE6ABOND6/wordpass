# wordpass 


**wordpass** is an, wordlist generator designed for penetration testing and security research. 

---

## 📦 Installation

You can install WordPass in two ways:

### Option 1: Easy Install (.deb Package) 
*Recommended for Kali Linux, Ubuntu, Debian users.*

1. Download the latest **`wordpass.deb`** file from the [Releases](../../releases) page.
2. Open your terminal in the download folder and run:

```bash
sudo apt install ./wordpass.deb
```

### 2. Install Required Libraries

Only regex is required beyond standard libraries.
```bash
pip install regex
```
Run:

```bash
wordpass
```

## Option 2: Manual Install (Source Code) 🛠️
For Windows users or developers.

1. Clone the Repository
   
```bash
git clone [https://github.com/6VE6ABOND6/wordpass.git](https://github.com/6VE6ABOND6/wordpass.git)
cd wordpass
```
2. Install Required Libraries

```bash
pip install regex
```

3. Run the Tool

```bash
python3 wordpass.py
```

### Usage

Step-by-Step:
1. Region Selection: Enter tr (for Turkey).

2. Information Entry: Input known details about the target (Name, Surname, Partner's Name, etc.).

    If you don't know a detail, just press Enter to skip.

3. Generation: The program will save the generated passwords to letstry.txt within seconds.

<img width="706" height="275" alt="Ekran görüntüsü 2026-02-01 213028" src="https://github.com/user-attachments/assets/38270474-1494-4b57-ba21-d8fb43bfdaa9" />

### ⚠️ Disclaimer
Use responsibly.

This tool is developed for educational and security testing (Pentest) purposes only. Using it on systems without permission is illegal. The developer is not responsible for any misuse or damage caused by this tool.

Contact & Contribution
If you would like to contribute to the development, feel free to submit a Pull Request or contact me.

Developer: VEGABOND

