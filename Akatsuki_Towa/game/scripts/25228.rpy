label avg25228(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c23') '[convertstrid(1210811)]' (**arg(1, 1210811))
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210812)]' (**arg(2, 1210812))
return "avg25228"