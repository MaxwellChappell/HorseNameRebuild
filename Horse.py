class Horse():
    def __init__(self, name, link, generation):
        self.name = name
        self.link = link
        self.generation = {generation}

    def add_generation(self, generation):
        self.generation.add(generation)

    def print_info(self):
        return f"{self.name}, {self.link}, {self.generation}\n"

    def __str__(self):
        return self.link

    def __eq__(self, ob):
        return self.name == ob.name or self.link == ob.link
