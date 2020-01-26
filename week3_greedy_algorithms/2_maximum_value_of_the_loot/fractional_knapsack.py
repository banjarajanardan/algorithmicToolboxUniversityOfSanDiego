# Uses python3

def get_optimal_value(capacity, weights, values):
    value = 0.
    valuePerweight = [0] * len(values)

    for i in range(len(values)):
        valuePerweight[i] = values[i]/weights[i]

    for i in range(len(values)):
        if capacity == 0:
            return value
        indexOfMaxValuePerWeight = valuePerweight.index(max(valuePerweight))
        if weights[indexOfMaxValuePerWeight] < capacity:
            value += values[indexOfMaxValuePerWeight]
            capacity -= weights[indexOfMaxValuePerWeight]
        else:
            value += valuePerweight[indexOfMaxValuePerWeight] * capacity
            capacity -= capacity

        valuePerweight.pop(indexOfMaxValuePerWeight)
        weights.pop(indexOfMaxValuePerWeight)
        values.pop(indexOfMaxValuePerWeight)
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    weights = [0] * n
    values = [0] * n
    for i in range(n):
        values[i], weights[i] = map(int, input().split())
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
