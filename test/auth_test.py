from page.AuthPage import AuthPage
from page.MainPage import MainPage

def auth_test(browser):
    email = "dagoryal@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "dagoryal_1306")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("dagoryal/boards")
    assert info[0] == "Дарья"
    assert info[1] == email

    