class TodoTask:
    description = "";
    name = "";
    isDone = False;

    def __init__(self, name = "", description = ""):
        self.name = name;
        self.description = description;