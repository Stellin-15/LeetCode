class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        seen = set([0])
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)

        return len(seen) == n
