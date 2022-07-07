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
1. Imports
```python
from [framework].utils.browser.webdriver import WebDriverFactory, WebDriver
from [framework].common.browser_name import BrowserName
```
2. Get driver instance (singleton)
```python
driver = WebDriverFactory.get_browser([BrowserName.Chrome/Browser.Firefox]).get_driver()
```

3. One of element usage example
```python
    button = Button("Tab Button", (By.XPATH, "//button[@id='tabButton']"), 15))
    button.click()
```

4. Graceful shutdown
```python
WebDriver.quit()
```
