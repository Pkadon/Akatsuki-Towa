label avg10661:

$ play_music("ed9999.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1165584)]' (**arg(1, 1165584))
scene avg_bg_001
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
with fade
get_char('c161') '[convertstrid(1165585)]' (**arg(2, 1165585))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165586)]' (**arg(3, 1165586))
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165587)]' (**arg(4, 1165587))
hide p16
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165588)]' (**arg(5, 1165588))
hide p2
hide p1
get_char('c0') '[convertstrid(1165589)]' (**arg(6, 1165589))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165590)]' (**arg(7, 1165590))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165591)]' (**arg(8, 1165591))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165592)]' (**arg(9, 1165592))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165593)]' (**arg(10, 1165593))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165594)]' (**arg(11, 1165594))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1165595)]' (**arg(12, 1165595))
return