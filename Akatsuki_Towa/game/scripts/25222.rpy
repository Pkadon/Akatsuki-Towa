label avg25222(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20183')
window show
with trans
play sfx2 "other_7079.ogg"
get_char('c20183') '[convertstrid(1210772)]' (**arg(1, 1210772))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210773)]' (**arg(2, 1210773))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210774)]' (**arg(3, 1210774))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210775)]' (**arg(4, 1210775))
hide p1
play sfx2 "other_7031.ogg"
get_char('c20183') '[convertstrid(1210776)]' (**arg(5, 1210776))
play sfx2 "other_7080.ogg"
get_char('c20163') '[convertstrid(1210777)]' (**arg(6, 1210777))
play sfx2 "other_7079.ogg"
get_char('c20183') '[convertstrid(1210778)]' (**arg(7, 1210778))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210779)]' (**arg(8, 1210779))
return "avg25222"