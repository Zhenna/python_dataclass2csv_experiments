# %%
from datetime import datetime
from python_class import write2csv
from python_dataclass import dataclass2csv
from pydantic_dataclass import pydantic_dataclass2csv

# %%
write2csv(
    item = "book1",
    purchase_date = datetime(2022, 7, 25),
    quantity = 3,
    total_price = 321
    ).save_csv(
        newfile=True
    )
# %%
write2csv(
    item = "book2",
    purchase_date = datetime(2019, 9, 10),
    quantity = 2,
    total_price = 214
    ).save_csv()
# %%
write2csv(
    item = "book3",
    purchase_date = datetime(2024, 2, 20),
    quantity = 3,
    total_price = 327
    ).save_csv()
 # %%
write2csv(
    item = "book4",
    purchase_date = datetime(2023, 12, 2),
    quantity = 3,
    total_price = 324
    ).save_csv()
 # %%
write2csv(
    item = "book_error",
    purchase_date = datetime(2023, 12, 2),
    quantity = 3,
    total_price = 324
    ).save_csv()

# %%

dataclass2csv(
    item = "item1",
    purchase_date = datetime(2022, 8, 5),
    quantity = 10,
    total_price = 85.6
    ).save_csv(
        newfile=True
)
# %%

dataclass2csv(
    item = 6, # int instead of str
    purchase_date = datetime(2022, 8, 5),
    quantity = 10,
    total_price = 85.6
    ).save_csv()

# %%
pydantic_dataclass2csv(
    item = "product1",
    purchase_date = datetime(2023, 2, 15),
    quantity = 10,
    total_price = 64.8
    ).save_csv(
        newfile=True
)
# %%
pydantic_dataclass2csv(
    item = 7, # should be str type
    purchase_date = datetime(2023, 2, 15),
    quantity = 10,
    total_price = 64.8
    ).save_csv()
# %%
pydantic_dataclass2csv(
    item = "product_wrong_date",
    purchase_date = datetime(2024, 2, 15),
    quantity = 10,
    total_price = 64.8
    ).save_csv()
# %%
