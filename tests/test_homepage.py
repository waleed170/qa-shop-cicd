from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    page.goto("http://127.0.0.1:8000")

    page.wait_for_timeout(3000)

    expect(
        page.get_by_role("heading", name="Welcome to QA Shop")
    ).to_be_visible()