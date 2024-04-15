from pages.filter_page import FilterPage

def test_sort_products_by_price_low_to_high(driver):
    filter_page = FilterPage(driver)
    filter_page.open("https://demowebshop.tricentis.com/desktops")
    price_low_to_high_value = "https://demowebshop.tricentis.com/desktops?viewmode=list&pagesize=4&orderby=10"
    filter_page.sort_products(price_low_to_high_value)
    assert "orderby=10" in driver.current_url, "The products were not sorted 'Price: Low to High'"
