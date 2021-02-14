class Staircase():
    def __init__(self, n):
        self.n = n

    def printing(self):
        last_line = ''
        for i in range(0, self.n):
            for j in range(0, self.n):
                if j < self.n-1:
                    print(' ', end='')
                elif j == self.n-1:
                    new_line = '#'+last_line
                    print(new_line)
                    last_line = new_line
                    self.n = self.n-1