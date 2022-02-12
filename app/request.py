from . models import Quote
import urllib.request,json


base_url=None
def configure_request(app):
  global base_url
  base_url=app.config['QUOTE_BASE_URL']
# base_url='http://quotes.stormconsultancy.co.uk/random.json'
  
def get_quote():
  '''
  Function that gets a random quote
  '''
  print(base_url)
  with urllib.request.urlopen(base_url) as url:
    get_quote_data=url.read()
    quote_response=json.loads(get_quote_data)

    quote_result=None

    if quote_response:
      quote_result=map_quote_result(quote_response)

    return quote_result

def map_quote_result(quote_obj):

  id=quote_obj.get('id')
  author=quote_obj.get('author')
  quote=quote_obj.get('quote')
  permalink=quote_obj.get('permalink')

  new_quote=Quote(id,author,quote,permalink)

  return new_quote
