label avg25058(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210167)]' (**arg(1, 1210167))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210168)]' (**arg(2, 1210168))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210169)]' (**arg(3, 1210169))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1210170)]' (**arg(4, 1210170))
return "avg25058"