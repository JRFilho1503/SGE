from decimal import Decimal

from django.test import TestCase

from brands.models import Brand
from categories.models import Category
from products.models import Product
from outflows.models import Outflow


class OutflowStockTestCase(TestCase):
    """Regra de negócio: uma saída (outflow) debita o estoque do produto (signal post_save)."""

    def setUp(self):
        brand = Brand.objects.create(name="Marca")
        category = Category.objects.create(name="Categoria")
        self.product = Product.objects.create(
            title="Produto X", brand=brand, category=category,
            cost_price=Decimal("10.00"), selling_price=Decimal("20.00"), quantity=10,
        )

    def test_saida_debita_o_estoque(self):
        Outflow.objects.create(product=self.product, quantity=3)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 7)

    def test_saidas_sucessivas_acumulam_o_debito(self):
        Outflow.objects.create(product=self.product, quantity=3)
        Outflow.objects.create(product=self.product, quantity=2)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 5)

    def test_saida_quantidade_zero_nao_altera_estoque(self):
        Outflow.objects.create(product=self.product, quantity=0)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 10)
