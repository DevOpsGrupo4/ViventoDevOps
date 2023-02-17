from django.test import TestCase

# Create your tests here.
from inmobiliaria.models import Cargo

# Create your tests here.
class CargoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Cargo.objects.create(codigo='020',nombre='Jefe de Operaciones', actividad='Operaciones')

    def test_codigo_label(self):
        cargo=Cargo.objects.get(id=1)
        field_label = cargo._meta.get_field('codigo').verbose_name
        self.assertEquals(field_label,'codigo')

    def test_nombre_label(self):
        cargo=Cargo.objects.get(id=1)
        field_label = cargo._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_actividad_label(self):
        cargo=Cargo.objects.get(id=1)
        field_label = cargo._meta.get_field('actividad').verbose_name
        self.assertEquals(field_label,'actividad')
