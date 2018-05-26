from note_mvc import TagsModel
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

# alias to display_list
def view_list(_list):
    for item in _list:
        title = item['title']
        descr = item['description']
        sub_titles = item['sub_heading']
        print("Title: {}, Description: {}".format(title, descr))
        if sub_titles:
            for s in sub_titles:
                s_1, s_2 = s[:2]
                print("\t- {}: {}".format(s_1, s_2))


class Controller:
    """ The controller should be agnostic to the interface that display the
        data.
    """

    def __init__(self, model_type):
        self.model = NotesModel()
        if model_type == 'tags':
            self.model = TagsModel(self.model)
        self.service = Service(self.model)

    def basic_output(self):
        items = list(self.model)
        self.__apply_service(items)

    def query_output(self, query=None):
        items = self.model.query_tags(query)
        self.__apply_service(items)

    def search_output(self, query):
        if not query:
            print("\n\tNo Query Error\n")
            exit()
        items = self.model.query_titles(query)
        self.__apply_service(items)

    def __apply_service(self, items):
        ordered_items = self.service.order(items)
        structure = self.service.structure(ordered_items)
        return view_list(structure)


# Actor logic:
ctrl = Controller('notes')
# ctrl = Controller('tags')
# ctrl.basic_output()
ctrl.query_output('tagle')

# ctrl = Controller('tags')
# ctrl.basic_output()
# print(ctrl.query_output(query))


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

