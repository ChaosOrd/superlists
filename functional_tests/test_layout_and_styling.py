import unittest
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_style(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices teh input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )


if __name__ == '__main__':
    unittest.main()
