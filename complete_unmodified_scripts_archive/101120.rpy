label avg101120(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220440)]' (**arg(1, 1220440))
hide p1
$ update_portrait('sc003_01 1', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220441)]' (**arg(2, 1220441))
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220442)]' (**arg(3, 1220442))
$ update_portrait('sc003_01 3', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220443)]' (**arg(4, 1220443))
hide p11
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220444)]' (**arg(5, 1220444))
return "avg101120"