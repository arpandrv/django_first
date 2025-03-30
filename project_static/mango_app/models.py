from django.db import models

class MangoItem(models.Model):
    """Data model representing a pest or disease affecting mangoes"""
    ITEM_TYPES = (
        ('pest', 'Pest'),
        ('disease', 'Disease'),
    )
    
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    image_path = models.CharField(max_length=255)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    detailed_info = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.get_item_type_display()})"
    
    def get_absolute_url(self):
        return f"/projects/{self.id}/"