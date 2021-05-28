from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    content, author and tag
    """

    def __init__(self,parent):
        self.parent=parent

    def __repr__(self):
        return f"< Quote : {self.content} : by {self.author} >"

    @property
    def content(self):
        locator=QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def TAGS(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator)]




