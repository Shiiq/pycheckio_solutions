# In computer science, a queue is a particular kind of data type
# in which the entities in the collection are kept in order and
# the principal operations on the collection are the addition of
# entities to the rear terminal position (enqueue or push),
# and removal of entities from the front terminal position (dequeue or pop).
# This makes the queue a First-In-First-Out (FIFO) data structure.
# In a FIFO data structure, the first element added to the queue will be
# the first one to be removed. This is equivalent to the requirement that
# once a new element is added, all elements that were added before have
# to be removed before the new element can be removed.
#
# We will emulate the queue process with Python. You are given a sequence of commands:
# - "PUSH X" -- enqueue X , where X is a letter in uppercase.
# - "POP" -- dequeue the front position. if the queue is empty, then do nothing.
# The queue can only contain letters.
#
# You should process all commands and assemble letters which remain in the queue in one word from the front to the rear of the queue.
#
# Let's look at an example, here’s the sequence of commands:
# ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]

# letter_queue(['PUSH A',
#  'POP',
#  'POP',
#  'PUSH Z',
#  'PUSH D',
#  'PUSH O',
#  'POP',
#  'PUSH T']) == 'DOT'
# letter_queue(['POP', 'POP']) == ''
# letter_queue(['PUSH H', 'PUSH I']) == 'HI'
# letter_queue([]) == ''
INPUT = ['PUSH A', 'POP', 'POP', 'PUSH Z', 'PUSH D', 'PUSH O', 'POP', 'PUSH T']
cmds = {
    "POP": lambda q: q.pop(),
    "PUSH": lambda q, x: q.push(x)
}

class Q:

    def __init__(self):
        self.data = []

    def pop(self):
        try:
            return self.data.pop(0)
        except IndexError:
            return None

    def push(self, val):
        self.data.append(val)


def letter_queue(input_commands: list[str]):
    q = Q()
    for command in input_commands:
        c = command.strip().split()
        cmd = cmds[c[0]]
        if len(c) == 2:
            arg = c[1]
            cmd(q, arg)
        elif len(c) == 1:
            cmd(q)
    return "".join(q.data)


if __name__ == '__main__':
#     # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(
        ['PUSH A', 'POP', 'POP', 'PUSH Z', 'PUSH D', 'PUSH O', 'POP', 'PUSH T']
    ) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
