label avg10333:

$ play_music("ed7105.ogg")
scene avg_bg_003
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(1130999)]' (**arg(1, 1130999))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 12', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1131000)]' (**arg(2, 1131000))
hide p4
$ update_portrait('oc005_01 12', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1131001)]' (**arg(3, 1131001))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131002)]' (**arg(4, 1131002))
return