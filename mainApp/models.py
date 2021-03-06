from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from datetime import datetime

class MainLogo(models.Model):
    logo_img = models.ImageField(upload_to="logos/")

    def __str__(self):
        return str(self.id)
    



class RoleModel(models.Model):
    role_title = models.CharField(max_length=120)

    def __str__(self):
        return self.role_title


class LandingSlider(models.Model):
    slider_img = models.ImageField(upload_to="images/")

    def __str__(self):

        return str(self.id)

class SecondarySlider(models.Model):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)


class Country(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


class City(models.Model):
    city_name = models.CharField(max_length=120)

    def __str__(self):
        return self.city_name


class SellerAccount(models.Model):
    joined_at = models.DateField(default=datetime.now, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(null=True, unique=True)
    contact_no = models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to="images/", null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(default=0, blank=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profile_complete = models.BooleanField(default=False, null=True)
    

    def __str__(self):
        return str(self.user)

class WithDrawPaymentMethod(models.Model):
    method_name = models.CharField(max_length=220, unique=True)


    def __str__(self):
        return self.method_name


class WithDrawModel(models.Model):
    withdraw_date = models.DateTimeField(default=datetime.now)
    method = models.ForeignKey(WithDrawPaymentMethod, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    on_review = models.BooleanField(default=True, null=True)
    is_approved = models.BooleanField(default=False, null=True)


    def __str__(self):
        return str(self.user)


class DummyUser(models.Model):
    user = models.CharField(max_length=120, default=None)

    def __str__(self):
        return self.user


class Services(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, unique=True)
    sub_title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

# Subcategory Model 
class Subcategory(models.Model):
    slug = models.SlugField(unique=True)
    sub_title = models.CharField(max_length=120, unique=True)
    sub_img = models.ImageField(upload_to="images/", null=True, blank=True)
    # is_iterested = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.sub_title

# Category model
class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, unique=True)
    icon = models.FileField(upload_to="images/", validators=[
                            FileExtensionValidator(['svg', 'png', 'jpg'])], null=True)
    subcategory = models.ManyToManyField(Subcategory, blank=True)

    def __str__(self):
        return self.title

# Child Subcategory Model
class ChildSubcategory(models.Model):
    child_slug = models.SlugField()
    child_title = models.CharField(max_length=220)
    child_image = models.ImageField(upload_to="images/", null=True, blank=True)
    parent_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.child_title



class CategoryInterestedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_interested = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.user)




class Tag(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class DeliveryTime(models.Model):
    title = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.title

class Revision(models.Model):
    title = models.CharField(max_length=120, null=True, unique=True)

    def __str__(self):
        return self.title

class NumberOfPage(models.Model):
    title = models.CharField(max_length=120, unique=True, null=True)

    def __str__(self):
        return self.title

class NumberOfPlugins(models.Model):
    title = models.CharField(max_length=120, null=True)
    
    def __str__(self):
        return str(self.id)

class FileFormats(models.Model):
    format_title = models.CharField(max_length=120)
    
    
    def __str__(self):
        return str(self.id)



class Package(models.Model):
    
    management_duration_choices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15")
    )
    
    title = models.CharField(max_length=120)
    delivery_time = models.ForeignKey(
        DeliveryTime, on_delete=models.CASCADE, null=True)
    package_desc = models.TextField(null=True)
    revision_basic = models.ForeignKey(Revision, on_delete=models.SET_NULL, null=True, blank=True, related_name="revision_basic")
    revision_standard = models.ForeignKey(Revision, on_delete=models.SET_NULL, null=True, blank=True, related_name="revision_standard")
    revision_premium = models.ForeignKey(Revision, on_delete=models.SET_NULL, null=True, blank=True, related_name="revision_premium")
    num_of_pages_for_basic = models.ForeignKey(NumberOfPage, on_delete=models.SET_NULL, null=True, related_name="num_of_pages_for_basic", blank=True)
    num_of_pages_for_standard = models.ForeignKey(NumberOfPage, on_delete=models.SET_NULL, null=True, related_name="num_of_pages_for_standard", blank=True)
    num_of_pages_for_premium = models.ForeignKey(NumberOfPage, on_delete=models.SET_NULL, null=True, related_name="num_of_pages_for_premium", blank=True)
    is_responsive_basic = models.BooleanField(default=False, null=True, blank=True)
    is_responsive_standard = models.BooleanField(default=False, null=True, blank=True)
    is_responsive_premium = models.BooleanField(default=False, null=True, blank=True)
    setup_payment = models.BooleanField(default=False, null=True, blank=True)
    will_deploy = models.BooleanField(default=False, null=True, blank=True)
    is_compitable = models.BooleanField(default=False, null=True, blank=True)
    supported_formats = models.ManyToManyField(FileFormats, blank=True)
    # For Logo Design
    provide_vector = models.BooleanField(default=False, null=True, blank=True)
    is_3dmockup = models.BooleanField(default=False, null=True, blank=True)
    is_high_res_for_basic = models.BooleanField(default=False, null=True, blank=True)
    is_high_res_for_standard = models.BooleanField(default=False, null=True, blank=True)
    is_high_res_for_premium = models.BooleanField(default=False, null=True, blank=True)
    will_sourcefile_for_basic = models.BooleanField(default=False, null=True, blank=True)
    will_sourcefile_for_standard = models.BooleanField(default=False, null=True, blank=True)
    will_sourcefile_for_premium = models.BooleanField(default=False, null=True, blank=True)
    # For Digital Marketing
    is_campaign_optimization = models.BooleanField(default=False, null=True, blank=True)
    management_duration = models.CharField(max_length=120, choices=management_duration_choices, null=True, blank=True)
    
    # For Video editor
    
    video_length = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    will_embedded_sub = models.BooleanField(default=False, null=True, blank=True)
    is_transactioable = models.BooleanField(default=False, null=True, blank=True)
    is_translated = models.BooleanField(default=False, null=True, blank=True)
    will_srt_logo = models.BooleanField(default=False, null=True, blank=True)
    will_add_logo = models.BooleanField(default=False, null=True, blank=True)
    
    # For Data Entry
    
    provide_pdf = models.BooleanField(null=True, default=False, blank=True)
    max_data = models.CharField(max_length=450, null=True, blank=True)
    provide_excel = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class ExtraImage(models.Model):
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return str(self.image)


class Offer(models.Model):
    Offer_STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("PENDING APPROVAL", "PENDING APPROVAL"),
        ("REQUIRED MODIFICATION", "REQUIRED MODIFICATION"),
        ("DENIED", "DENIED"),
        ("PAUSED", "PAUSED"),
    )

    slug = models.SlugField(unique=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    offer_title = models.CharField(max_length=240)
    seo_title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/')
    extra_images = models.ManyToManyField(ExtraImage)
    offer_video = models.FileField(upload_to="images/", blank=True, null=True)
    document = models.FileField(upload_to="files/", null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    packages = models.ManyToManyField(Package, through='OfferManager')
    description = models.TextField()
    # offer_rating = models.FloatField(default=0)
    is_popular = models.BooleanField(default=False, null=True)
    pop_web = models.BooleanField(default=False, null=True, blank=True)
    is_pro = models.BooleanField(default=False, null=True)
    click = models.PositiveIntegerField(null=True, blank=True, default=0)
    impressions = models.PositiveIntegerField(default=0, null=True, blank=True)
    order_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    cancellation = models.PositiveIntegerField(default=0, null=True, blank=True)
    offer_status = models.CharField(max_length=200, null=True, choices=Offer_STATUS, default="ACTIVE")
    # is_favorite = models.BooleanField(null=True, default=False, blank=True)
    # is_complete = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.slug



class OfferFavoriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    is_Favorite = models.BooleanField(default=False)




class OfferManager(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_price(self):
        return self.price

    @staticmethod
    def get_offer(ids):
        return OfferManager.objects.filter(id__in=ids)


class Currency(models.Model):
    currency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.currency_name


class Rating(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class ReviewSeller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    rate_seller = models.ForeignKey(
        Rating, on_delete=models.CASCADE, null=True)


class Checkout(models.Model):
    ORDER_CHOICES = (
        ("ACTIVE", "ACTIVE"),
        ("LATE", "LATE"),
        ("COMPLETED", "COMPLETED"),
        ("DELIVERED", "DELIVERED"),
        ("CANCELLED", "CANCELLED"),
        ("ON REVIEW", "ON REVIEW")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='seller')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.TextField(null=True)
    package = models.ForeignKey(OfferManager, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    grand_total = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00, null=True)
    paid = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    order_status = models.CharField(max_length=200, choices=ORDER_CHOICES, default="ACTIVE")
    is_complete = models.BooleanField(default=False, null=True)
    is_cancel = models.BooleanField(default=False, null=True)
    on_review = models.BooleanField(default=False, null=True)
    
    def save(self, *args, **kwargs):
        self.total = self.price*self.quantity
        service_fee = self.total * 25 / 100
        self.grand_total = self.total + service_fee
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_total(total):
        return Checkout.objects.filter(total=total)

    @staticmethod
    def get_all_orders(self):
        return Checkout.objects.all()

    @staticmethod
    def placeOrder(self):
        return self.save()

    @staticmethod
    def get_orders_by_users(user):
        return Checkout.objects.filter(user=user['id'])


class SellerSubmit(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name="checkout")
    file_field = models.FileField(upload_to="files/", null=True)
    submit_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    


class PromoCode(models.Model):
    promo_title = models.CharField(max_length=120)
    code = models.CharField(max_length=90)
    discount_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.promo_title


class BuyerPostRequest(models.Model):
    POST_STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("RESERVED", "RESERVED"),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    postrequest_title = models.CharField(max_length=220, unique=True, null=True)
    description = models.TextField(null=True)
    attachment = models.FileField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE)
    budget = models.IntegerField()
    post_status = models.CharField(max_length=100, null=True, choices=POST_STATUS, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.postrequest_title


class SendOfferModel(models.Model):
    send_offer_slug = models.SlugField(max_length=200, null=True, unique=True)
    buyer_post_request = models.ForeignKey(BuyerPostRequest, on_delete=models.CASCADE, related_name="buyer_post_request", null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_offer_buyer", null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_offer_seller", null=True)
    offer_letter = models.TextField(null=True)
    offered_price = models.PositiveIntegerField(null=True)
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE, related_name="send_offer_delivery_time", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.send_offer_slug


class ReviewSellerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_seller")
    star = models.IntegerField(default=0)
    review_ield = models.TextField()


    def __str__(self):
        return str(self.id)