from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)
    categoryDesc = models.CharField(max_length= 300, null=True, blank=True)

    def __str__(self):
        return self.categoryName

    @staticmethod
    def is_duplicate(category_name):
        try:
            return Category.objects.get(categoryName = category_name)
        except:
            return False
    
    @staticmethod
    def get_category():
        try:
            return Category.objects.all()
        except:
            return False

    @staticmethod
    def get_category_by_name(name):
        try:
            return Category.objects.get(categoryName = name)
        except:
            return False