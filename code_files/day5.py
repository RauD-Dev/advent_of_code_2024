class AdventDay5:

    def __init__(self):
        self.rules: dict[int, set] = {}
        self.updates = []
        self.bad_updates = []
        with open('input_files/day5input.txt', 'r') as f:
            for line in f.readlines():
                if '|' in line:
                    self._process_rule(self._process_line(line, '|'))
                elif line == '\n':
                    pass
                else:
                    self.updates.append(self._process_line(line, ','))
        self.part1 = 0
        self.part2 = 0

    def check_updates(self):
        for update in self.updates:
            good = True
            for i in range(len(update) - 1, 0, -1):
                if not self.rules[update[i]].isdisjoint(set(update[:i])):
                    good = False
                    self.bad_updates.append(update)
                    break

            if good:
                self.part1 += update[len(update)//2]

    def _process_rule(self, item: list[int]):
        try:
            self.rules[item[0]].add(item[1])
        except KeyError:
            self.rules[item[0]] = set([item[1]])

    def _process_line(self, string_list: str, on: str):
        return [int(x) for x in string_list.replace('\n', '').split(on)]


if __name__ == '__main__':
    mgr = AdventDay5()
    mgr.check_updates()
    print(mgr.part1, mgr.part2)
