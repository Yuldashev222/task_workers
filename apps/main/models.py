from django.db import models
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    """
    Departments. Examples: accounting, sales department, ...
    """
    name = models.CharField(
        verbose_name=_('подразделение'),
        max_length=255,
        unique=True,
        db_index=True
    )

    parent = models.ForeignKey(
        verbose_name=_('подразделение'),
        to='self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )  # last

    def clean(self):
        # check подразделение имеют структуру до 5 уровней
        try:
            if self.parent.parent.parent.parent.parent:
                raise ValidationError(
                    {'parent': 'подразделение имеют структуру до 5 уровней'}
                )
        except AttributeError:
            pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('подразделение')
        verbose_name_plural = _('подразделении')


class Position(models.Model):
    """
    Worker position model. Examples: Director, accountant, security, ...
    """
    name = models.CharField(
        verbose_name=_('должность'),
        max_length=255,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('должность')
        verbose_name_plural = _('должности')


class Worker(models.Model):
    """
    Worker information model
    """

    first_name = models.CharField(
        verbose_name=_('имя'),
        max_length=50
    )

    last_name = models.CharField(
        verbose_name=_('фамилия'),
        max_length=50,
    )

    father_name = models.CharField(
        verbose_name=_('отчество'),
        max_length=50,
        blank=True
    )  # blank=True Optional

    position = models.ForeignKey(
        verbose_name=_('должность'),
        to=Position,
        on_delete=models.PROTECT
    )

    department = models.ForeignKey(
        verbose_name=_('подразделение'),
        to=Department,
        on_delete=models.PROTECT
    )

    salary = models.DecimalField(
        verbose_name=_('размер заработной платы'),
        max_digits=20,
        decimal_places=2
    )

    date_joined = models.DateField(
        verbose_name=_('дата приема на работу'),
        blank=True,
        null=True
    )  # blank=True, null=True Optional

    class Meta:
        verbose_name = _('сотрудник')
        verbose_name_plural = _('сотрудники')
