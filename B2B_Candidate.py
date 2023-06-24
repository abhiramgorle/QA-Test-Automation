import re
import time
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://acme.punchit.in/b2b/candidate/login")
        yield page
        browser.close()

@pytest.mark.required
def test_test1_login(browser):
    page = browser
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").fill("alcovextest@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").fill("alcovex1234")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_url("https://acme.punchit.in/b2b/candidate/dashboard")
    page.wait_for_timeout(1000)

######################################## Profile #######################################

@pytest.mark.required
def test_editProfileDetails(browser):
    page = browser
    page.get_by_text("View Profile").click()
    # page.locator("app-organization-candidate-profile-details div").filter(has_text="Basic Details First NameLast NameNick NameYear of Birth1981GenderMale").locator("img").click()
    page.click("//img[@src='../../../../assets/edit.svg']")
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").press("Control+a")
    page.get_by_label("First Name").fill("Automation")
    # page.get_by_label("First Name").fill("Testing")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").press("Control+a")
    page.get_by_label("Last Name").fill("Testing")
    # page.get_by_label("Last Name").fill("Account")
    page.get_by_label("Nick Name").click()
    page.get_by_label("Nick Name").press("Control+a")
    page.get_by_label("Nick Name").fill("Playwright")
    # page.get_by_label("Nick Name").fill("Automation")
    # page.locator("p-dropdown").filter(has_text="1981").get_by_role("button", name="dropdown trigger").click()
    # page.get_by_role("option", name="1980").click()
    page.locator("p-dropdown").filter(has_text="1980").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="1981").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

######################################## Interviews #######################################

@pytest.mark.required

# CREATE INTERVIEW FIRST

# def test_joinInterview(browser):
#     page = browser
#     with page.expect_popup() as page1_info:
#         page.get_by_role("button", name="Join Interview").click()
#     page1 = page1_info.value
#     page1.get_by_role("button", name="Join").click()
#     # page1.close()

#  @pytest.mark.required
# def test_viewInterviewDetails(browser):
#     page = browser
#     page.goto("https://acme.punchit.in/b2b/candidate/dashboard")
#     interviewName = "test123"
#     page.get_by_role("link", name="").click()
#     page.get_by_text("View all Interviews").click()
#     page.get_by_role("row", name=interviewName).get_by_role("button", name="View details").click()
#     page.get_by_role("link", name="").click()

######################################## Feedback #######################################

#@pytest.mark.required
def test_giveFeedback(browser):
    page = browser
    page.get_by_text("View all Interviews").click()
    page.get_by_role("link", name="").click()
    page.get_by_text("View all Interviews").click()
    page.get_by_role("row", name="Sample").get_by_role("button", name="View details").click()
    page.get_by_role("tab", name=" Your Feedback").click()
    page.get_by_role("region", name=" Your Feedback").locator("img").click()
    page.locator("div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
    page.locator("div:nth-child(6) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.locator("div:nth-child(8) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.locator("div:nth-child(10) > .row > div:nth-child(5) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    # page.locator("div:nth-child(10) > .row > div:nth-child(6) > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="").click()

######################################## Logout #######################################

@pytest.mark.required
def test_logout(browser):
    # page.goto("https://acme.punchit.in/b2b/candidate/dashboard")
    page = browser
    page.locator("app-navbar").get_by_role("button").click()
    page.get_by_role("button", name="Logout").click()