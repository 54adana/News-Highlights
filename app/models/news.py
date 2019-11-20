class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,source_name,title,description,poster, url):
        self.source_name =source_name
        self.title = title
        self.description = description
        self.poster = poster
        self.url = url
        