class Command:
    def __init__(self, number_from: int, symbol_from: int, number_to: int, symbol_to: int, direction: str):
        self.number_from = number_from
        self.symbol_from = symbol_from
        self.number_to = number_to
        self.symbol_to = symbol_to
        self.direction = direction

    def parse_string(string: str):
        arr = string.split()
        return Command(int(arr[0][1:]), int(arr[1]), int(arr[2][1:]), int(arr[3]), arr[4])

def TuringMachine(P: str, commands: list[Command], max_steps: int = 10000):
    index = 0
    state = 1
    steps = 0
    while True:
        if steps >= max_steps:
            print(f"Превышен лимит шагов ({max_steps}). Машина, скорее всего, зациклилась.")
            if len(P) > 100:
                return
            break

        steps += 1

        symbol = int(P[index])
        tmp = list(filter(lambda x: (x.number_from == state and x.symbol_from == symbol), commands))
        if len(tmp) > 0:
            command = tmp[0]
        else:
            command = Command(state, symbol, 0, symbol, 'S')
        state = command.number_to
        if index == len(P) - 1:
            P += '0'
        P = P[:index] + str(command.symbol_to) + P[index + 1:]
        if command.direction == 'R':
            index += 1
        elif command.direction == 'L':
            index -= 1
        if index == -1:
            P = '0' + P
            index += 1
        if state == 0:
            break
    print(P)
    print(index * ' ' + '^')
    print(index * ' ' + '|')
    print(index * ' ' + 'q' + str(state))

commands1 = [Command.parse_string('q1 0 q2 1 L'), 
             Command.parse_string('q1 1 q2 1 R'), 
             Command.parse_string('q2 0 q0 0 S'), 
             Command.parse_string('q2 1 q1 1 R')]
P1 = '110111'
TuringMachine(P1, commands1)

commands2 = [Command.parse_string('q1 0 q1 0 S'), #зацикливание

             Command.parse_string('q1 1 q2 1 R'), 
             Command.parse_string('q2 0 q2 0 S'), #зацикливание при x=0

             Command.parse_string('q2 1 q3 1 R'),
             Command.parse_string('q3 0 q4 1 R'),
             Command.parse_string('q4 0 q5 1 R'),
             Command.parse_string('q5 0 q6 0 L'),
             Command.parse_string('q6 0 q0 0 R'),
             Command.parse_string('q6 1 q6 1 L'), #'1111'=3 при x=1

             Command.parse_string('q3 1 q7 1 R'),
             Command.parse_string('q7 0 q9 1 L'), 
             Command.parse_string('q7 1 q8 1 R'),
             Command.parse_string('q8 1 q12 1 R'),
             Command.parse_string('q8 0 q9 1 L'), #'11'=1 при x in {2, 3}
             
             
             Command.parse_string('q12 1 q12 1 R'),
             Command.parse_string('q12 0 q9 0 L'), #'1'=0 при x>3

             Command.parse_string('q9 1 q10 1 L'),
             Command.parse_string('q10 0 q11 0 R'),
             Command.parse_string('q10 1 q10 0 L'),
             Command.parse_string('q11 0 q11 0 R'),
             Command.parse_string('q11 1 q0 1 S') #оставляем одну единицу, все слева стираем
             ]
P2 = '1' * 50
TuringMachine(P2, commands2)

commands3 = [Command.parse_string('q1 1 q2 0 R'), 
            Command.parse_string('q1 0 q4 0 R'),
            Command.parse_string('q2 1 q2 1 R'),
            Command.parse_string('q2 0 q3 0 R'),
            Command.parse_string('q3 0 q4 1 R'),
            Command.parse_string('q3 1 q3 1 R'),
            Command.parse_string('q4 0 q5 1 L'),
            Command.parse_string('q4 1 q7 0 R'),
            Command.parse_string('q5 1 q5 1 L'),
            Command.parse_string('q5 0 q6 0 L'),
            Command.parse_string('q6 0 q1 0 R'),
            Command.parse_string('q6 1 q6 1 L'),
            Command.parse_string('q7 0 q0 0 R')]
P3 = '111111'
TuringMachine(P3, commands3)