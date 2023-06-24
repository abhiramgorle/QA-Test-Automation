import re
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
        yield page
        browser.close()

@pytest.mark.required
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
    page.wait_for_url("https://acme.punchit.in/b2b/admin/dashboard")
    page.wait_for_timeout(1000)


########################################################### Organisation Details     ########################################################################################
#Edit Organisation54
@pytest.mark.skip(reason="Not needed")
def test_test2_edit_organisation(browser):
    # page.wait_for_timeout(1000)
    page = browser
    page.wait_for_timeout(1000)
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    oname = "abc"
    oslug = "acme"
    email = "kasturisivakumari93@gmail.com"
    phone = "3656695"
    website = "www.google.com"
    page.locator("div").filter(has_text=re.compile(r"^Organization Details$")).nth(2).click()
    page.locator("app-org-details div").filter(has_text="Profile Details Organization Details Organization NameOrganization SLUG Contact ").locator("img").click()
    page.get_by_label("Organization Name").click()
    page.get_by_label("Organization Name").fill(oname)
    page.get_by_label("Organization SLUG").click()
    page.get_by_label("Organization SLUG").fill(oslug)
    page.get_by_label("Email ID").click()
    page.get_by_label("Email ID").fill(email)
    page.get_by_role("spinbutton").first.click()
    page.get_by_role("spinbutton").first.fill(phone)
    page.get_by_label("URL").click()
    page.get_by_label("URL").fill(website)
    page.get_by_role("button", name="Update").click()
    page.get_by_role("button", name="Save Changes").click()

# @pytest.mark.required
def test_test11_downloadInvoices(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.get_by_text("Organization Details").click()
    page.get_by_role("row", name="3. Tue, 14 Mar 2023 18:23 TESTING (1).pdf Paid View Details").get_by_role("button",name="View Details").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download").click()
    download = download_info.value



############################################################Domains################################################################
@pytest.mark.required
def test_test12_addOwnDomain(browser):
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    domainname = "Automated Testing155"
    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Organization Logo Use Own Domains/Subdomains").click()
    page.click("//img[@src='../../../../assets/plus.svg']")
    page.get_by_label("Domain Name 1").click()
    page.get_by_label("Domain Name 1").fill(domainname)
    page.get_by_role("button", name="Add Domains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

# @pytest.mark.required
def test_test13_addSubDomain(browser):
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    d = "Automated Testing7"
    sub = "Automatted Sub Domain155"
    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Organization Logo Use Own Domains/Subdomains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(d)
    page.get_by_role("button", name="Search").click()
    time.sleep(3)
    page.get_by_role("button", name="View Details").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Subdomain 1").click()
    page.get_by_label("Subdomain 1").fill(sub)
    page.get_by_role("button", name="Add Subdomains").click()
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("button", name="Close").click()

@pytest.mark.required
def test_test14_deleteSubDomain(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.wait_for_timeout(1000)
    d = "Automated Testing7"
    sub = "Automatted Sub Domain155"
    page.get_by_text("Domains").click()
    page.get_by_role("link", name="Use Own Domains/Subdomains").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(d)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(1000)
    # page.get_by_role("row", name=d).get_by_role("button",name = "View Details").click()
    page.get_by_role("button", name="View Details").click()
    page.wait_for_timeout(1000)
    page.get_by_role("row", name=sub).get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()


################################################################Templates###############################################################
@pytest.mark.required
def test_test15_createTemplate(browser):
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    name= "Automated Testing155"
    objective = "Screening" # "Screening" or "Mock Interview" or "Interview"
    description = "no description in the automated testing"
    type = "One Way Interview"    #"One Way Interview" or "One on One Interview"
    dom = "Web dev"
    subdom = "A13"
    years = "0 - 2 Years" # "0 - 2 Years" or "2 - 4 Years" or "4+ Years"
    page.get_by_text("Template Dashboard").click()
    page.get_by_role("link", name="Organization Logo Use Own Templates").click()
    page.locator("app-header img").nth(1).click()
    page.get_by_label("Template Name").click()
    page.get_by_label("Template Name").fill(name)
    page.get_by_text("Select Objective").click()
    page.get_by_role("option", name=objective, exact=True).click()
    page.get_by_label("Template Description").click()
    page.get_by_label("Template Description").fill(description)
    page.locator("p-dropdown").filter(has_text="Select Type").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=type).click()
    page.get_by_text("Select Domain", exact=True).click()
    page.get_by_role("option", name=dom).click()
    page.locator("p-dropdown").filter(has_text="Select Sub Domain").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=subdom).click()
    page.locator("p-dropdown").filter(has_text="Select Years of Experience").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name=years).click()
    page.get_by_role("button", name="Add Template").click()
    page.get_by_role("button", name="Save Changes").click()

################################################################## Manage Admins ###############################################
####################To Add new Admin
@pytest.mark.required
def test_test3_add_admin(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    fname = "automation15"
    lname = "testing15"
    email = "testing99@automatioon.com"
    phno = "9977788999"
    page.click("//img[@src='../../../../assets/undraw_meet_the_team_re_4h08 1.svg']")
    page.click("//img[@src='../../../../assets/plus.svg']")
    page.get_by_role("textbox",name = "First Name").fill(fname)
    page.get_by_role("textbox",name = "Last Name").fill(lname)
    page.get_by_role("textbox",name = "Email ID").fill(email)
    page.fill("//input[@class='p-inputtext p-component p-element ng-untouched ng-pristine ng-invalid']",phno)
    page.click("//button[@class='btn btn-accent-blue m-0 ng-star-inserted']")
    page.click("//button[@class='btn m-0 btn-accent-blue ng-star-inserted']")
    page.click("//button[@class='btn btn-primary m-0 ng-star-inserted']")

#####################To Block Admins
@pytest.mark.required
def test_test4_block_admin(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    adminname = "testing15"
    reason = "automation Testing15"
    page.locator("div:nth-child(4) > .row > .col-12 > img").click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(adminname)
    page.get_by_role("button", name="Search").click()
    page.locator("app-organization-admin-card").filter(has_text=adminname).get_by_role("button", name="View").click()
    page.get_by_role("button", name="Block").click()
    page.locator("textarea").click()
    page.locator("textarea").fill(reason)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()


######################################## Manage Interviewer #######################################
@pytest.mark.required
def test_test5_add_interviewers(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    fname = "Automated15"
    lname = "Tesstingg15"
    email = "testinn156@automation.com"
    phno = "9555577175"
    page.click("//img[@src='../../../../assets/undraw_group_hangout_re_4t8r 2.svg']")
    page.click("//img[@src='../../../../assets/plus.svg']")
    page.get_by_role("textbox", name="First Name").fill(fname)
    page.get_by_role("textbox", name="Last Name").fill(lname)
    page.get_by_role("textbox", name="Email ID").fill(email)
    page.fill("//input[@class='p-inputtext p-component p-element ng-untouched ng-pristine ng-invalid']", phno)
    page.click("//button[@class='btn action-btn-1 m-0 ng-star-inserted']")
    page.click("//button[@class='btn m-0 btn-accent-blue ng-star-inserted']")
    page.click("//button[@class='btn btn-primary m-0 ng-star-inserted']")

@pytest.mark.required
def test_test6_block_interviewers(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    name = "Tesstingg15"
    page.click("//img[@src='../../../../assets/undraw_group_hangout_re_4t8r 2.svg']")
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(name)
    page.get_by_role("button", name="Search").click()
    page.click('app-organization-interviewer-card:has(div:text("'+name+' ")) button')
    page.get_by_role("button", name="Block").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").click()
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").fill("automation testing")
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()

def test_test7_unblock_interviewers(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    fname = "Tesstingg15"
    page.click("//img[@src='../../../../assets/undraw_group_hangout_re_4t8r 2.svg']")
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.click('app-organization-interviewer-card:has(div:text("' + fname + ' ")) button')
    page.get_by_role("button", name="Unblock").click()
    page.locator("textarea").nth(1).click()
    page.locator("textarea").nth(1).fill("Automation Testing")
    page.get_by_role("dialog", name="Confirmation").get_by_role("button").nth(2).click()

###############################################Manage Candidates ######################################################
def test_test8_blockCandidate(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    fname = "Rocky"
    reason = "Automated Testing"
    page.locator("div").filter(has_text=re.compile(r"^Manage Candidates$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.locator("app-organization-candidate-card").filter(has_text=fname).get_by_role("button", name="View").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Block").click()
    page.wait_for_timeout(1000)
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").click()
    page.wait_for_timeout(1000)
    page.get_by_role("dialog", name="Confirmation").get_by_role("textbox").fill(reason)
    page.wait_for_timeout(1000)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button", name="Block").click()

def test_test9_UnblockCandidate(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    fname = "Rocky"
    reason = "Automated Testing"
    page.locator("div").filter(has_text=re.compile(r"^Manage Candidates$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill(fname)
    page.get_by_role("button", name="Search").click()
    page.locator("app-organization-candidate-card").filter(has_text=fname).get_by_role("button", name="View").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Unblock").click()
    page.wait_for_timeout(1000)
    page.locator("textarea").nth(1).click()
    page.wait_for_timeout(1000)
    page.locator("textarea").nth(1).fill(reason)
    page.wait_for_timeout(1000)
    page.get_by_role("dialog", name="Confirmation").get_by_role("button").nth(2).click()


################################################################INterview Groups ###################################################
@pytest.mark.required
def test_test10_AddInterviewGroups(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    groupname = "Automationn Testingg15"
    interviewType = "One Way Interview"    #"One Way Interview" or "One on One Interview"
    intdur = "4 Min"                # ("{1-5} Min" for One way ) or ("{10,15,20,25,30,45,60} Mins" for One on One)
    bufforattempts = "5"            #("{1-5}" for One way ) or ("{0,2,10,15,20,25,30,45,60} Mins" for One on One)
    temptype = "Use IB Templates (Recommended)" #"Use IB Templates (Recommended)" or "Use Own Template"
    tempname = "notification testing"
    version = "Version 1 Version Description 123 test"
    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.locator("app-header img").nth(1).click()
    if interviewType == "One Way Interview":
        page.get_by_label("Name of the Interview Group").click()
        page.get_by_label("Name of the Interview Group").fill(groupname)
        page.locator("p-dropdown").filter(has_text="Select the type of interview(s)").get_by_role("button",
                                                                                                  name="dropdown trigger").click()
        page.get_by_role("option", name=interviewType).click()
        page.locator("p-dropdown").filter(has_text="Select Duration").get_by_role("button",
                                                                                  name="dropdown trigger").click()
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
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    page.locator("span").filter(has_text="Use IB Templates (Recommended)").locator("div").nth(1).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text(tempname).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text(version).click()
    page.wait_for_timeout(1000)
    page.locator("app-template-version-card").filter(has_text=version).get_by_role("button", name="Select").click()
    page.get_by_role("button", name="Next").click()
    page.wait_for_timeout(1000)
    time.sleep(3)
    page.get_by_role("button", name="Confirm & Create").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()

@pytest.mark.required
def test_test16_modifyInterviewInstructions(browser) :
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    grpname = "Automation Testing7"
    INstruction = "Automated Inviewuctions are to be modified"
    page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
    page.locator("app-header img").first.click()
    page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
    page.wait_for_timeout(1000)
    page.get_by_role("option", name=grpname).click()
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="View Details").click()
    page.wait_for_timeout(1000)
    page.locator(".col-auto > img").click()
    page.locator("textarea").click()
    page.locator("textarea").fill(INstruction)
    page.get_by_role("button", name="Save changes").click()
    page.get_by_role("button", name="Save Changes", exact=True).click()


# def test_test16_addingInterviews(browser) :
#     page = browser
#     page.goto("https://acme.punchit.in/b2b/admin/dashboard")
#     group_name = "Automation Testing7"
#     numOfInterviews = "Single" # or "Multiple"
#     Reviewers_type = "Own" # or "IB"
#     Reviewers_assign = "Auto" # or "Manual"
#     date = "June 4, 2023" # in the format of {month day, year}
#     deadline = "1 day" # "1 day" or "2 days" or "3 days"
#     review_deadline = "June 9, 2023"
#
#     page.locator("div").filter(has_text=re.compile(r"^Interview Groups$")).nth(2).click()
#     page.locator("app-header img").first.click()
#     page.locator("p-dropdown").filter(has_text="Select group name").get_by_role("button",name="dropdown trigger").click()
#     page.get_by_role("option", name=group_name).click()
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("button", name="View Details").click()
#     page.get_by_role("button", name="Add Interview").click()
#     if numOfInterviews == "Single" :
#         page.locator(".p-radiobutton-box").first.click()
#     else :
#         page.locator(".col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").first.click()
#     if Reviewers_type == "Own" :
#         page.locator("div:nth-child(4) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#         if Reviewers_assign == "Auto" :
#             page.locator("div:nth-child(6) > .col-5 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#         else :
#             page.locator("div:nth-child(6) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#     else :
#         page.locator("div:nth-child(4) > .col-7 > .p-field-radiobutton > .p-element > .p-radiobutton > .p-radiobutton-box").click()
#
#     page.get_by_role("button", name="Next").click()
#     page.get_by_label("Date").fill(date)
#     page.get_by_label("Date").press("Enter")
#     page.locator("p-dropdown").filter(has_text="Please select Deadline").get_by_role("button",name="dropdown trigger").click()
#     page.get_by_role("option", name=deadline).click()
#     page.get_by_text("Please select timezone").click()
#     page.get_by_role("option", name="IST(GMT +5:30)").click()
#     page.get_by_label("Deadline for review").fill(review_deadline)
#     page.get_by_label("Date").press("Enter")
#     page.get_by_role("button", name="Next").click()
#     page.get_by_text("Choose").click()
#     page.locator("span").filter(has_text="Choose").first.set_input_files("Single_Candidate_details_sheet.xlsx")
#     page.get_by_role("button", name="Upload").click()
#     page.get_by_role("button", name="Next").click()
#     if Reviewers_type != "Own" :
#         page.get_by_role("textbox").click()
#         page.get_by_role("textbox").fill("Automated Testing")
#         page.get_by_role("checkbox").check()
#     else :
#         page.locator("#interviewer_name_search").click()
#         page.locator("#interviewer_name_search").fill("Akhil")
#         page.get_by_role("dialog", name="Add Interview").locator("i").click()
#         page.get_by_role("button", name="Select").click()
#     page.get_by_role("button", name="Next").click()
#     page.get_by_role("button", name="Confirm & Create").click()
#     page.get_by_role("button", name="Save Changes").click()
#     page.get_by_role("button", name="Close").click()
#     page.get_by_role("link", name="").click()



################################################################Logout###########################################################
def test_test100_logout(browser):
    page = browser
    page.goto("https://acme.punchit.in/b2b/admin/dashboard")
    page.get_by_role("button").click()
    page.get_by_role("button", name="Logout").click()
