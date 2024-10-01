import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Simple model for demonstration
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that checks the thread ID
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler is running in thread: {threading.get_ident()}")

# Create an instance of MyModel to trigger the signal
def create_model_instance():
    print(f"Model creation is running in thread: {threading.get_ident()}")
    instance = MyModel.objects.create(name="Test")

# Code to test thread behavior
if __name__ == "__main__":
    create_model_instance()
