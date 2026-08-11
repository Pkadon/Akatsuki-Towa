label avg25041(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210105)]' (**arg(1, 1210105))
hide p2
$ update_portrait('uc001_02 1', 'p2001', [mid(6), light], 6)
get_char('c20013') '[convertstrid(1210106)]' (**arg(2, 1210106))
return "avg25041"