label avg25193(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210647)]' (**arg(1, 1210647))
hide p2
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210648)]' (**arg(2, 1210648))
hide p1
get_char('c20133') '[convertstrid(1210649)]' (**arg(3, 1210649))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210650)]' (**arg(4, 1210650))
hide p2
get_char('c20133') '[convertstrid(1210651)]' (**arg(5, 1210651))
return "avg25193"