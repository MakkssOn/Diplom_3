class Url:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = f'{MAIN_PAGE}/login'
    HISTORY_PAGE = f'{MAIN_PAGE}/account/order-history'
    FEED_PAGE = f'{MAIN_PAGE}/feed'


class Ingredients:
    BUN = "61c0c5a71d1f82001bdaaa6d"
    MEAT = '61c0c5a71d1f82001bdaaa6f'
    KOKLETA = '61c0c5a71d1f82001bdaaa71'
    SAUCE = '61c0c5a71d1f82001bdaaa72'
    ENIGMA = '00000000000000000000000000'


class API:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register'
    CREATE_ORDER = f'{MAIN_PAGE}/api/orders'
    DELETE_DATA = f'{MAIN_PAGE}/api/auth/user'
