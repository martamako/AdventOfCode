import operator

file = open("input.txt", "r")
lines = file.read().splitlines()

ops = {
    'AND': operator.and_,
    'OR': operator.or_,
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift,
    'NOT': operator.not_
}

gates = {}

for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
    gates[lines[i][-1]] = -1


def find_gate(name: str) -> int:
    signal_value = -1

    if gates[name] >= 0:
        signal_value = gates[name]
        return signal_value

    for i in range(len(lines)):
        if lines[i][-1] == name:
            if len(lines[i]) == 3:
                if lines[i][0].isnumeric():
                    gates[name] = int(lines[i][0])
                    signal_value = gates[name]
                    break
                else:
                    signal_value = find_gate(lines[i][0])
                    signal_value = signal_value & 0xffff
                    gates[name] = signal_value
                    break
            elif len(lines[i]) == 4:
                signal_value = ~find_gate(lines[i][1])
                signal_value = signal_value & 0xffff
                gates[name] = signal_value
                break
            elif len(lines[i]) == 5:
                if lines[i][2].isnumeric():
                    signal_value = ops[lines[i][1]](find_gate(lines[i][0]), int(lines[i][2]))
                    signal_value = signal_value & 0xffff
                    gates[name] = signal_value
                    break
                elif lines[i][0].isnumeric():
                    signal_value = ops[lines[i][1]](int(lines[i][0]), find_gate(lines[i][2]))
                    signal_value = signal_value & 0xffff
                    gates[name] = signal_value
                    break
                elif lines[i][2].isnumeric() and lines[i][0].isnumeric():
                    signal_value = ops[lines[i][1]](int(lines[i][0]), int(lines[i][2]))
                    signal_value = signal_value & 0xffff
                    gates[name] = signal_value
                    break
                else:
                    signal_value = ops[lines[i][1]](find_gate(lines[i][0]), find_gate(lines[i][2]))
                    signal_value = signal_value & 0xffff
                    gates[name] = signal_value
                    break

    return signal_value


a = find_gate('a')

for gate in gates:
    gates[gate] = -1

gates['b'] = a
a = find_gate('a')
print(a)
