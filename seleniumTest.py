from selenium import webdriver
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")
inputele= driver.find_element_by_css_selector('input[name=q]')
inputele.send_keys('dice.com')
inputele.submit()
elem=driver.find_element_by_link_text("dice.com")
elem.click()
searchelm=driver.find_element_by_css_selector('input[class="form-control ng-tns-c28-0 ng-star-inserted"]')
searchelm.send_keys('ETL TESTER')
searchelm=driver.find_element_by_id("google-location-search")
searchelm.send_keys('St. Louis,MO')
searchelm=driver.find_element_by_id("submitSearch-button")
searchelm.click()
driver.get_screenshot_as_file("screenshot.jpeg")
#driver.close()
#driver.quit()
