class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if self._title is None:
            if isinstance(value, str) and 5 <= len(value) <= 50:
                self._title = value

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self.__dict__["name"] = name
    def __setattr__(self, key, value):
        if  key == "name" and "name" in self.__dict__:
            return
        super().__setattr__(key, value)

    def articles(self):
        return [article for article in Article.all if article.author == self]   
        pass

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))   
        pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        pass

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))
    def __repr__(self):
        return f"Author(name='{self.name}')"
        pass

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        #else: raise ValueError("Name must be a non-empty string")

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and 3 <= len(value) <= 20:
            self._category = value
        #else: raise ValueError("Category must be a non-empty string")
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        return list(set(article.author for article in self.articles()))
        pass

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in self.articles()]
        pass

    def contributing_authors(self):
        authors = [
            author for author in self.contributors() 
            if len([a for a in self.articles() if a.author == author]) > 2
        ]
        if not authors:
            return None
        return authors
        pass