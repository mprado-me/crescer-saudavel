from unittest import TestCase
from ..paginator import PaginatorDataProvider

class TestPaginatorDataProvider(TestCase):
    def test_get_pages_n_pages_1_total_9(self):
        self.assertEqual(PaginatorDataProvider().get_pages_number(1, 1, 9), [1])
        self.assertEqual(PaginatorDataProvider().get_pages_number(2, 1, 9), [2])
        self.assertEqual(PaginatorDataProvider().get_pages_number(3, 1, 9), [3])
        self.assertEqual(PaginatorDataProvider().get_pages_number(4, 1, 9), [4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(5, 1, 9), [5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(6, 1, 9), [6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(7, 1, 9), [7])
        self.assertEqual(PaginatorDataProvider().get_pages_number(8, 1, 9), [8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(9, 1, 9), [9])

    def test_get_pages_n_pages_2_total_9(self):
        self.assertEqual(PaginatorDataProvider().get_pages_number(1, 2, 9), [1, 2])
        self.assertEqual(PaginatorDataProvider().get_pages_number(2, 2, 9), [1, 2])
        self.assertEqual(PaginatorDataProvider().get_pages_number(3, 2, 9), [3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(4, 2, 9), [3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(5, 2, 9), [5, 6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(6, 2, 9), [5, 6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(7, 2, 9), [7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(8, 2, 9), [7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(9, 2, 9), [8, 9])


    def test_get_pages_n_pages_3_total_9(self):
        self.assertEqual(PaginatorDataProvider().get_pages_number(1, 3, 9), [1, 2, 3])
        self.assertEqual(PaginatorDataProvider().get_pages_number(2, 3, 9), [1, 2, 3])
        self.assertEqual(PaginatorDataProvider().get_pages_number(3, 3, 9), [1, 2, 3])
        self.assertEqual(PaginatorDataProvider().get_pages_number(4, 3, 9), [4, 5, 6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(5, 3, 9), [4, 5, 6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(6, 3, 9), [4, 5, 6])
        self.assertEqual(PaginatorDataProvider().get_pages_number(7, 3, 9), [7, 8, 9])
        self.assertEqual(PaginatorDataProvider().get_pages_number(8, 3, 9), [7, 8, 9])
        self.assertEqual(PaginatorDataProvider().get_pages_number(9, 3, 9), [7, 8, 9])

    def test_get_pages_n_pages_4_total_9(self):
        self.assertEqual(PaginatorDataProvider().get_pages_number(1, 4, 9), [1, 2, 3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(2, 4, 9), [1, 2, 3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(3, 4, 9), [1, 2, 3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(4, 4, 9), [1, 2, 3, 4])
        self.assertEqual(PaginatorDataProvider().get_pages_number(5, 4, 9), [5, 6, 7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(6, 4, 9), [5, 6, 7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(7, 4, 9), [5, 6, 7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(8, 4, 9), [5, 6, 7, 8])
        self.assertEqual(PaginatorDataProvider().get_pages_number(9, 4, 9), [6, 7, 8, 9])

    def test_get_pages_n_pages_5_total_9(self):
        self.assertEqual(PaginatorDataProvider().get_pages_number(1, 5, 9), [1, 2, 3, 4, 5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(2, 5, 9), [1, 2, 3, 4, 5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(3, 5, 9), [1, 2, 3, 4, 5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(4, 5, 9), [1, 2, 3, 4, 5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(5, 5, 9), [1, 2, 3, 4, 5])
        self.assertEqual(PaginatorDataProvider().get_pages_number(6, 5, 9), [5, 6, 7, 8, 9])
        self.assertEqual(PaginatorDataProvider().get_pages_number(7, 5, 9), [5, 6, 7, 8, 9])
        self.assertEqual(PaginatorDataProvider().get_pages_number(8, 5, 9), [5, 6, 7, 8, 9])
        self.assertEqual(PaginatorDataProvider().get_pages_number(9, 5, 9), [5, 6, 7, 8, 9])


