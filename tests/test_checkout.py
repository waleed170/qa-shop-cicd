from playwright.sync_api import Page, expect


def test_checkout(page: Page):
    page.goto("http://127.0.0.1:8000/products.html")

    page.get_by_test_id("add-laptop").click()

    page.get_by_role("link", name="View Cart").click()

    page.get_by_role("link", name="Proceed to Checkout").click()
    page.locator("#name").fill("John Smith")
    page.locator("#address").fill("123 Main Street")
    page.locator("#card").fill("4111111111111111")
    page.get_by_role("button", name="Place Order").click()
    expect(page.get_by_role("heading", name="Order Confirmed!")).to_be_visible()