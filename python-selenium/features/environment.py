from utilities.webapp import webApp
from behave import *

def before_scenario(context, step):
    if "web" in context.tags:
        webApp.get_driver().refresh()
        print("Inside the before_scenario")

def after_feature(context, step):
    if "web" in context.tags:
        webApp.get_driver().quit()
        print("Inside the after_feature")


