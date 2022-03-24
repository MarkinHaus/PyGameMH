name_list = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255],
             [255, 255, 255]]
list_name = ["black", "red", "green", "blue", "yellow", "purple", "azul", "white"]


def name_to_list(name: str):
    if name in list_name:
        return name_list[list_name.index(name.lower())]  # converting name to color list (for pygame)
    else:
        assert IndexError(f"Element {name} not in list {list_name}")
