label avg12546:

$ play_music("ED6105.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1152959)]' (**arg(1, 1152959))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152960)]' (**arg(2, 1152960))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152961)]' (**arg(3, 1152961))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152962)]' (**arg(4, 1152962))
return