# -*- coding: utf-8 -*-
# problem_4.py
# Author: Matheus Dal Mago
# 2020


class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Check group
    if user in group.users:  # O(N)
        return True

    # Check subgroups
    for sub_group in group.groups:  # O(N)
        if is_user_in_group(user, sub_group):
            return True

    return False


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("sub_child_user", parent))  # Should be True
    print(is_user_in_group("sub_child_user", child))  # Should be True
    print(is_user_in_group("sub_child_user", sub_child))  # Should be True

    child_user = "child_user"
    child.add_user(child_user)

    print(is_user_in_group(child_user, child))  # Should be True
    print(is_user_in_group(child_user, sub_child))  # Should be False

    print(is_user_in_group("another_user", parent))  # Should be False

    parent2 = Group("sith")
    user2 = "luke"
    user3 = "anakin"
    print(is_user_in_group(user2, parent2))  # False because the group has no user

    child2 = Group("skywalker")
    parent2.add_group(child2)
    child2.add_user(user3)

    print(is_user_in_group(user3, parent2))  # True. Anakin is in Skywalker, which is part of Sith.
