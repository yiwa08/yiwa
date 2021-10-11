# typo
# test
# add 3rd
import sys

class State:
    def __init__(self, m=2, c=2, l=True):
        self.m = m
        self.c = c
        self.l = l

    def __str__(self):
        if self.l:
            return "(" + str(self.m) + ", " + str(self.c) + ", " + "L)"
        else:
            return "(" + str(self.m) + ", " + str(self.c) + ", " + "R)"
    
    def can_move(self, m, c):
        if self.l:
            if self.m < m or self.c < c:
                return False
            if self.m - m > 0 and self.m - m < self.c - c:
                return False
            if 2 - self.m + m > 0 and 2 - self.m + m < 2 - self.c + c:
                return False
        if not self.l:
            if 2 - self.m < m or 2 - self.c < c:
                return False
            if self.m + m > 0 and self.m + m < self.c + c:
                return False
            if 2 - self.m - m > 0 and 2 - self.m - m < 2 - self.c - c:
                return False
        return True

    def move(self, m, c):
        news = State()
        if self.l:
            news.m = self.m - m
            news.c = self.c - c
        else:
            news.m = self.m + m
            news.c = self.c + c
        news.l = not self.l
        return news

result = []

def dfs(state, alist, visited):
    news = State()
    MC_combinations = [(0,1), (0,2), (1,0), (1,1), (2,0)]
    if state.m == 0 and state.c == 0 and not state.l:
        result.append(list(alist))
        return
    for (m,c) in MC_combinations:
        if state.can_move(m, c):
            news = state.move(m, c)
            thistuple = (news.m, news.c, news.l)
            if thistuple not in visited:
                visited.append(thistuple)
                alist.append(news)
                dfs(news, alist, visited)
                visited.pop()
                alist.pop()

if __name__ == "__main__":
    alist = [State(2, 2, True)]
    visited = [(2, 2, True)]
    dfs(alist[0], alist, visited)
    for res in result:
        for s in res:
            print(s)
        print()
    # print(result)
