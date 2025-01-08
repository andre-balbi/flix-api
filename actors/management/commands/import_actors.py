from actors.models import Actor
from django.core.management import BaseCommand
import csv
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="Nome do arquivo com atores")

    def handle(self, *args, **options):
        file_name = options["file_name"]
        print(f"Arquivo: {file_name}")

        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                birthday = datetime.strptime(row["birthday"], "%Y-%m-%d").date()
                nationality = row["nationality"]

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name, birthday=birthday, nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS("Atores importados com sucesso!"))
