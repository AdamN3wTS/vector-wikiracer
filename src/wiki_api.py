import wikipediaapi
from wikipediaapi._enums import RedirectFilter

from models import WikiModel
from vectorize import vectorini

wikiApi = wikipediaapi.Wikipedia('MyProjectName (example@example.com)', 'en',extract_format=wikipediaapi.ExtractFormat.WIKI)

# Steps:
# 1. Random wiki_link1 -> random wiki_link2
# 1.1 link ->
# {
#   "name": "Poland"
#   "url": "www.wikipedia.com/Poland"
# }
# 2. Cheks all links if url is the same not -> take what is the most similar -> repeat

def random_wiki():
    title_random = ""
    url_random = ""
    pages = wikiApi.random(limit=1)
    
    for title in pages:
        page_py = get_wiki(title)
        title_random=title
        url_random=page_py.fullurl
    return WikiModel(title_random,url_random)
def convert_wikiModel(title,url):
    return WikiModel(title,url)


def get_wiki(_title):
    pages = wikiApi.page(_title)
    return pages

def searchArticle(articleStart:WikiModel,articleEnd:WikiModel,no_words=[],i=1):
    print(f"podejscie nr {i}",flush=True)
    articleStartPage=get_wiki(articleStart.title)
    word,value = vectorini(articleStartPage.links,articleEnd.title,no_words)
    no_words.append(word)
    page=get_wiki(word)
    print(f"get: {word} score: {value}",flush=True)
    if page.fullurl==articleEnd.url:
        print("FINALLYYYY ",flush=True)
        return
    new_model=convert_wikiModel(page.title,page.fullurl)
    return searchArticle(new_model,articleEnd,i=i+1)



