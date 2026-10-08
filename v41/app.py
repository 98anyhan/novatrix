
from flask import Flask, request
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

STORAGE_ACCOUNT = "stnordvikfelanmalan"
CONTAINER_NAME = "felanmalningar"

account_url = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net"

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
    account_url=account_url,
    credential=credential
)

@app.route("/felanmalan", methods=["POST"])
def felanmalan():
    beskrivning = request.form.get("beskrivning", "")
    bild = request.files.get("bild")

    if not bild or bild.filename == "":
        return "Ingen bild valdes.", 400

    filename = secure_filename(bild.filename)
    blob_name = f"{uuid.uuid4()}-{filename}"

    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(blob_name)

    blob_client.upload_blob(bild.stream, overwrite=True)

    return f"Felanmälan mottagen! Beskrivning: {beskrivning}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
