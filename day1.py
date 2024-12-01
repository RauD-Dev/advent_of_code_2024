class AdventDay1:

    def __init__(self):
        self.left = []
        self.right = []
        with open('day1input.txt', 'r') as f:
            for line in f.readlines():
                l, r = line.split()
                self.left.append(int(l))
                self.right.append(int(r))
        self.left.sort()
        self.right.sort()
        self.left_counter = self._val_counter(self.left)
        self.right_counter = self._val_counter(self.right)
        self.part1 = 0
        self.part2 = 0

    def get_diff_sum(self):
        for i in range(len(self.left)):
            self.part1 += abs(self.left[i] - self.right[i])

    def get_similarity_score(self):
        for key, val in self.left_counter.items():
            self.part2 += key * val * self.right_counter.get(key, 0)

    def _val_counter(self, list):
        counts = {}
        for x in list:
            counts[x] = counts.get(x, 0) + 1
        return counts


if __name__ == '__main__':
    day1 = AdventDay1()
    day1.get_diff_sum()
    day1.get_similarity_score()
    print(day1.part1, day1.part2)
