class AdventDay2:

    def __init__(self):
        self.data = []
        self.unsafe = []
        with open('input_files/day2input.txt', 'r') as f:
            for line in f.readlines():
                self.data.append([int(x) for x in line.split()])
        self.part1 = 0
        self.part2 = 0

    def find_safe_reports(self):
        for i, row in enumerate(self.data):
            if self._is_safe_row(row):
                self.part1 += 1
                self.part2 += 1
            else:
                self.unsafe.append(i)

    def allow_one_bad_level(self):
        for index in self.unsafe:
            row = self.data[index]
            for i in range(len(row)):
                if self._is_safe_row(row[:i] + row[i+1:]):
                    self.part2 += 1
                    break

    def _is_safe_row(self, row):
        self.row_diff_set = {row[j] - row[j-1] for j in range(1, len(row))}
        return (self.row_diff_set <= {1, 2, 3} or
                self.row_diff_set <= {-1, -2, -3})


if __name__ == '__main__':
    mgr = AdventDay2()
    mgr.find_safe_reports()
    mgr.allow_one_bad_level()
    print(mgr.part1, mgr.part2)
