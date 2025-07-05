import random
import string
from django.utils.text import slugify 

class generate_ids:

    def gen_table_id(self):
        table_id = f"Table-{"".join(random.choice(string.digits) for _ in range(5))}"
        return slugify(table_id)
    
    def gen_category_id(self):
        category = f"Category-{"".join(random.choice(string.digits) for _ in range(3))}"
        return slugify(category)
    
    def gen_menu_item_id(self):
        item = f"Item-{"".join(random.choice(string.digits) for _ in range(6))}"
        return slugify(item)