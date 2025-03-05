from flask import Flask, request, Response
import requests

app = Flask(__fake_url_maker__)

# Target website jo mirror karni hai jiski fake url apko banani he yaha per dalo niche
ORIGINAL_SITE = "https://token2.raghavchoudhary.site/"  # Change this to actual target- url change kr lena Original Website ka 

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    try:
        # Requested URL construct kar raha hai
        url = f"{ORIGINAL_SITE}/{path}"

        
        response = requests.get(url, stream=True)

        # Headers cleanup aur set karna
        excluded_headers = ['content-encoding', 'transfer-encoding', 'content-length', 'connection']
        headers = {k: v for k, v in response.headers.items() if k.lower() not in excluded_headers}

        # MIME type ko properly preserve karna
        return Response(response.content, response.status_code, headers)

    except requests.exceptions.RequestException as e:
        return f"Error fetching {path}: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
