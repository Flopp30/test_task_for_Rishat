from django.db import models


class CustomBaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, editable=False)
    deleted = models.BooleanField(verbose_name='Deleted?', default=False)

    class Meta:
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()


class Item(CustomBaseModel):
    name = models.CharField(verbose_name='item name', max_length=150)
    description = models.TextField(verbose_name='description')
    price = models.IntegerField(verbose_name='price', default=0)  # cents

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price / 100}'
