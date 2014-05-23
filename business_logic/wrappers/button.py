import webdriver

# Button Wrapper
class ButtonFactory(object):
  def _init_(self, locator, action):
    self.locator = locator
    self.action = action
    
  
# Button Declaration
class Button(object):
  def _init_(self, locator):
    self.locator = locator
  
  def get_button_by_xpath(self):
    pass
  
  def get_button_by_id(self):
    pass
  
  def get_button_by_css(self):
    pass
  
  def get_button_by_class(self):
    pass
