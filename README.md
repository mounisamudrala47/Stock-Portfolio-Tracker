# 📈 Stock Portfolio Tracker

A simple command-line **Stock Portfolio Tracker** built with Python. This application allows users to enter their stock holdings, calculates the investment value for each stock, displays a portfolio summary, and generates a report in a text file.

## 📌 Features

* View available stock prices
* Add multiple stock holdings
* Input validation for stock symbols and quantities
* Automatically combines duplicate stock entries
* Calculates investment value for each stock
* Displays the total portfolio value
* Generates a portfolio report (`portfolio_report.txt`)

## 🛠️ Technologies Used

* Python 3
* File Handling
* Dictionaries
* Loops and Conditional Statements
* Exception Handling (`try` / `except`)

## 📂 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt    # Generated after running the program
└── README.md
```

## ▶️ How to Run

1. Ensure Python 3 is installed on your system.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python stock_portfolio_tracker.py
```

## 📊 Available Stocks

| Stock Symbol | Price (USD) |
| ------------ | ----------: |
| AAPL         |        $180 |
| TSLA         |        $250 |
| GOOGL        |        $150 |
| MSFT         |        $320 |
| AMZN         |        $140 |

> **Note:** The stock prices are hardcoded for demonstration purposes.

## 🎯 How It Works

1. Displays the list of available stocks and their prices.
2. Prompts the user to enter the number of different stocks they own.
3. Collects the stock symbol and quantity for each holding.
4. Validates user input to prevent invalid entries.
5. Calculates the investment value for each stock.
6. Displays a portfolio summary.
7. Saves the report to **portfolio_report.txt**.

## 💻 Example Output

```text
========================================
      STOCK PORTFOLIO TRACKER
========================================

Available Stocks:
AAPL : $180
TSLA : $250
GOOGL : $150
MSFT : $320
AMZN : $140

Enter the number of different stocks you own: 2

Stock 1
Enter Stock Symbol: AAPL
Enter Quantity: 5

Stock 2
Enter Stock Symbol: TSLA
Enter Quantity: 3

========================================
        PORTFOLIO SUMMARY
========================================

Stock       : AAPL
Price       : $180
Quantity    : 5
Investment  : $900

Stock       : TSLA
Price       : $250
Quantity    : 3
Investment  : $750

========================================
Total Investment Value = $1650
========================================

Portfolio report has been saved as 'portfolio_report.txt'
```

## 📚 Concepts Covered

* Python Dictionaries
* User Input
* Input Validation
* Exception Handling
* Loops (`for`, `while`)
* Conditional Statements
* File Handling
* Basic Financial Calculations

## 🚀 Future Improvements

* Fetch live stock prices using a financial API
* Add buy and sell transaction history
* Calculate profit/loss based on purchase price
* Export reports in CSV or Excel format
* Create a graphical user interface (GUI)
* Store portfolio data in a database
* Visualize portfolio performance with charts

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

