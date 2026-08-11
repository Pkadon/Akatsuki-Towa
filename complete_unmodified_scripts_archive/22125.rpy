label avg22125(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1128249)]' (**arg(1, 1128249))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128250)]' (**arg(2, 1128250))
return "avg22125"