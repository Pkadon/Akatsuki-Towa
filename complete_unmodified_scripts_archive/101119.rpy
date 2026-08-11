label avg101119(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220434)]' (**arg(1, 1220434))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220435)]' (**arg(2, 1220435))
hide p1
$ update_portrait('sc003_01 1', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220436)]' (**arg(3, 1220436))
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220437)]' (**arg(4, 1220437))
hide p11
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220438)]' (**arg(5, 1220438))
return "avg101119"