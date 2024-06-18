from django.core.management.base import BaseCommand
from faker import Faker
from ...models import TFTs, GamingPC, GraphicsCard, Laptops, Accessories, ComputerParts
import requests
import random

fake = Faker('en_US')

class Command(BaseCommand):
    help = 'Generates random items for TFT Screens, Gaming PCs, Graphics Cards, Laptops, Computer Accessories, and Computer Parts and saves them to the database'

    # Replace 'YOUR_UNSPLASH_ACCESS_KEY' with your actual Unsplash Access Key
    unsplash_access_key = 'FoB2biN0VKz0FLzIo5Ae3bE9fz_KDVmRj4TQ9fzBujc'

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating New Items...")

        # Generate TFT items
        self.generate_items(TFTs, 10)

        # Generate Gaming PCs
        self.generate_items(GamingPC, 10)

        # Generate Graphics Cards
        self.generate_items(GraphicsCard, 10)

        # Generate Laptops
        self.generate_items(Laptops, 10)

        # Generate Computer Accessories
        self.generate_items(Accessories, 10)

        # Generate Computer Parts
        self.generate_items(ComputerParts, 5)

        self.stdout.write(self.style.SUCCESS("Random items generated successfully"))

    def generate_items(self, model_class, count):
        for _ in range(count):
            image_url = self.get_random_unsplash_image_url()
            item = model_class(
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                description=fake.sentence(nb_words=6, variable_nb_words=True),
                price=fake.random_int(min=100, max=10000),
                image_url=image_url,
                stock=random.choice([True, False])  # Randomly set stock status
            )
            item.save()
            self.stdout.write(self.style.SUCCESS(f"Created {model_class.__name__} item: {item.name}"))

    def get_random_unsplash_image_url(self):
        url = f"https://api.unsplash.com/photos/random/?client_id={self.unsplash_access_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['urls']['regular']
        else:
            # Fallback to placeholder URL if Unsplash API request fails
            return f"https://via.placeholder.com/{random.randint(200, 600)}x{random.randint(200, 600)}"   