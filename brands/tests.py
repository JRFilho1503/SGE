from django.contrib.auth.models import User, Permission
from rest_framework import status
from rest_framework.test import APITestCase

from brands.models import Brand


class BrandAPITestCase(APITestCase):
    """Cobre autenticação (401), permissão de escrita (403) e CRUD da API de marcas."""

    def setUp(self):
        self.user = User.objects.create_user(username="qa", password="qa123456")
        perms = Permission.objects.filter(
            content_type__app_label="brands",
            codename__in=["view_brand", "add_brand", "change_brand", "delete_brand"],
        )
        self.user.user_permissions.set(perms)
        self.brand = Brand.objects.create(name="Marca A", description="descrição")
        self.list_url = "/api/v1/brands/"
        self.detail_url = f"/api/v1/brands/{self.brand.id}/"

    def test_listar_sem_autenticacao_retorna_401(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_criar_sem_permissao_retorna_403(self):
        sem_perm = User.objects.create_user(username="noperm", password="x1234567")
        self.client.force_authenticate(user=sem_perm)
        resp = self.client.post(self.list_url, {"name": "Marca B"})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_marcas(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_criar_marca(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.post(self.list_url, {"name": "Marca B"})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 2)

    def test_atualizar_marca(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.put(self.detail_url, {"name": "Marca Z"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.brand.refresh_from_db()
        self.assertEqual(self.brand.name, "Marca Z")

    def test_remover_marca(self):
        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.count(), 0)
