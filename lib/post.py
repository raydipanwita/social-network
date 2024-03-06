
class Post:
    def __init__(self, id, title, contents, no_of_views):
        self.id = id
        self.title = title
        self.contents = contents
        self.no_of_views = no_of_views
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post{(self.id), (self.title), (self.contents), (self.no_of_views)}"