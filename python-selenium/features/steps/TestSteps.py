from behave import *
from pages.google import google

@then(u'I can see the product information pages')
def step_impl(context):
    google.product_list_page()

@given(u'Launch the application url \'{url}\'')
def step_impl(context, url):
    google.launch_application(url)


@when(u'I search for the keyword \'{keyword}\'')
def step_impl(context, keyword):

    if keyword == "python":
        google.search_google(keyword)
    else :
        google.search_amazon(keyword)

@then(u'I can see the results wih links')
def step_impl(context):

    google.google_list_page()



