class Group(object):
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
    if user in group.users:  # O(N)
        return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True

    return False

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
