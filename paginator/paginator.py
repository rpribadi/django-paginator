import math

from django.conf import settings
from django.core.paginator import Paginator as Pgtr, Page, PageNotAnInteger, EmptyPage

from . import settings as app_settings

DEFAULT_PER_PAGE = getattr(
    settings,
    'PAGINATOR_PER_PAGE',
    app_settings.PAGINATOR_PER_PAGE)

DEFAULT_MAX_PAGE_NAV = getattr(
    settings,
    'PAGINATOR_MAX_PAGE_NAV',
    app_settings.PAGINATOR_MAX_PAGE_NAV)

DEFAULT_MAX_JUMPER = getattr(
    settings,
    'PAGINATOR_MAX_JUMPER',
    app_settings.PAGINATOR_MAX_JUMPER)

DEFAULT_RAISE_404_ON_INVALID_PAGE = getattr(
    settings,
    'PAGINATOR_RAISE_404_ON_INVALID_PAGE',
    app_settings.PAGINATOR_RAISE_404_ON_INVALID_PAGE)


class Paginator(Pgtr):
    def __init__(self,
            object_list,
            per_page=DEFAULT_PER_PAGE,
            max_page_nav=DEFAULT_MAX_PAGE_NAV,
            max_jumper=DEFAULT_MAX_JUMPER,
            raise_404_on_invalid_page=DEFAULT_RAISE_404_ON_INVALID_PAGE,
            **kwargs):

        super(Paginator, self).__init__(object_list, per_page, **kwargs)
        self.max_page_nav = max_page_nav
        self.max_jumper = max_jumper
        self.raise_404_on_invalid_page = raise_404_on_invalid_page

    def _get_delta(self):
        delta_left = int((self.max_page_nav - 1 )/ 2)
        delta_right = self.max_page_nav - delta_left - 1
        return delta_left, delta_right

    def _get_main_page_numbers(self, page):
        delta_left, delta_right = self._get_delta()
        start_page = page - delta_left
        end_page = page + delta_right

        extend_left = 0
        extend_right = 0        
        if start_page < 1:
            extend_right += (1 - start_page)
        if end_page > self.num_pages:
            extend_left = end_page - self.num_pages

        if extend_right:
            start_page = 1
            end_page += extend_right
            if end_page > self.num_pages:
                end_page = self.num_pages
        if extend_left:
            end_page = self.num_pages
            start_page -= extend_left
            if start_page < 1:
                start_page = 1

        # + 1 to include end_page
        return [i for i in range(start_page, end_page + 1)]

    def _get_left_jumpers(self, start_page):
        if self.max_jumper < 1 or start_page <= 1:
            return []

        jumpers = []
        interval = int(math.ceil(float(start_page - 1) / self.max_jumper))
        minimimum_interval = 2
        interval = max(interval, minimimum_interval)
        
        page = 1        
        while page < start_page:
            jumpers.append(page)
            page += interval
            
        return jumpers

    def _get_right_jumpers(self, end_page):
        if self.max_jumper < 1 or end_page >= self.num_pages:
            return []

        jumpers = []
        interval = int(math.ceil(float(self.num_pages - end_page) / self.max_jumper))
        minimimum_interval = 2
        interval = max(interval, minimimum_interval)

        page = self.num_pages
        while page > end_page:
            jumpers.append(page)
            page -= interval
        jumpers.reverse()

        return jumpers

    def _get_page_nav(self, page):
        page_nav = []
        if self.num_pages <= self.max_page_nav:
            page_nav = [i for i in range(1, self.num_pages + 1)]
        else:
            page_nav = self._get_main_page_numbers(page)
            start_page = page_nav[0]
            end_page = page_nav[-1]
            left_jumpers = self._get_left_jumpers(start_page)
            right_jumpers = self._get_right_jumpers(end_page)
            
            if left_jumpers:
                page_nav = left_jumpers + [None] + page_nav
            if right_jumpers:
                page_nav = page_nav+ [None] + right_jumpers
        return page_nav

