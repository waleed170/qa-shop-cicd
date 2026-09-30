from playwright.sync_api import Page, expect


def test_products_page(page: Page):
    page.goto("http://127.0.0.1:8000/products.html")

    expect(
        page.get_by_role("heading", name="Products")
    ).to_be_visible()

    expect(
        page.get_by_role("heading", name="Laptop")
    ).to_be_visible()

    expect(
        page.get_by_role("heading", name="Mouse")
    ).to_be_visible()

    expect(
        page.get_by_role("heading", name="Keyboard")
    ).to_be_visible()