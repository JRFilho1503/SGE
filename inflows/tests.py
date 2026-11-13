from decimal import Decimal

from django.test import TestCase

from brands.models import Brand
from categories.models import Category
from products.models import Product
from suppliers.models import Supplier
from inflows.models import Inflow


class InflowStockTestCase(TestCase):
    """Regra de negócio: uma entrada (inflow) adiciona ao estoque do produto (signal post_save)."""

    def setUp(self):
        brand = Brand.objects.create(name="Marca")
        category = Category.objects.create(name="Categoria")
        self.supplier = Supplier.objects.create(name="Fornecedor")
        self.product = Product.objects.create(
            title="Produto X", brand=brand, category=category,
            cost_price=Decimal("10.00"), selling_price=Decimal("20.00"), quantity=5,
        )

    def test_entrada_adiciona_ao_estoque(self):
        Inflow.objects.create(supplier=self.supplier, product=self.product, quantity=4)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 9)

    def test_entradas_sucessivas_acumulam(self):
        Inflow.objects.create(supplier=self.supplier, product=self.product, quantity=4)
        Inflow.objects.create(supplier=self.supplier, product=self.product, quantity=6)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 15)

    def test_entrada_quantidade_zero_nao_altera_estoque(self):
        Inflow.objects.create(supplier=self.supplier, product=self.product, quantity=0)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 5)
