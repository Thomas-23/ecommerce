from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        abstract = True


class MetaDescriptionModel(models.Model):

    meta_keywords = models.CharField(
        _("meta keywords"),
        max_length=255,
        help_text=_('Comma-delimited set of SEO keywords for meta tag')
    )

    meta_description = models.CharField(
        _("meta description"),
        max_length=255,
        help_text=_('Content for description meta tag')
    )

    description = models.TextField(_('description'), max_length=500)

    class Meta:
        abstract = True


class Category(TimeStampedModel, MetaDescriptionModel):

    is_active = models.BooleanField(_('is active'), default=True)
    name = models.CharField(_('name'), max_length=50, unique=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(TimeStampedModel, MetaDescriptionModel):
    is_active = models.BooleanField(_('is active'), default=True)
    name = models.CharField(_('name'), max_length=50, unique=True)
    brand = models.CharField(_('brand'), max_length=50)
    sku = models.CharField(_('product sku'), max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.CharField(max_length=50)
    is_best_seller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(_('product quantity'))
    categories = models.ManyToManyField(Category, verbose_name=_('product in categories'))

    class Meta:
        db_table = 'products'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


