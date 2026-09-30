from playwright.sync_api import Page, expect


def test_add_laptop_to_cart(page: Page):
    page.goto("http://127.0.0.1:8000/products.html")

    page.get_by_test_id("add-laptop").click()

    page.get_by_role("link", name="View Cart").click()

    expect(
        page.get_by_text("Laptop - $1000")
    ).to_be_visible()

    expect(
        page.get_by_text("Total: $1000")
    ).to_be_visible()