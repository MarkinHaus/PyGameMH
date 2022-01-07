name_list = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
             (255, 255, 255)]
list_name = ["black", "red", "green", "blue", "yellow", "purple", "azul", "white"]


def name_to_list(name: str):
    return name_list[list_name.index(name.lower())]
