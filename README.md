
# Bitcoin

**Automate Wallet Creator on Bitcoin.com**


This project provides tools and scripts to automate the creation of Bitcoin wallets on [Bitcoin.com](https://www.bitcoin.com) using Python. It leverages browser automation to simulate user interactions, making it easier to generate wallets for testing, development, or educational purposes.

> **Note:** This repository is for educational and testing purposes only. Never use automated wallets for storing significant funds. Always keep your seed phrases secure!

---

## Features

- 📄 Automate wallet creation on [Bitcoin.com](https://wallet.bitcoin.com)
- 🤖 Uses Python and browser automation (Pyppeteer)
- 🔑 Extracts and displays wallet seed phrases for backup
- 🛠️ Easily customizable for other web automation tasks

---

## Getting Started

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndreiPlazzaSouza/Bitcoin.git
    cd Bitcoin
    ```

2. **Install dependencies:**
    ```bash
    pip install pyppeteer
    ```

---

## Usage

The main script is `btc.py`. It automates wallet creation on Bitcoin.com.

```bash
python btc.py
```

By default, the script will:

- Open a browser window
- Navigate to the Bitcoin.com wallet page
- Simulate the process of creating a new wallet
- Extract and print the generated seed phrase

> **Important:**  
> - Update CSS selectors in the script if Bitcoin.com changes its web interface.
> - Never share your seed phrase. This script is for demonstration only.

---

## Example

```python
import asyncio
from pyppeteer import launch

async def create_wallet():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://wallet.bitcoin.com')
    # Add your automation steps here
    await asyncio.sleep(5)
    await browser.close()

asyncio.run(create_wallet())
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

