label avg102001(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218618)]' (**arg(1, 1218618))
hide p20
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218619)]' (**arg(2, 1218619))
hide p1
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218620)]' (**arg(3, 1218620))
$ update_portrait('sc012_01 4', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218621)]' (**arg(4, 1218621))
hide p20
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218622)]' (**arg(5, 1218622))
hide p1
$ update_portrait('sc012_01 5', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218623)]' (**arg(6, 1218623))
return "avg102001"