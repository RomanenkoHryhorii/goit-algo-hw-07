# функція для знаходження найбільшого значення

def find_max_value(root):
    # Якщо дерево порожнє, повертаємо None
    if not root:
        return None
    
    # Проходимо максимально праворуч по дереву
    current = root
    while current.right is not None:
        current = current.right
    
    # Повертаємо значення найправішого вузла (максимальне)
    return current.key


# функція для знаходження найменшого значення

def find_min_value(root):
    # Якщо дерево порожнє, повертаємо None
    if not root:
        return None
    
    # Проходимо максимально ліворуч по дереву
    current = root
    while current.left is not None:
        current = current.left
    
    # Повертаємо значення найлівішого вузла (найменше)
    return current.key


# функція знаходження суми всіх значень

def calculate_tree_sum(root):
    # Базовий випадок: якщо дерево порожнє, повертаємо 0
    if not root:
        return 0
    
    # Рекурсивно обраховуємо суму:
    # поточний вузол + сума лівого піддерева + сума правого піддерева
    return (root.key + 
            calculate_tree_sum(root.left) + 
            calculate_tree_sum(root.right))