class ElementChecker:
    def __init__(self, browser):
        self.browser = browser

    def has_any_class(self, element_classes, expected_classes):
        return any(cls in element_classes for cls in expected_classes)