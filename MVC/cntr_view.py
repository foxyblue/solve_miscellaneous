# from note_mvc import TagsModel
from note_mvc import NotesModel
from note_mvc import Service

#    tui_object = {
#        "title": string,
#        "description": string,
#        "subheadings": list[string, string],
#    }
# https://github.com/google/fleetspeak/blob/master/fleetspeak/src/server/comms.go#L137-L142

# Show this, hide that etc
# forwards info to view
# handles dictation of models

class Controller:

    def __init__(self, model):
        if model == 'notes':
            self.model = NotesModel()
        else:
            self.model = TagsModel()
        self.service = Service()

    def basic_output(self):
        items = list(self.model)
        sorted_items = self.service.sort(items)
        # items = self.model.tui_objectify(items) # <-- plan interface
        return sorted_items

    def query_output(self, query):
        query_result = self.model.query(self.menu_items, query)
        return self.model.sort_items()

    def sub_query_output(self, subquery):
        query_result = self.model.sub_query(self.menu_items, subquery)
        return self.model.sort_items()

ctrl = Controller('notes')
print(ctrl.basic_output())


# Features to Solve:

# list_notes - query
#   - output notes
#   - output notes after query on tag
#
# list_tags - query
#   - output tags
#   - output tags after query
#
# list search - query
#   - no query error
#   - output results query starts with on titles

