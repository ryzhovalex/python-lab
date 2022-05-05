#!/usr/bin/env python
"""Paginator

Splits input string into pages.
"""


__author__ = "D4rkof"
__version__ = "1.0.0"
__email__ = "thed4rkof@gmail.com"
__status__ = "Production"


import math


class Pagination:

	def __init__(self, items = [], page_size = 10):

		self.items = items
		self.page_size = page_size
		self.pages_number = math.ceil(len(self.items) / self.page_size)
		self.pages_content = {}
		self.current_page = 1

		page = 1
		counter = 1

		while page <= self.pages_number:
			page_content = []

			while counter <= self.page_size * page:
				try:
					page_content.append(self.items[counter - 1])

				except:
					break

				else:
					counter += 1

			self.pages_content[page] = page_content

			page += 1	


	def get_visible_items(self):

		print(self.pages_content[self.current_page])
		return self

	def prev_page(self):

		if self.current_page - 1 > 0:
			self.current_page -= 1
		else:
			self.current_page = 1

		return self


	def next_page(self):

		if self.current_page + 1 <= self.pages_number:
			self.current_page += 1
		else:
			self.current_page = self.pages_number

		return self


	def first_page(self):

		self.current_page = 1
		return self


	def last_page(self):

		self.current_page = self.pages_number
		return self


	def go_to_page(self, number):

		if number < 1:
			number = 1

		elif number > self.pages_number:
			number = self.pages_number

		self.current_page = number

		return self


	def get_current_page(self):
		return self.current_page


	def get_page_size(self):
		return self.page_size


	def get_items(self):
		return self.items
	

if __name__ == "__main__":
	p = Pagination([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
	p.get_visible_items()

		