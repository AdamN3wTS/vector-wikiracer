from wiki_api import get_wiki, searchArticle,random_wiki,convert_wikiModel
def main():
    print("======> Wiki search start <======",flush=True)
    aein = get_wiki("Warsaw")
    mars = get_wiki("Apollo 11")
    aein_model = convert_wikiModel(aein.title,aein.fullurl)
    mars_model = convert_wikiModel(mars.title,mars.fullurl)

    start = aein_model
    end = mars_model
    print(f"start: {start.title} end: {end.title}",flush=True)
    searchArticle(start,end)
if __name__=="__main__":
    main()