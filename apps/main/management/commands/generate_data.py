import random

from django.core.management import BaseCommand
from faker import Faker

from apps.main.models import Worker, Department

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        Worker.objects.all().delete()
        Department.objects.all().delete()

        # ======== generate departments ===========
        for i in range(5):
            parent = Department.objects.create(
                name=f'Department No {i + 1}'
            )
            for j in range(3):
                parent2 = Department.objects.create(
                    name=f'Department No {i + 1}.{j + 1}',
                    parent=parent
                )
                for k in range(3):
                    parent3 = Department.objects.create(
                        name=f'Department No {i + 1}.{j + 1}.{k + 1}',
                        parent=parent2
                    )
                    for m in range(3):
                        parent4 = Department.objects.create(
                            name=f'Department No {i + 1}.{j + 1}.{k + 1}.{m + 1}',
                            parent=parent3
                        )
                        for n in range(3):
                            Department.objects.create(
                                name=f'Department No {i + 1}.{j + 1}.{k + 1}.{m + 1}.{n + 1}',
                                parent=parent4
                            )

        self.stdout.write('departments created')

        # ======== generate workers ===========
        department_ids = list(Department.objects.values_list('id', flat=True))
        workers = [
            Worker(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                father_name=fake.first_name_male(),
                position=fake.job(),
                department_id=random.choice(department_ids),
                salary=round(random.uniform(30_000, 500_000), 2),
                date_joined=fake.date()
            )
            for _ in range(50_000)
        ]
        Worker.objects.bulk_create(objs=workers)

        self.stdout.write('workers created')
