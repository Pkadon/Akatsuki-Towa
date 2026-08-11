label avg25272(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1211033)]' (**arg(1, 1211033))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211034)]' (**arg(2, 1211034))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1211035)]' (**arg(3, 1211035))
hide p2
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1211036)]' (**arg(4, 1211036))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211037)]' (**arg(5, 1211037))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1211038)]' (**arg(6, 1211038))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211039)]' (**arg(7, 1211039))
return "avg25272"