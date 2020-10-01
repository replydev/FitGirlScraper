class Article:
    def __init__(self,title,link,magnet):
        self.title = title
        self.link = link
        self.magnet = magnet

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def get_magnet(self):
        return self.magnet