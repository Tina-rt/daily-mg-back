def clean(list_of_headlines):
    links = []
    result = []
    for headline in list_of_headlines:
        if headline['link'] not in links:
            result.append(headline)
            links.append(headline['link'])
    return result