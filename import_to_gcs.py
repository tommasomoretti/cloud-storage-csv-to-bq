from datetime import date
from google.cloud import storage
 
def upload_to_gcs():
   credentials = '/.../service_account_keys.json' # Modificare con il path del file del service account
   storage_client = storage.Client.from_service_account_json(credentials)
   
   local_path = "/.../" # Modificare con il path in cui c'è il CSV da caricare
   local_file_name = "my_csv.csv" # Modificare con il nome del CSV da caricare
   local_destination = f"{local_path}{local_file_name}"
   
   gcs_bucket_name = "my_bucket" # Modificare con il bucket di destinazione
   gcs_path = ".../" # Modificare con il path di destinazione (se non esiste, verrà creato in automatico)
   current_timestamp = date.today()
   gcs_file_name ="my_data_" + str(current_timestamp.strftime('%Y%m%d')) + ".csv" # Modificare con il nome finale del file da caricare (se esiste già verrà sovrascritto)
   gcs_destination = f"{gcs_path}{gcs_file_name}"
   blob = storage_client.bucket(gcs_bucket_name).blob(gcs_destination)

   try:
       blob.upload_from_filename(local_destination)
       print(f"{local_file_name} uploaded to {gcs_destination}.")
   except Exception as e:
       print(f"Error: {e}")
 
upload_to_gcs()
