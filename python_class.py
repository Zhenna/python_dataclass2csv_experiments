from datetime import datetime
import csv


class write2csv:
    def __init__(
            self, 
            item: str, 
            purchase_date: datetime, 
            quantity: int, 
            total_price: float,
            ):
        self.item = item
        self.purchase_date = purchase_date
        self.quantity = quantity
        self.total_price = total_price

    def get_tax_rate(self) -> float:
        """return different tax rate based on year of purchase"""
        if self.purchase_date.year < 2023:
            return 0.07
        elif self.purchase_date.year >= 2022 and self.purchase_date.year < 2024:
            return 0.08
        elif self.purchase_date.year >= 2024:
            return 0.09
        
    def get_unit_price(self) -> float:
        return self.total_price/self.quantity
    
    def get_price_before_tax(self) -> float:
        tax_rate = self.get_tax_rate()
        return self.total_price/(1+tax_rate)
    
    def get_unit_price_before_tax(self) -> float:
        total_before_tax = self.get_price_before_tax()
        return total_before_tax/self.quantity
    
    def header(self) -> list[str]:
        return [
            "item",
            "date of purchase",
            "quantity",
            "total price",
            "total price before tax",
            "unit price",
            "unit price before tax"
        ]
    
    def one_row(self) -> list:
        return [
                self.item,
                self.purchase_date.date(),
                self.quantity,
                self.total_price,
                self.get_price_before_tax(),
                self.get_unit_price(),
                self.get_unit_price_before_tax()
            ]
    
    def save_csv(
            self,
            filename: str = "regular_python_class.csv",
            newfile: bool = False,
            ):
        if newfile:
            # overwrite file and add header
            with open(filename, "w") as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow(self.header())
                writer.writerow(self.one_row())
                
        else:
            # append row to existing file
            with open(filename, "a") as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow(self.one_row())