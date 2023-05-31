#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Items import Bag


class bookshelf:
    # List of items
    item_list = []

    def __init__(self):
        pass

    def setup_bookshelf(self):

        map = Bag("cape", "flotador")
        torch = Bag("sword", "lighter")

        # self.items.append(key)
        self.item_list.append(map)
        self.item_list.append(torch)

    def get_item_list(self):
        return self.item_list

    def get_item(self, name):
        return next((item for item in self.items if item.name == name), "This item doesn't exist")

