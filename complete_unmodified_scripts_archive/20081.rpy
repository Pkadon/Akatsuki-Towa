label avg20081(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1004268)]' (**arg(1, 1004268))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1004269)]' (**arg(2, 1004269))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1004270)]' (**arg(3, 1004270))
hide p1
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1004271)]' (**arg(4, 1004271))
hide p3
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1004272)]' (**arg(5, 1004272))
hide p2
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1004273)]' (**arg(6, 1004273))
hide p3
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1004274)]' (**arg(7, 1004274))
hide p1
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1004275)]' (**arg(8, 1004275))
hide p3
$ update_portrait('oc004_01 13', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1004276)]' (**arg(9, 1004276))
hide p4
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1004277)]' (**arg(10, 1004277))
return "avg20081"