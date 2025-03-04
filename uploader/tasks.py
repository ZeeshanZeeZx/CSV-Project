import pandas as pd
from celery import shared_task
from .models import CSVFile

@shared_task
def process_csv(csv_id):
    csv_file = CSVFile.objects.get(id=csv_id)
    file_path = csv_file.file.path
    
    try:
        df = pd.read_csv(file_path, usecols=['Index', 'Customer Id', 'First Name', 'Last Name'])
        
        result = {"Total Rows": len(df)}

        # Save result
        csv_file.result = str(result)
        csv_file.processed = True
        csv_file.save()
    except Exception as e:
        csv_file.result = f"Error: {str(e)}"
        csv_file.save()