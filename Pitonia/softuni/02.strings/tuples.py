ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия', 'facebook']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

ivan_s = set(ivan)
maria_s = set(maria)
in_cmn = set()

for i in ivan_s:
	if i in maria_s:
		in_cmn.add(i)
print(in_cmn)
input("Enter to proceed")