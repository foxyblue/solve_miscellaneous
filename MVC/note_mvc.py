import pickle
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def fuzzy_match(title, iterable):
    print("Yup, not found! Try one of these:")
    print(iterable)
    exit()


def load_meta():
    with open('note_data.pkl', 'rb') as _input:
        return pickle.load(_input)


class Model:

    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key, value pairs of its information."""
        raise NotImplementedError

    @property
    def model_type(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.items)

# 1.) If choosing the sort as part of the model
# The order is part of the model, so it should go there.
# A raw pull of "all data" would return the data in the
# sorted order, and there is no interface to choose the
# sort order.

class NotesModel(Model):
    """ The model should be agnostic with how you store the data
        and the app it is serving too.

        - The model should not know of specifics with the app.
    """
    model_type = 'notes'
    notes = load_meta()
    tags = [values['tags'] for _, values in notes.items()]
    tags = [n for x in tags for n in x]

    def __iter__(self):
        for item in self.notes:
            yield item

    def __len__(self):
        return len(self.notes)

    def get(self, title):
        try:
            return self.notes[title]
        except KeyError as e:
            fuzzy_match(title, self.notes.keys())

    def get_value(self, item, info):
        return self.notes[item].get(info, None)

    def get_values(self, iterable, info):
        return [self.get_value(item, info)
                for item in iterable]

    def query_tags(self, tag):
        titles = [title
                 for title, values in self.notes.items()
                 if 'tags' in values and tag in values['tags']]
        if titles:
            return titles
        fuzzy_match(tag, self.tags)

    def query_titles(self, query):
        titles = [title
                  for title, values in self.note.items()
                  if title.startswith(query)]
        if titles:
            return titles
        self.get(query)


class TagsModel(Model):
    model_type = 'tags'

    def __init__(self, note_model):
        tags = OrderedCounter(note_model.tags).most_common()
        tags = [
            (tag, str(count),
                [
                (title, note_model.get_value(title, 'description'))
                for title in note_model.query_tags(tag)])
            for tag, count in tags
        ]

        tags = {tag: {'title': tag,
                 'description': count,
                 'sub_headings': titles}
                 for tag, count, titles in tags}
        self.tags = tags

    def __iter__(self):
        for item in self.tags:
            yield item

    def __len__(self):
        return len(self.tags)

    def get(self, tag):
        try:
            return self.tags[tag]
        except KeyError as e:
            fuzzy_match(tag, self.tags.keys())

    def get_value(self, item, info):
        return self.tags[item].get(info, None)

    def query_tags(self, query):
        tags = [tag
                for tag, values in self.tags.items()
                if tag.startswith(query)]
        if tags:
            return tags
        self.get(query)

# Should this (Service) communicate with the model??
#   - should the model build [title, subtitle, drop_down] for TUI
#   - would defining a column interface be easier and passing all the data make
#     things less complicated? e.g. I want title, subtitle drop_down=views
#   - Alternatively I pass only the things I need for sorting to Service
#
# What I am actually doing??
#  - I want x, y, z after sorting after querying.
class Service:
    """ The Service should satisfy the requirements of the View
        and contain app specific logic.
    """
    ORDER_RULE = 5
    TOP_n_VIEWED = 3

    def __init__(self, model):
        self.model = model

    def order(self, items):
        if self.model.model_type == 'notes':
            return self.order_notes(items)
        return self.order_tags(items)

    def order_tags(self, items):
        return self.by_count(items)

    def order_notes(self, items):
        if len(items) > self.ORDER_RULE:
            return self.alphabetize(items)
        return self.last_viewed(items)

    def alphabetize(self, iterable):
        return sorted(iterable, key=lambda x: x[0].lower())

    def last_viewed(self, iterable):
        sort_key = lambda i: self.model.get_value(i, 'modified')
        return sorted(iterable,
                      key=sort_key,
                      reverse=True)

    def by_count(self, iterable):
        sort_key = lambda i: int(self.model.get_value(i, 'description'))
        return sorted(iterable,
                      key=sort_key,
                      reverse=True)

    def structure(self, iterable):
        x, y, z = ['title', 'description', 'sub_headings']
        return [{'title': item,
                 # tag model should calculate count as description
                 'description': self.model.get_value(item, y),
                 'sub_heading': self.model.get_value(item, z)}
                 for item in iterable]


if __name__ == '__main__':
    note_model = NotesModel()
    print(note_model.get_views('drops'))
