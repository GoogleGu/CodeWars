import copy
class Solution:
    def FindPath(self, root, expectNumber):
        current_path = []
        all_path = []
        all_path = self.find(root, expectNumber, current_path, all_path)
        return all_path
        ## return self.shell_sort(all_path)

    def find(self, root, expect_number, current_path, all_path):
        if root is None:
            return all_path
        current_path.append(root.val)
        expect_number = expect_number-root.val
        if expect_number == 0 and root.left is None and root.right is None:
            all_path.append(copy.deepcopy(current_path))
        self.find(root.left, expect_number, current_path, all_path)
        self.find(root.right, expect_number, current_path, all_path)
        # 到叶节点后往后退一步
        # 如果已经到叶节点，并且该节点为左子树
        # 正好符合条件，填入，现在要判断该节点的父节点的右子树是否符合条件
        # 要后退一步，所以要弹出最后最后一位
        current_path.pop()
        return all_path

    def shell_sort(self, value):
        n = len(value)
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                for j in range(i, gap-1, -gap):
                    if len(value[j]) > len(value[j-gap]):
                        value[j], value[j-gap] = value[j-gap], value[j]
                    else:
                        break
            gap //= 2
        return value
