from sites.xplit import get_fail_list as xplit_get_fail_list
from sites.megaceramic import get_fail_list as megaceramic_get_fail_list


def get_fail():
    xplit_fail = xplit_get_fail_list()
    megaceramic_fail = megaceramic_get_fail_list()
    fail = xplit_fail + megaceramic_fail
    return fail
