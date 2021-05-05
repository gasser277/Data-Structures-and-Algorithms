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
    current_users=group.users
    current_groups=group.groups
    for i in current_users:
        if i == user:
            print(user, " user is in group: ",group)
            return True
        else:
            for i in current_groups:
                if i==group:
                    is_user_in_group(user,i)
                else: return False


#Test case1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group(sub_child_user,sub_child))#Expected True
print("//////////////////////")
#Test case2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group("sub_child_user2",sub_child))#Expected False
print("//////////////////////")
#Test case3
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group(None,sub_child))#Expected False
print("//////////////////////")
