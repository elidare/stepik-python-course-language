import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"

def test_button_add_to_cart_is_present(browser):
    browser.get(link)    
    buttons = browser.find_elements_by_css_selector("#add_to_basket_form [type='submit']")

    # Смотрим, что на странице один элемент с таким селектором
    assert len(buttons) == 1, "Add to cart button is not present"

    #time.sleep(30)
