s_hh, s_mm = map(int, input().split(':'))
t_hh, t_mm = map(int, input().split(':'))


hh = list(range(0,24))
mm = list(range(0,60))

if s_mm-t_mm < 0:
	t_hh += 1
print(str(hh[s_hh-t_hh]).zfill(2) + ':' + str(mm[s_mm-t_mm]).zfill(2))