from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

# Simple model for demonstration
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that tries to raise an exception
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler triggered!")
    # Check if we are inside a transaction block
    if transaction.get_connection().in_atomic_block:
        print("Inside a transaction!")
    else:
        print("Not inside a transaction!")

    # Now raise an exception to see what happens
    raise Exception("This is an error in the signal handler.")

# Create an instance of MyModel to trigger the signal
def create_model_instance():
    try:
        instance = MyModel.objects.create(name="Test")
        print("Model instance created!")
    except Exception as e:
        print(f"Error caught: {e}")

# Code to test transaction behavior
if __name__ == "__main__":
    create_model_instance()
