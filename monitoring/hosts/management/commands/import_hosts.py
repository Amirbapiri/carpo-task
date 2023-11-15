import csv
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from monitoring.hosts.models import Host
from monitoring.organs.models import Organ

User = get_user_model()

class Command(BaseCommand):
    help = "Upload Host instances from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the csv file")

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs.get("csv_file")

        rows_generator = self.read_csv_rows(csv_file_path)
        for row in rows_generator:
            self.process_row(row)

    def read_csv_rows(self, file_path):
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                yield row

    def process_row(self, row):
        host_name, description, organ_name = row
        sys_user = User.objects.get(pk=2)
        organ, created = Organ.objects.get_or_create(name=organ_name, sys_admin=sys_user)
        host, created = Host.objects.get_or_create(
            name=host_name,
            description=description,
            organ=organ,
            host_admin=sys_user,
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Host created: {host.name}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Host already exists: {host.name}"))
