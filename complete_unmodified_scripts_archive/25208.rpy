label avg25208(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c23') '[convertstrid(1210718)]' (**arg(1, 1210718))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210719)]' (**arg(2, 1210719))
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210720)]' (**arg(3, 1210720))
return "avg25208"