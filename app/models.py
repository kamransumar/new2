class Articles:

    def __init__(self, title, author, description, urlToImage, url, publishedAt):
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt


class Source:

    def __init__(self, id, name, description, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
