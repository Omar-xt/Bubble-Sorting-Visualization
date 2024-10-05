from dataclasses import dataclass, field


@dataclass
class BubbleSort:
    arr: list[int]
    offset_x: int = 0
    offset_y: int = 200
    width: int = 20
    spacing: int = 5
    height_multiplier: int = 5
    window_size: tuple[int, int] = field(default_factory=tuple)

    # -- sort releted
    speed: int = 60  # frame rate
    arr_is_sorted: bool = False
    sorting_is_paused: bool = True
    sorted_item_indexes: list[int] = field(default_factory=list)
    marked_items_indexes: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.last_sorted_item_index = len(self.arr) - 1
        self.current_index = 0

        if not len(self.window_size):
            return

        min_offset_x = self.window_size[0] / 20
        arr_width = len(self.arr) * (self.width + self.spacing)

        offx = (self.window_size[0] - arr_width) / 2

        if offx < min_offset_x:
            offx = min_offset_x

            max_width = self.window_size[0] - (min_offset_x * 2)

            self.spacing = 2

            self.width = (max_width / len(self.arr)) - self.spacing

        self.offset_x = offx
        self.offset_y = self.window_size[1] - 50

    def update(self, arr):
        self.arr = arr

        self.reset()
        self.__post_init__()

    def reset(self):
        self.arr_is_sorted = False
        self.sorting_is_paused = True

        self.sorted_item_indexes.clear()
        self.marked_items_indexes.clear()

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def sort(self):
        if self.arr_is_sorted:
            return

        count_loop = 0
        for i in range(self.last_sorted_item_index):
            current = -1
            for j in range(1, self.last_sorted_item_index + 1):
                current += 1
                if self.arr[current] > self.arr[j]:
                    self.swap(j, current)
                count_loop += 1

            self.last_sorted_item_index -= 1

        self.arr_is_sorted = True

        print("sorted in {count_loop}".format(count_loop=count_loop))

    def next_step(self):
        if self.arr_is_sorted:
            return

        if self.current_index == self.last_sorted_item_index:
            self.sorted_item_indexes.append(self.current_index)
            self.current_index = 0
            self.last_sorted_item_index -= 1

            if self.last_sorted_item_index == -1:
                self.current_index = -1
                self.arr_is_sorted = True
                self.marked_items_indexes.clear()
                print("sorted")
            return

        if self.arr[self.current_index] > self.arr[self.current_index + 1]:
            self.swap(self.current_index + 1, self.current_index)
        elif self.current_index + 1 != self.last_sorted_item_index:
            self.marked_items_indexes.append(self.current_index)

        self.current_index += 1

        if self.current_index in self.marked_items_indexes:
            self.marked_items_indexes.pop(
                self.marked_items_indexes.index(self.current_index)
            )

    def run_sorting(self):
        if self.arr_is_sorted or self.sorting_is_paused:
            return

        self.next_step()

    def draw(self, app, py):
        for ind, item in enumerate(self.arr):
            color = "blue"
            x = ind * (self.width + self.spacing) + self.offset_x
            height = item * self.height_multiplier
            if ind in self.sorted_item_indexes:
                color = "green"
            if ind in self.marked_items_indexes:
                color = "white"
            if ind == self.current_index:
                color = "red"
            py.draw.rect(
                app,
                color,
                (x, self.offset_y - height, self.width, item * self.height_multiplier),
            )
