from xplit import get_fail_list as xplit_get_fail_list
from plitkaking import get_fail_list as plitkaking_get_fail_list
from megaceramic import get_fail_list as megaceramic_get_fail_list
from save_csv import save_to_csv


xplit_fail = xplit_get_fail_list()
plitkaking_fail = plitkaking_get_fail_list()
megaceramic_fail = megaceramic_get_fail_list()
fail = xplit_fail + plitkaking_fail + megaceramic_fail
save_to_csv(fail)
