label avg101103(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 2', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220392)]' (**arg(1, 1220392))
hide p11
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220393)]' (**arg(2, 1220393))
hide p1
$ update_portrait('sc003_01 1', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220394)]' (**arg(3, 1220394))
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220395)]' (**arg(4, 1220395))
hide p11
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220396)]' (**arg(5, 1220396))
hide p1
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220397)]' (**arg(6, 1220397))
return "avg101103"