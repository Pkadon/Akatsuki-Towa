label avg25174(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1210556)]' (**arg(1, 1210556))
hide p1
get_char('c20133') '[convertstrid(1210557)]' (**arg(2, 1210557))
get_char('c20133') '[convertstrid(1210558)]' (**arg(3, 1210558))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210559)]' (**arg(4, 1210559))
hide p2
get_char('c20133') '[convertstrid(1210560)]' (**arg(5, 1210560))
return "avg25174"