# Investment Simulation Script - README

This document will guide you step-by-step on how to run the investment simulation script, even if you have no prior computer knowledge.

---

## Prerequisites

### 1. **Install Python:**
   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Download the latest version for your operating system (Windows or Mac).
   - Run the downloaded file and **check the box** that says **"Add Python to PATH"** during installation.
   - Click **Install Now** and follow the prompts.

### 2. **Download the Script and CSV File:**
   - Ensure you have the files `simulate_portfolio.py` and `stocks_money_invest_history.csv` in the same folder on your computer.

---

## Running the Script

### **Step 1: Open the Command Prompt or Terminal:**
- **Windows:** Press `Win + R`, type `cmd`, and hit Enter.
- **Mac:** Press `Cmd + Space`, type `Terminal`, and hit Enter.

### **Step 2: Navigate to the Folder with the Files:**
- Type the following command (adjust the path to where the files are stored):
   - **Windows:** `cd path\to\your\folder`
   - **Mac:** `cd /path/to/your/folder`

### **Step 3: Install Required Libraries:**
- Type the following command and press **Enter**:
   ```
   pip install pandas yfinance
   ```
- Wait for the installation to finish.

### **Step 4: Run the Script:**
- Type the following command and press **Enter**:
   ```
   python simulate_portfolio.py
   ```

---

## Results and Output

- The script will display the portfolio details and total value directly in the command window.
- A CSV file will be generated in the same folder, named like `final_portfolio_1234.csv` (a random number is added to avoid overwriting previous results).
- Open this CSV file with Excel or any spreadsheet application to view the results.

---

## Troubleshooting

- **Python not recognized error?**
   - Ensure Python was added to PATH during installation.
   - If not, reinstall Python and check the **"Add Python to PATH"** box.

- **Permission Denied Error?**
   - Ensure you have write permissions for the folder where the script and CSV file are saved.

- **Other Issues?**
   - Feel free to reach out for help if you run into any problems!

---

**Enjoy using the investment simulation script! 😊**

