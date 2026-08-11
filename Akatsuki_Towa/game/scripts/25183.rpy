label avg25183(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210597)]' (**arg(1, 1210597))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210598)]' (**arg(2, 1210598))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210599)]' (**arg(3, 1210599))
hide p2
get_char('c6123') '[convertstrid(1210600)]' (**arg(4, 1210600))
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
get_char('c13') '[convertstrid(1210601)]' (**arg(5, 1210601))
return "avg25183"