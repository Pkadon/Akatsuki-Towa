label avg25005(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7079.ogg"
get_char('c23') '[convertstrid(1210007)]' (**arg(1, 1210007))
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_sc01_01.ogg"
get_char('c13') '[convertstrid(1210008)]' (**arg(2, 1210008))
return "avg25005"