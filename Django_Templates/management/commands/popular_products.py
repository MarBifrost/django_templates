from django.core.management.base import BaseCommand
from order.models import CartItem
from django.db.models import Count

class Command(BaseCommand):
    help = "Find the three most popular product which are added to carts"

    def handle(self, *args, **options):
        most_popular_items = (
            CartItem.objects.values(
                'product_id', 'product_name'
            ).annotate(count=Count('product_id')).order_by('-count')[:3]
        )

        if most_popular_items:
            self.stdout.write("The most popular products are:")
            for item in most_popular_items:
                self.stdout.write(f"{item['product_name']}")

            else:
                self.stdout.write("There are no products")