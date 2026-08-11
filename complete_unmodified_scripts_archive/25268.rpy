label avg25268(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1211006)]' (**arg(1, 1211006))
hide p2
get_char('c20133') '[convertstrid(1211007)]' (**arg(2, 1211007))
return "avg25268"