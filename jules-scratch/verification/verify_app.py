from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Go to the application
        page.goto("http://localhost:4200")

        # Wait for the connection status to be "Conectado"
        connected_status = page.locator("span.connected")
        expect(connected_status).to_have_text("✅ Conectado", timeout=10000) # Increased timeout for initial load

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run_verification()