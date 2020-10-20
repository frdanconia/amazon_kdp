from selenium import webdriver


def get_url(asin_number):
    return f'https://www.amazon.com/gp/product/{asin_number}/'


def get_data_using_asin(asin_number):
    """This function getting data about book from KDP Amazon using ASIN number"""

    driver = webdriver.Chrome('./src/product/chromedriver')

    url = get_url(asin_number)
    driver.get(url)
    driver.implicitly_wait(2)

    driver.find_element_by_css_selector('span.a-button.a-spacing-top-base.a-button-base.glow-toaster-button.glow-toaster-button-dismiss > span > input').click()
    driver.find_element_by_css_selector('#bdSeeAllPrompt').click()

    """Using css selector we can download data about our book."""
    title = driver.find_element_by_css_selector('#productTitle').text
    author = driver.find_element_by_css_selector('#bylineInfo > span > span.a-declarative > a.a-link-normal.contributorNameID').text
    price = driver.find_element_by_css_selector('#a-autoid-7-announce > span.a-color-base > span').text
    categories = driver.find_elements_by_css_selector('span.zg_hrsr_ladder > a')
    print_format = driver.find_element_by_css_selector('#productDetailsTable > tbody > tr > td > div > ul > li:nth-child(2)').text

    fr = driver.find_element_by_id("bookDesc_iframe")
    driver.switch_to.frame(fr)
    description = driver.find_element_by_id('iframeContent').text
    driver.switch_to.default_content()

    """Here we get cover images"""
    driver.find_element_by_css_selector('#imgThumbs > div:nth-child(1) > img').click()
    img1_url = driver.find_element_by_css_selector('div > #igImage').get_attribute('src')
    driver.find_element_by_css_selector('div > #ig-thumb-1').click()
    img2_url = driver.find_element_by_css_selector('div > #igImage').get_attribute('src')

    "All data have been stored in dict"
    product_details = {
        'ASIN': asin_number,
        'title': title,
        'author': author,
        'price': price,
        'categories': {
            'category_1': categories[0].text,
            'category_2': categories[1].text
        },
        'print_format': print_format,
        'img_url': {
            'img1_url': img1_url,
            'img2_url': img2_url
        },
        'description': description,
        'url': url
    }

    driver.close()

    return product_details


print(get_data_using_asin('108127316X'))