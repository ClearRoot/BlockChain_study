from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length = 10)
    check_price = models.FloatField(blank=True, null=True) # 확인할 금액
    complete_price = models.FloatField(blank=True, null=True) # 내가 거래한 금액
    max_price = models.FloatField(blank=True, null=True) # 최댓값 저장
    today_result = models.FloatField(blank=True, null=True)
    result_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.name