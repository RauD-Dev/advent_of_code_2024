class AdventDay2:

    def __init__(self):
        self.data = []
        with open('input_files/day2input.txt', 'r') as f:
            for line in f.readlines():
                self.data.append([int(x) for x in line.split()])
        self.part1 = 0

    def find_safe_reports(self):
        def good_diff(a, b):
            if abs(a-b) > 3:
                return False
            return True

        for row in self.data:
            row_good = True
            if row[0] < row[1] and good_diff(row[0], row[1]):
                inc = True
            elif row[0] > row[1] and good_diff(row[0], row[1]):
                inc = False
            else:
                continue
            for i in range(2, len(row)):
                if inc and (row[i-1] >= row[i] or
                            not good_diff(row[i-1], row[i])):
                    row_good = False
                    break
                elif not inc and (row[i-1] <= row[i] or
                                  not good_diff(row[i-1], row[i])):
                    row_good = False
                    break
            if row_good:
                self.part1 += 1


if __name__ == '__main__':
    mgr = AdventDay2()
    mgr.find_safe_reports()
    print(mgr.part1)
