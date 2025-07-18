# import_data.py inside harrychart/management/commands/
from django.core.management.base import BaseCommand
import pandas as pd
from harrychart.models import Commits

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the Commits model'

    def handle(self, *args, **kwargs):
        csv_file_path = r"C:\Users\madhshiva\Desktop\Airtel_Intern\git_commit_data.csv"
        df = pd.read_csv(csv_file_path)

        for index, row in df.iterrows():
            Commits.objects.get_or_create(
                created_dates=row["created_dates"],
                author_name=row["author_name"],
                added_lines=row["added_lines"],
                deleted_lines=row["deleted_lines"],
                project_name=row["project_name"],
                merge=row["merge"],
                hash_commit=row["hash_commit"],
                email=row["email"]
            )

        self.stdout.write(self.style.SUCCESS('Data import successful!'))
