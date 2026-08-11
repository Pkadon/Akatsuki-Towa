label avg25227(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "fight_6025.ogg"
get_char('c0') '[convertstrid(1210807)]' (**arg(1, 1210807))
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210808)]' (**arg(2, 1210808))
hide p1
play sfx2 "other_7082.ogg"
get_char('c20173') '[convertstrid(1210809)]' (**arg(3, 1210809))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210810)]' (**arg(4, 1210810))
return "avg25227"