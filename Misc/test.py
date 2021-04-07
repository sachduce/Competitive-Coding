class Node:
    def __init__(self, val):
        self.val = val;
        self.left = None;
        self.right = None;


def countNodes(root):
    if root is None:
        return 0;
    return countNodes(root.left) + countNodes(root.right) + 1;

def traversal(root, arr):
    if(root):
        traversal(root.left, arr);
        arr.append(root.val);
        traversal(root.right, arr);

def arrToBST(arr, root):
    if root is None:
        return;
    arrToBST(arr, root.left);
    root.val = arr[0];
    arr.pop(0);
    arrToBST(arr, root.right);

def binarySearchTree(root):
    if(root is None):
        return;
    n = countNodes(root);
    arr = [];
    traversal(root, arr);
    arr.sort();
    arrToBST(arr, root);



if __name__ == '__main__':
    root = Node(1);
    root.left = Node(2);
    root.right = Node(6);
    root.left.left = Node(17);
    root.left.right = Node(80);
    root.right.left = Node(19);
    root.right.right = Node(110);

    initial = [];
    traversal(root, initial);
    print(initial);
    final = [];
    binarySearchTree(root);
    traversal(root, final);
    print(final);



