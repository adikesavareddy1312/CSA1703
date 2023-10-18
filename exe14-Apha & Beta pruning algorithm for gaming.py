def alpha_beta_pruning(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or node.is_terminal_node:
        return node.evaluate()

    if is_maximizing_player:
        best_value = -float("inf")
        for child in node.get_children():
            value = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float("inf")
        for child in node.get_children():
            value = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value

class Node:
    def __init__(self, value, is_terminal_node, children=[]):
        self.value = value
        self.is_terminal_node = is_terminal_node
        self.children = children

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children

root_node = Node(0, False, [Node(3, False, [Node(4, True), Node(5, True)]), Node(6, False, [Node(7, True), Node(8, True)])])

result = alpha_beta_pruning(root_node, 3, -float("inf"), float("inf"), True)
print("Best value:", result)
