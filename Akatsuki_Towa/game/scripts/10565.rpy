label avg10565(trans=fade_in):

$ play_music("ED6303.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1154337)]' (**arg(1, 1154337))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6009.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c21') '[convertstrid(1154338)]' (**arg(2, 1154338))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154339)]' (**arg(3, 1154339))
hide p3
hide p1
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
$ update_narrator('c12121')
with fade
get_char('c12121') '[convertstrid(1154340)]' (**arg(4, 1154340))
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7085.ogg"
get_char('c23') '[convertstrid(1154341)]' (**arg(5, 1154341))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st056_01 2', 'p1212', [l(-6), l_shake, light, flip], 6)
get_char('c12121') '[convertstrid(1154342)]' (**arg(6, 1154342))
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
get_char('c12121') '[convertstrid(1154343)]' (**arg(7, 1154343))
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154344)]' (**arg(8, 1154344))
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154345)]' (**arg(9, 1154345))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
get_char('c12121') '[convertstrid(1154346)]' (**arg(10, 1154346))
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1154347)]' (**arg(11, 1154347))
hide p1212
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154348)]' (**arg(12, 1154348))
hide p4
hide p2
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1154349)]' (**arg(13, 1154349))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154350)]' (**arg(14, 1154350))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154351)]' (**arg(15, 1154351))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154352)]' (**arg(16, 1154352))
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1154353)]' (**arg(17, 1154353))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154354)]' (**arg(18, 1154354))
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154355)]' (**arg(19, 1154355))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154356)]' (**arg(20, 1154356))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154357)]' (**arg(21, 1154357))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1154358)]' (**arg(22, 1154358))
return "avg10565"