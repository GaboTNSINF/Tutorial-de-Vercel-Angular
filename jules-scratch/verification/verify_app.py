from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:4200")

    # Wait for the connection status to be "Conectado"
    expect(page.locator(".connection-status span.connected")).to_have_text("✅ Conectado")

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)