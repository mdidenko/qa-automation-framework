# Python Framework for Web Automation QA
**This package is an add-on for Selenium WebDriver.**

### Supported browsers
- Google Chrome
- Mozilla Firefox

### Supported web elements
- Button
- Dropdown menu
- Dropdowm menu item
- iFrame
- Link
- Progress bar
- Text
- Text field

### Quick start
1. Get driver instance
```python
from [framework].utils.browser.webdriver import WebDriverFactory, WebDriver
from [framework].common.browser_name import BrowserName

browser = WebDriverFactory.get_browser([BrowserName.Chrome/BrowserName.Firefox])
driver = WebDriver.get_driver()  # singleton
```

2. One of element usage example
```python
from [framework].utils.browser.elements import Button

button = Button("Tab Button", (By.XPATH, "//button[@id='tabButton']"), 15)
button.click()
```

3. Graceful shutdown
```python
WebDriver.quit()
```
