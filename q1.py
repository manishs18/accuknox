import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Simple model for demonstration
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that introduces a delay
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5)  # Introduce a delay of 5 seconds
    print("Signal handler finished!")

# Create an instance of MyModel to trigger the signal
def create_model_instance():
    print("Creating model instance...")
    instance = MyModel.objects.create(name="Test")
    print("Model instance created!")

# Code to test synchronous behavior
if __name__ == "__main__":
    create_model_instance()
    print("This will print after the signal handler finishes.")
