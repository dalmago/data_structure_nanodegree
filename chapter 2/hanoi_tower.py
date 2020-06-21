def tower_of_Hanoi_recur(num_disks, source, auxiliary, destination):
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    tower_of_Hanoi_recur(num_disks - 1, source, destination, auxiliary)
    tower_of_Hanoi_recur(1, source, auxiliary, destination)
    tower_of_Hanoi_recur(num_disks - 1, auxiliary, source, destination)

def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    """
    tower_of_Hanoi_recur(num_disks, 'S', 'A', 'D')

tower_of_Hanoi(5)
