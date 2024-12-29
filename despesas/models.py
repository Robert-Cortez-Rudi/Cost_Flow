from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Entrada(models.Model):
    CATEGORIAS_ENTRADA = [
        ('salario', 'Salário'),
        ('dividendos', 'Dividendos'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='entradas',
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_ENTRADA,
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    def clean(self):
        if self.valor <= 0:
            raise ValidationError('O valor da entrada deve ser positivo.')

    class Meta:
        ordering = ['-data']
        verbose_name_plural = 'Entradas'


class Despesa(models.Model):
    CATEGORIAS_SAIDA = [
        ('gastos', 'Gastos'),
        ('despesas', 'Despesas'),
        ('contas', 'Contas'),
        ('investimento', 'Investimento'),
        ('outros', 'Outros'),
        ('alimentacao', 'Alimentação'),
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('lazer', 'Lazer'),
        ('moradia', 'Moradia'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='despesas',
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_SAIDA,
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    def clean(self):
        if self.valor <= 0:
            raise ValidationError('O valor da despesa deve ser positivo.')

    class Meta:
        ordering = ['-data']
        verbose_name_plural = 'Despesas'
