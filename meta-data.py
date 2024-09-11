from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_meta_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

        metadata = {
            'title': soup.title.string if soup.title else 'No title found',
            'description': '',
            'keywords': ''
        }

        # Get meta description
        description = soup.find('meta', attrs={'name': 'description'})
        if description and 'content' in description.attrs:
            metadata['description'] = description['content']

        # Get meta keywords
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords and 'content' in keywords.attrs:
            metadata['keywords'] = keywords['content']

        return metadata
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

@app.route('/get-meta-data', methods=['GET'])
def get_meta_data_api():
    url = request.args.get('url')
    print(url)
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    metadata = get_meta_data(url)
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True, port=9000)
