label avg25049(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210125)]' (**arg(1, 1210125))
hide p2
$ update_portrait('uc001_02 2', 'p2002', [mid(6), light], 6)
get_char('c20023') '[convertstrid(1210126)]' (**arg(2, 1210126))
hide p2002
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210127)]' (**arg(3, 1210127))
hide p1
$ update_portrait('uc001_02 1', 'p2002', [mid(6), light], 6)
get_char('c20023') '[convertstrid(1210128)]' (**arg(4, 1210128))
$ update_portrait('uc001_02 3', 'p2002', [mid(6), light], 6)
get_char('c20023') '[convertstrid(1210129)]' (**arg(5, 1210129))
hide p2002
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210130)]' (**arg(6, 1210130))
return "avg25049"