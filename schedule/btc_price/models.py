from locale import currency
from django.db import models

class BitcoinCalculactor(models.Model):
    currency = models.CharField(max_length=50)
    rate = models.FloatField("rate")
    
    def __str__(self) -> str:
        return f"{self.currency} = {self.rate}"

    # BitcoinCalculactor().get_price_by_curr()
    @classmethod
    def get_price_by_curr(cls, curr):
        rate = BitcoinCalculactor.objects.get(currency = curr)
        return getattr(rate,'rate')
    
    @classmethod
    def get_bit_sum(cls, curr, amount):

        rate = BitcoinCalculactor.objects.get(currency = curr) 
        rate = getattr(rate,'rate')
        result = rate * float(amount)
        return result
        
    @classmethod
    def get_btc(self,curr,money):
        rate = BitcoinCalculactor.objects.get(currency = curr) 
        rate = getattr(rate,'rate')
        result = float(money) / rate
        return result

