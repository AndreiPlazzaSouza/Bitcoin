import asyncio
from pyppeteer import launch

async def create_bitcoin_wallet():
    browser = await launch(headless=False)  # Show browser for debugging
    page = await browser.newPage()
    await page.goto('https://wallet.bitcoin.com')  # Official bitcoin.com wallet URL

    # Example steps (adjust selectors as per actual site):
    # Click "Create Wallet" button
    await page.waitForSelector('button#create-wallet')  # Example selector
    await page.click('button#create-wallet')

    # Wait for seed phrase or backup step
    await page.waitForSelector('.seed-phrase')  # Example selector for seed phrase display

    # Extract seed phrase (important to save securely)
    seed_phrase = await page.evaluate('''() => {
        return document.querySelector('.seed-phrase').innerText;
    }''')
    print("Seed phrase:", seed_phrase)

    # Continue with further steps: confirm seed phrase, set password, etc.
    # Example: click next button
    await page.click('button#next-step')

    # Finish wallet creation
    await asyncio.sleep(5)  # Wait to observe

    await browser.close()

asyncio.run(create_bitcoin_wallet())
