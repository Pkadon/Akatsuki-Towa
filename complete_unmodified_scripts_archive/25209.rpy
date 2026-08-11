label avg25209(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch28.ogg"
get_char('c23') '[convertstrid(1210721)]' (**arg(1, 1210721))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfx2 "other_7043.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210722)]' (**arg(2, 1210722))
hide p1
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6020.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1210723)]' (**arg(3, 1210723))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210724)]' (**arg(4, 1210724))
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5002.ogg"
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c23') '[convertstrid(1210725)]' (**arg(5, 1210725))
return "avg25209"