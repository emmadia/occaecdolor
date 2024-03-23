def close_info(driver):
    """Closes the info box on the map."""

    try:
        info_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'info-box')))
        info_box.find_element_by_css_selector('.close').click()
    except TimeoutException:
        pass

