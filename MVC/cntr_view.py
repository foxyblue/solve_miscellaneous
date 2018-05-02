# from note_mvc import TagsModel
from note_mvc import NotesModel
from note_mvc import Service

#    tui_object = {
#        "title": string,
#        "description": string,
#        "subheadings": list[string, string],
#    }


# Show this, hide that etc
# forwards info to view
# handles dictation of models

class Controller:

    def __init__(self, model):
        self.model = model
        self.service = Service(model)
        self.menu_items = self.model.items()

    def basic_output(self):
        return self.model.sort_items()

    def query_output(self, query):
        query_result = self.model.query(self.menu_items, query)
        return self.model.sort_items()

    def sub_query_output(self, subquery):
        query_result = self.model.sub_query(self.menu_items, subquery)
        return self.model.sort_items()

""" Prototype View Interface
def list_notes(query):
    notes_model = NotesModel()
    control = Controller(notes_model)
    if query:
        return display_list(control.query_output(query))
    else:
        return display_list(note_control.basic_output())
def list_tags(query):
    tags_model = TagsModel()
    control = Controller(notes_model)
    if query:
        return display_list(control.query_output(query))
    else:
        return display_list(control.basic_output())
def list_search(query):
    notes_model = NotesModel()
    control = Controller(notes_model)
    if query:
        return display_list(control.model_query(query))
    else:
        raise NotImplementedError
"""


notes_model = NotesModel()
# view = View()

note_control = Controller(notes_model) #, view)


for x in note_control.basic_output():
    print(x)
    print('\n')



# tags_model = TagsModel()
# tag_control = Controller(tags_model)


