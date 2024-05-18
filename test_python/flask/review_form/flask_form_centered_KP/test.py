from selenium import webdriver
from selenium.webdriver.common.by import By


def test_specifity1():
    print("Testing")
    driver = webdriver.Chrome()
    webpage = driver.get(
        "file:///Users/dc/test_stuff/flask/review_form1/first/point2/specificity1.html")
    print("webpage:", webpage)
    span = driver.find_element(
        by=By.TAG_NAME, value="span")
    fs = span.value_of_css_property("font-size")
    print("specifity1 span:", span, "font-size:", fs)
    webpage = driver.get(
        "file:///Users/dc/test_stuff/flask/review_form1/first/point2/specificity2.html")
    # print("webpage:", webpage)
    span = driver.find_element(
        by=By.TAG_NAME, value="span")
    fs = span.value_of_css_property("font-size")
    print("specifity2 span:", span, "font-size:", fs)
    webpage = driver.get(
        "file:///Users/dc/test_stuff/flask/review_form1/first/point2/specificity3.html")
    print("webpage:", webpage)
    span = driver.find_element(
        by=By.TAG_NAME, value="span")
    fs = span.value_of_css_property("font-size")
    print("specifity3 span:", span, "font-size:", fs)
    webpage = driver.get(
        "file:///Users/dc/test_stuff/flask/review_form1/first/point2/specificity4.html")
    print("webpage:", webpage)
    span = driver.find_element(
        by=By.TAG_NAME, value="span")
    fs = span.value_of_css_property("font-size")
    print("specifity4 span:", span, "font-size:", fs)
    driver.quit()


if __name__ == "__main__":
    test_specifity1()
