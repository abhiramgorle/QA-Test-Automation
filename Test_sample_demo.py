import re
import os
import time
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False,slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://acme.punchit.in/b2b/admin/login")
        # app_path = os.getenv("LOCALAPPDATA")
        # user_path = "C:\\Users\\asust\\AppData\\Local\\Google\\Chrome\\User Data\\Profile31"
        # context =  playwright.chromium.launch_persistent_context(user_path,headless=False,slow_mo=1000)
        yield page
        context.close()

# @pytest.fixture()
# def b2b_browser(browser) :
#     context = browser
#     page = context.new_page()
#     page.goto("https://acme.punchit.in/b2b/admin/login")

def test_test1_login(browser):
    page = browser
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Email or phone").fill("abhiramgorle6@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter your Password").fill("1234@Gmail")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.wait_for_url("https://acme.punchit.in/b2b/admin/dashboard")
    # page.wait_for_timeout(40000)
# @pytest.fixture()
def test_test2_intgrp(browser) :
    page = browser
    page.wait_for_timeout(1000)
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    groupname = "Demonstration"
    interviewType = "One Way Interview"    #"One Way Interview" or "One on One Interview"
    intdur = "3 Min"                # ("{1-5} Min" for One way ) or ("{10,15,20,25,30,45,60} Mins" for One on One)
    bufforattempts = "5"            #("{1-5}" for One way ) or ("{0,2,10,15,20,25,30,45,60} Mins" for One on One)
    temptype = "Use IB Templates (Recommended)" #"Use IB Templates (Recommended)" or "Use Own Template"
    tempname = "notification testing"
    version = "Version 1 Version Description 123 test"
    # page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    # page.locator("div:nth-child(7) > .row > .col-12 > img").click()
    page.get_by_text("Interview Groups").click()
    page.locator("app-header img").nth(1).click()
    if interviewType == "One Way Interview":
        page.get_by_label("Name of the Interview Group").click()
        page.get_by_label("Name of the Interview Group").fill(groupname)
        page.locator("p-dropdown").filter(has_text="Select the type of interview(s)").get_by_role("button",name="dropdown trigger").click()
        page.get_by_role("option", name=interviewType).click()
        page.locator("p-dropdown").filter(has_text="Select Duration").get_by_role("button",name="dropdown trigger").click()
        page.get_by_role("option", name=intdur).click()
        page.wait_for_timeout(1000)
        page.locator("p-dropdown").filter(has_text="Select no of attempts").get_by_role("button",
                                                                                        name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=bufforattempts).click()

    else:
        page.get_by_label("Name of the Interview Group").click()
        page.get_by_label("Name of the Interview Group").fill(groupname)
        page.locator("p-dropdown").filter(has_text="Select the type of interview(s)").get_by_role("button",
                                                                                                  name="dropdown trigger").click()
        page.get_by_role("option", name=interviewType).click()
        page.locator("p-dropdown").filter(has_text="Select Duration").get_by_role("button",
                                                                                  name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=intdur).click()
        page.locator("p-dropdown").filter(has_text="Select Buffer").get_by_role("button",
                                                                                name="dropdown trigger").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=bufforattempts).click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("span").filter(has_text="Use IB Templates (Recommended)").locator("div").nth(1).click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(10000)
    page.locator("div:nth-child(3) > .card > app-template-card > div").click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("app-template-version-card").filter(
        has_text="Version 1 Version Description 123 test ViewSelect").get_by_role("button", name="Select").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Confirm & Create").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()

def test_test3_interviewcreate(browser) :
    page = browser
    page.wait_for_timeout(1000)
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.wait_for_timeout(1000)
    page.locator("app-organization-interview-group-card").filter(has_text="Demonstration").get_by_role("button", name="View Details").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Add Interviews").click()
    page.wait_for_timeout(1000)
    page.locator(".p-radiobutton-box").first.click()
    page.locator("div:nth-child(4) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.locator("div:nth-child(6) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_label("Date").click()
    page.get_by_label("Date").fill("21/06/2023")
    page.get_by_label("Date").press("Enter")
    page.get_by_label("Deadline for attempting the Interview").click()
    page.get_by_label("Deadline for attempting the Interview").fill("22/06/2023")
    page.get_by_label("Deadline for attempting the Interview").press("Enter")
    page.get_by_text("Please select timezone").click()
    page.get_by_text("IST(GMT +5:30)").click()
    page.get_by_label("Deadline for review").click()
    page.get_by_label("Deadline for review").fill("24/06/2023")
    page.get_by_label("Deadline for review").press("Enter")
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("p-button").filter(has_text="Upload").click()
    page.locator("p-button").filter(has_text="Upload").click()
    page.locator("span").filter(has_text="Choose").first.click()
    crnt_dir = os.getcwd()
    file_path = os.path.join(crnt_dir, 'Candidate_Details_sheets\\Single_Candidate_details_sheet.xlsx')
    with page.expect_file_chooser() as fc_info:
        page.locator("span").filter(has_text="Choose").first.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("app-organization-interviewer-card").filter(has_text="Abhiram Gorla abhiramgorle6@gmail.com +91 - 9490076650Active ViewSelect").get_by_role("button", name="Select").click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Confirm & Create").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()


def test_test5_newpage(browser) :
    page = browser.context.new_page()
    page.goto("https://acme.punchit.in/b2b/candidate/login")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(10000)
    page.locator("div").filter(has_text=re.compile(r"^Abhiram Gorle\.$")).click()
    page.wait_for_timeout(100000)
    page.wait_for_url("https://acme.punchit.in/b2b/candidate/dashboard")


#     page.locator("span").filter(has_text=temptype).locator("div").first.click()
#     page.get_by_role("button", name="Next").click()
#     page.locator("div:nth-child(2) > .card > app-template-card > .row").click()
#     page.get_by_role("button", name="Next").click()
#     page.wait_for_timeout(1000)
#     page.locator("app-template-version-card").filter(
#         has_text="Version 1 Version Description 123 test Select").get_by_role("button", name="Select").click()
#     page.get_by_role("button", name="Next").click()
#     page.wait_for_timeout(1000)
#     # time.sleep(3)
#     page.get_by_role("button", name="Confirm & Create").click()
#     page.wait_for_timeout(1000)
#     page.get_by_role("button", name="Save Changes").click()
#     page.goto("https://acme.punchit.in/b2b/admin/dashboard")
#     group_name = "Bubbledemo3"
#     numOfInterviews = "Single" # or "Multiple"
#     Reviewers_type = "IB" # or "IB"
#     Reviewers_assign = "Auto" # or "Manual"
#     date = "June 4, 2023" # in the format of {month day, year}
#     deadline = "1 day" # "1 day" or "2 days" or "3 days"
#     review_deadline = "June 9, 2023"
#     crnt_dir = os.getcwd()
#     file_path = os.path.join(crnt_dir,'Candidate_Details_sheets\\Single_Candidate_details_sheet.xlsx')
#
#     # page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
#     page.get_by_text("Interview Groups").click()
#     time.sleep(5)
#     # page.locator("app-header img").first.click()
#     # page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
#     # page.get_by_role("option", name=group_name).click()
#     # page.get_by_role("button", name="Search").click()
#     # page.get_by_role("button", name="View Details").click()
#     # page.get_by_role("button", name="Add Interview").click()
#     page.locator("app-organization-interview-group-card").filter(has_text=group_name).get_by_role("button", name="View Details").click()
#     page.get_by_role("button", name="Add Interviews").click()
#     page.locator(".p-radiobutton-box").first.click()
#     page.locator("div:nth-child(4) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     page.get_by_role("button", name="Next").click()
#     page.get_by_label("Date").fill("08/06/2023")
#     page.get_by_label("Date").press("Enter")
#     # page.get_by_label("Deadline for attempting the Interview").click()
#     page.get_by_label("Deadline for attempting the Interview").fill("10/06/2023")
#     page.get_by_label("Deadline for attempting the Interview").press("Enter")
#     page.get_by_role("dialog", name="Add Interview").get_by_role("button", name="dropdown trigger").click()
#     page.get_by_role("option", name="IST(GMT +5:30)").click()
#     page.get_by_label("Deadline for review").click()
#     page.get_by_label("Deadline for review").fill("14/06/2023")
#     page.get_by_label("Deadline for review").press("Enter")
#     page.get_by_role("button", name="Next").click()
#     with page.expect_file_chooser() as fc_info:
#         page.locator("span").filter(has_text="Choose").first.click()
#     file_chooser = fc_info.value
#     file_chooser.set_files(file_path)
#
#     # page.locator("span").filter(has_text="Choose").first.set_input_files(file_path)
#     page.get_by_role("button", name="Upload").click()
#     page.wait_for_timeout(4000)
#     page.get_by_role("button", name="Next").click()
#     page.locator("textarea").click()
#     page.locator("textarea").fill("Hello Testing")
#     page.locator("div").filter(has_text=re.compile(r"^I have read and understood the disclamer\.$")).click()
#     page.get_by_role("checkbox").check()
#     page.get_by_role("button", name="Next").click()
#     page.get_by_role("button", name="Confirm & Create").click()
#     page.get_by_role("button", name="Save Changes").click()
#     page.get_by_role("button", name="Close").click()
#
# #     #
#     # page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
#     # page.locator("app-header img").first.click()
#     # page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
#     # page.get_by_role("option", name=group_name).click()
#     # page.get_by_role("button", name="Search").click()
#     # page.get_by_role("button", name="View Details").click()
#     # page.get_by_role("button", name="Add Interview").click()
#     # if numOfInterviews == "Single" :
#     #     page.locator(".p-radiobutton-box").first.click()
#     # else :
#     #     page.locator(".col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
#     # if Reviewers_type == "Own" :
#     #     page.locator("div:nth-child(4) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     #     if Reviewers_assign == "Auto" :
#     #         page.locator("div:nth-child(6) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     #     else :
#     #         page.locator("div:nth-child(6) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     # else :
#     #     page.locator("div:nth-child(4) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     #
#     # page.get_by_role("button", name="Next").click()
#     # page.get_by_label("Date").fill(date)
#     # page.get_by_label("Date").press("Enter")
#     # page.locator("p-dropdown").filter(has_text="Please select Deadline").get_by_role("button",name="dropdown trigger").click()
#     # page.get_by_role("option", name=deadline).click()
#     # page.get_by_text("Please select timezone").click()
#     # page.get_by_role("option", name="IST(GMT +5:30)").click()
#     # page.get_by_label("Deadline for review").fill(review_deadline)
#     # page.get_by_label("Date").press("Enter")
#     # page.get_by_role("button", name="Next").click()
#     # page.get_by_text("Choose").click()
#     # page.locator("span").filter(has_text="Choose").first.set_input_files("Single_Candidate_details_sheet.xlsx")
#     # page.get_by_role("button", name="Upload").click()
#     # page.get_by_role("button", name="Next").click()
#     # if Reviewers_type != "Own" :
#     #     page.get_by_role("textbox").click()
#     #     page.get_by_role("textbox").fill("Automated Testing")
#     #     page.get_by_role("checkbox").check()
#     # else :
#     #     page.locator("#interviewer_name_search").click()
#     #     page.locator("#interviewer_name_search").fill("Akhil")
#     #     page.get_by_role("dialog", name="Add Interview").locator("i").click()
#     #     page.get_by_role("button", name="Select").click()
#     # page.get_by_role("button", name="Next").click()
#     # page.get_by_role("button", name="Confirm & Create").click()
#     # page.get_by_role("button", name="Save Changes").click()
#     # page.get_by_role("button", name="Close").click()

@pytest.mark.skip(reason="sfsaf")
def test_test6_damnitt(browser) :
    context = browser
    page = context.new_page()
    page.goto("https://acme.punchit.in/b2b/interviewer/login")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Sign in with Google").click()
    page.wait_for_timeout(10000)
    page.locator("div").filter(has_text="Abhiram Gorle").click()
    page.wait_for_timeout(1000)
    page.wait_for_url("https://acme.punchit.in/b2b/interviewer/dashboard")
    # page.get_by_role("button", name="Sign in with Google").click()
    # page.wait_for_timeout(1000)
    # page.get_by_role("textbox", name="Email or phone").click()
    # page.wait_for_timeout(1000)
    # page.get_by_role("textbox", name="Email or phone").fill("abhiramgorle6@gmail.com")
    # page.wait_for_timeout(1000)
    # page.get_by_role("button", name="Next").click()
    # page.wait_for_timeout(1000)
    # page.get_by_role("textbox", name="Enter your Password").click()
    # page.wait_for_timeout(1000)
    # page.get_by_role("textbox", name="Enter your Password").fill("1234@Gmail")
    # page.wait_for_timeout(1000)
    # page.get_by_role("button", name="Next").click()
    # page.wait_for_timeout(40000)
    page.wait_for_url("https://acme.punchit.in/b2b/interviewer/dashboard")

