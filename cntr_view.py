# from note_mvc import TagsModel
from note_mvc import NotesModel


class Controller:

    def __init__(self, model): #, view):
        self.model = model
        # self.view = view

    def basic_output(self):
        menu_items = self.model.items()
        return self.model.sort_items()

    def query_output(self, query):
        menu_items = self.model.items()
        query_result = self.model.query(menu_items, query)
        return self.model.sort_items()

    def sub_query_output(self, subquery):
        menu_items = self.model.items()
        query_result = self.model.sub_query(menu_items, subquery)
        return self.model.sort_items()





#    tui_object = {
#        "title": string,
#        "description": string,
#        "subheadings": list[string, string],
#    }

# class View:
#     def __init__(self):
#         pass
#     def attach_info(self, items, info):
#         for item in items:



notes_model = NotesModel()
# view = View()

note_control = Controller(notes_model) #, view)

for x in note_control.basic_output():
    print(x)
    print('\n')



# tags_model = TagsModel()
# tag_control = Controller(tags_model)


