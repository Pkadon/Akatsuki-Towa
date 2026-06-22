label avg10336:

$ play_music("ed7105.ogg")
scene avg_bg_003
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(1130999)]' (**arg(1, 1130999))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131024)]' (**arg(2, 1131024))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131025)]' (**arg(3, 1131025))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131026)]' (**arg(4, 1131026))
hide p2
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131027)]' (**arg(5, 1131027))
hide p4
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131028)]' (**arg(6, 1131028))
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131029)]' (**arg(7, 1131029))
menu:
    extend ""
    '[convertstrid(1131030)]':
        call avg10338
    '[convertstrid(1131031)]':
        call avg10339
return