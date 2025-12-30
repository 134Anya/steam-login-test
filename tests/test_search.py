import pytest

from data.test_data import GAMES_DATA
from pages.result_page import ResultPage


@pytest.mark.parametrize("game_name, qty", GAMES_DATA)
def test_sort_prices(open_main_page, driver, game_name, qty):
    main_page = open_main_page
    main_page.search_game(game_name)

    result_page = ResultPage(driver)
    result_page.wait_for_page_loaded()
    result_page.sort_by_price_desc()

    actual_prices = result_page.get_prices(qty)
    print(f"Цены для '{game_name}': {actual_prices}")
    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices, \
        (f"Цены отсортированы не по убыванию."
         f"Ожидаемая сортировка цен: {expected_prices}\n"
         f"Фактическая сортировка цен:  {actual_prices}")
