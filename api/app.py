from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os
import io

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"


@app.route('/store', methods=['POST'])
def store():
    data = request.json
    
    try:
    	object_name = data.get("name")
    	content = data.get("content")
    	
    	# Check if the content is a path or a text
    	if (os.path.isfile(content)):
    		print("Entered in image file")
    		minio_client.fput_object(bucket_name, object_name, content)
    		return jsonify({"message": "Data stored successfully"}), 200
    		
    	# Transform the content text to
    	else:
    		content_bytes = content.encode('utf-8')
    		content_stream = io.BytesIO(content_bytes)
    		length = len(content)
    		minio_client.put_object(bucket_name, object_name, content_stream, len(content))
    		return jsonify({"message": "Data stored successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)
    
