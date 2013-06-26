from django.test import TestCase

from . import settings
from .paginator import Paginator

class PaginatorTest(TestCase):
    object_list = []

    def setUp(self):
        # contains 50 records
        self.object_list = [i for i in range(1, 51)]

    def test_default_config(self):
        paginator = Paginator(self.object_list);
        self.assertEqual(paginator.per_page, settings.PAGINATOR_PER_PAGE)
        self.assertEqual(paginator.max_page_nav,
                         settings.PAGINATOR_MAX_PAGE_NAV)
        self.assertEqual(paginator.max_jumper,
                         settings.PAGINATOR_MAX_JUMPER)
        self.assertEqual(paginator.raise_404_on_invalid_page,
                         settings.PAGINATOR_RAISE_404_ON_INVALID_PAGE)

    def test_custom_config(self):
        paginator = Paginator(self.object_list,
                              per_page=20,
                              max_page_nav=6,
                              max_jumper=1,
                              raise_404_on_invalid_page=True);
        self.assertEqual(paginator.per_page, 20)
        self.assertEqual(paginator.max_page_nav, 6)
        self.assertEqual(paginator.max_jumper, 1)
        self.assertEqual(paginator.raise_404_on_invalid_page, True)


    def test_delta_odd(self):
        paginator = Paginator(self.object_list, max_page_nav=5)

        delta_left, delta_right = paginator._get_delta()
        self.assertEqual(delta_left, 2)
        self.assertEqual(delta_right, 2)

    def test_delta_even(self):
        paginator = Paginator(self.object_list, max_page_nav=10)

        delta_left, delta_right = paginator._get_delta()
        self.assertEqual(delta_left, 4)
        self.assertEqual(delta_right, 5)


    def test_is_paginated(self):
        paginator = Paginator(self.object_list, per_page=10)
        self.assertEqual(paginator.is_paginated, True)

        paginator = Paginator(self.object_list, per_page=100)
        self.assertEqual(paginator.is_paginated, False)


    def test_main_page_numbers_exactly(self):
        paginator = Paginator(self.object_list,
                              per_page=10,
                              max_page_nav=5)

        self.assertEqual(paginator.num_pages, 5)
        self.assertEqual(paginator._get_main_page_numbers(1), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(2), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(3), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(4), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(5), [1, 2, 3, 4, 5])

    def test_main_page_numbers_short(self):
        paginator = Paginator(self.object_list,
                              per_page=20,
                              max_page_nav=5)

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(paginator._get_main_page_numbers(1), [1, 2, 3])
        self.assertEqual(paginator._get_main_page_numbers(2), [1, 2, 3])
        self.assertEqual(paginator._get_main_page_numbers(3), [1, 2, 3])

    def test_main_page_numbers_long(self):
        paginator = Paginator(self.object_list,
                              per_page=7,
                              max_page_nav=5)

        self.assertEqual(paginator.num_pages, 8)
        self.assertEqual(paginator._get_main_page_numbers(1), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(2), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(3), [1, 2, 3, 4, 5])
        self.assertEqual(paginator._get_main_page_numbers(4), [2, 3, 4, 5, 6])
        self.assertEqual(paginator._get_main_page_numbers(5), [3, 4, 5, 6, 7])
        self.assertEqual(paginator._get_main_page_numbers(6), [4, 5, 6, 7, 8])
        self.assertEqual(paginator._get_main_page_numbers(7), [4, 5, 6, 7, 8])
        self.assertEqual(paginator._get_main_page_numbers(8), [4, 5, 6, 7, 8])
        
    def test_left_jumper(self):
        paginator = Paginator(self.object_list,
                              per_page=4,
                              max_page_nav=5,
                              max_jumper=2)

        self.assertEqual(paginator.num_pages, 13)
        self.assertEqual(paginator._get_left_jumpers(1), [])
        self.assertEqual(paginator._get_left_jumpers(2), [1])
        self.assertEqual(paginator._get_left_jumpers(3), [1, 2])
        self.assertEqual(paginator._get_left_jumpers(4), [1, None, 3])
        self.assertEqual(paginator._get_left_jumpers(5), [1, 3, None])
        self.assertEqual(paginator._get_left_jumpers(6), [1, 4, None])
        self.assertEqual(paginator._get_left_jumpers(7), [1, 4, None])
        self.assertEqual(paginator._get_left_jumpers(8), [1, 5, None])
        self.assertEqual(paginator._get_left_jumpers(9), [1, 5, None])
        self.assertEqual(paginator._get_left_jumpers(10), [1, 6, None])
        self.assertEqual(paginator._get_left_jumpers(11), [1, 6, None])
        self.assertEqual(paginator._get_left_jumpers(12), [1, 7, None])
        self.assertEqual(paginator._get_left_jumpers(13), [1, 7, None])

    def test_right_jumper(self):
        paginator = Paginator(self.object_list,
                              per_page=4,
                              max_page_nav=5,
                              max_jumper=2)

        self.assertEqual(paginator.num_pages, 13)
        self.assertEqual(paginator._get_right_jumpers(1), [None, 7, 13])
        self.assertEqual(paginator._get_right_jumpers(2), [None, 7, 13])
        self.assertEqual(paginator._get_right_jumpers(3), [None, 8, 13])
        self.assertEqual(paginator._get_right_jumpers(4), [None, 8, 13])
        self.assertEqual(paginator._get_right_jumpers(5), [None, 9, 13])
        self.assertEqual(paginator._get_right_jumpers(6), [None, 9, 13])
        self.assertEqual(paginator._get_right_jumpers(7), [None, 10, 13])
        self.assertEqual(paginator._get_right_jumpers(8), [None, 10, 13])
        self.assertEqual(paginator._get_right_jumpers(9), [None, 11, 13])
        self.assertEqual(paginator._get_right_jumpers(10), [11, None, 13])
        self.assertEqual(paginator._get_right_jumpers(11), [12, 13])
        self.assertEqual(paginator._get_right_jumpers(12), [13])
        self.assertEqual(paginator._get_right_jumpers(13), [])

