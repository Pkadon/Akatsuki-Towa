label avg25156(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1210496)]' (**arg(1, 1210496))
hide p1
get_char('c6123') '[convertstrid(1210497)]' (**arg(2, 1210497))
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1210498)]' (**arg(3, 1210498))
return "avg25156"