import pickle


def fuzzy_match(title, iterable):
    print("Yup, not found! Try one of these:")
    print(iterable)


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

    def items(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.items)

# 1.)
# The order is part of the model, so it should go there.
# A raw pull of "all data" would return the data in the
# sorted order, and there is no interface to choose the
# sort order.

class NotesModel(Model):
    model_type = 'notes'
    notes = load_meta()

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
        return [self.get_attribute(item, info)
                for item in iterable]

    def get_structure(self, iterable, structure):

        return [{item:

# Should this (Service) communicate with the model??
#   - should the model build [title, subtitle, drop_down] for TUI
#   - would defining a column interface be easier and passing all the data make
#     things less complicated? e.g. I want title, subtitle drop_down=views
#   - Alternatively I pass only the things I need for sorting to Service
#
# What I am actually doing??
#  - I want x, y, z after sorting after querying.
class Service:

    SORT_RULE = 5
    TOP_n_VIEWED = 3

    def __init__(self):
        pass

    def sort(self, items):
        if len(items) > self.SORT_RULE:
            return self.alphabetize(items)
        return self.alphabetize(items)

    @staticmethod
    def alphabetize(iterable):
        sort = sorted(iterable, key=lambda x: x[0].lower())
        return sort


if __name__ == '__main__':
    note_model = NotesModel()
    print(note_model.get_views('drops'))
