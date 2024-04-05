from django.db import models
from slugify import slugify
from django.core.exceptions import ValidationError

# Create your models here.
class MarketAreaCluster(models.Model):
    """
        MarketAreaCluster - This model will contain the area | store | brand location Information it will help all stores | brand to club with each other
    """
    title= models.CharField(max_length=200,help_text="Area | Market | Cluster Name/Title ")
    slug = models.SlugField(editable=False,unique=True,blank=True)
    location = models.CharField(max_length=100,help_text="Location Or Area Name in Text")
    # Internal Purpose Only
    location_co_ordinates = models.CharField(max_length=100,help_text="Only Internal Purpose",blank=True, null=True) #for now blank null is true later with geolocation it will be disabled

    def get_market_area_name(self):
        return self.title

    def __str__(self) -> str:
        return self.title
    
    def clean(self):
        """
            Clean - Convert title into slug with slug_candidate(slugify)
        """
        if not self.pk:
            slug_candidate = slugify(self.title, replacements=[['|', 'or'], ['%', 'percent'],['+', 'plus'], ['*', 'star'],['^', 'power'], ['!','ex'], ['$', 'dollar'],['#', 'hash'],['@', 'at']], allow_unicode=True)
            if MarketAreaCluster.objects.filter(slug=slug_candidate).exists():
                raise ValidationError("Market/ Area/ Cluster Name/Type Already Exists")
            else:
                self.slug = slug_candidate

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Area | Market | Cluster Details/Location"
        verbose_name_plural = "Area | Market | Cluster Details/Locations"

class MenuCategory(models.Model):
    """
        Menu Category - This Model will contain the Menu Items Categories which Brands will serve.
    """
    title= models.CharField(max_length=200,help_text="Category's Name/Title ")
    slug = models.SlugField(editable=False,unique=True,blank=True)

    def get_menu_category_name(self):
        return self.title

    def __str__(self) -> str:
        return self.title

    def clean(self):
        """
            Clean - Convert title into slug with slug_candidate(slugify)
        """
        if not self.pk:
            slug_candidate = slugify(self.title, replacements=[['|', 'or'], ['%', 'percent'],['+', 'plus'], ['*', 'star'],['^', 'power'], ['!','ex'], ['$', 'dollar'],['#', 'hash'],['@', 'at']], allow_unicode=True)
            if MenuCategory.objects.filter(slug=slug_candidate).exists():
                raise ValidationError("Category Name/Type Already Exists")
            else:
                self.slug = slug_candidate

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Menu Category's"
        verbose_name_plural = "Menu Category's"

class Brand(models.Model):
    """
        Brand - This Model will contain the Brand | Shop Information which will get onboard with Food Verse
    """
    # Link with Market | Area | Cluster
    market_area_cluster = models.ForeignKey(MarketAreaCluster,on_delete=models.DO_NOTHING)
    # Choices for Fields
    brand_serving_option_choices = (('SELF-PICKUP','SELF SERVICE'),('ON-TABLE','TABLE SERVING'),('BOTH-OPTIONS','BOTH'))
    title = models.CharField(max_length=200,help_text="Enter Brands | Shop Name ")
    license_number = models.CharField(max_length=50,help_text="Enter the FSSAI License Number")
    gstin = models.CharField(max_length=50,help_text="Enter the Registered GST Number",null=True,blank=True)
    location = models.CharField(max_length=100,help_text="Location Or Area Name in Text")
    serving_options = models.CharField(max_length=20,choices=brand_serving_option_choices)
    # logo = skipping logo not yet configured media lib location
    # Flags | Optional Configuration
    opening_time = models.TimeField(blank=True, null=True,help_text="Time to get Brand | Store Online")    
    closing_time = models.TimeField(blank=True, null=True,help_text="Time to get Brand | Store Offline")
    cooking_time = models.CharField(max_length=10,blank=True, null=True,help_text="Approx Time under which Food will be Prepared (Preparation Time)")

    def get_brands_name(self):
        return self.title

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Brands | Shop Details"
        verbose_name_plural = "Brands | Shop Details"

class BrandMenu(models.Model):
    """
        Brand Menu - This Model will contain the Brand | Shop Menu Information which they will serve on Food Verse
    """
    # Link with Brand
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    # Choices for Fields
    menu_item_type_choices = (('VEG','VEG'),('NON-VEG','NON-VEG'))
    menu_item_availability_choices = (('IN-STOCK','IN-STOCK'),('OUT-OF-STOCK','OUT-OF-STOCK'))
    menu_item_bulk_order_choices = (('IN-STOCK','IN-STOCK'),('OUT-OF-STOCK','OUT-OF-STOCK'))
    # Menu Fields
    item_name = models.CharField(max_length=100)
    item_category = models.ForeignKey(MenuCategory,on_delete=models.DO_NOTHING)
    item_type = models.CharField(max_length=50,choices=menu_item_type_choices)
    item_available = models.CharField(max_length=20,choices=menu_item_availability_choices,default="IN-STOCK")
    item_selling_price = models.FloatField()
    item_discounted_price = models.FloatField(blank=True, null=True)
    # Flags | Optional Configuration
    item_promotion_value = models.IntegerField(blank=True, null=True,help_text="Ordering of Promotion Item")
    item_order_limit = models.IntegerField(blank=True, null=True,help_text="Max number of Order Place in single Checkout")
    item_bulk_order = models.CharField(max_length=20,choices=menu_item_bulk_order_choices,blank=True, null=True,help_text="Product/Item could be Builk Ordered Or Not")
    item_bulk_order_limit = models.IntegerField(blank=True, null=True,help_text="Lower Limit after which Price is Applicable")
    item_bulk_order_price = models.IntegerField(blank=True, null=True,help_text="Bulk order Discounted Price")
    
    class Meta:
        verbose_name = "Brand Menu Item"
        verbose_name_plural = "Brand Menu Item's"
