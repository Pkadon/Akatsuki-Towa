label avg19011:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1216095)]' (**arg(1, 1216095, size=(0.9)))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216096)]' (**arg(2, 1216096, size=(0.9)))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216097)]' (**arg(3, 1216097, size=(0.9)))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216098)]' (**arg(4, 1216098, size=(0.9)))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216099)]' (**arg(5, 1216099, size=(0.9)))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216100)]' (**arg(6, 1216100, size=(0.9)))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216101)]' (**arg(7, 1216101, size=(0.9)))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216102)]' (**arg(8, 1216102, size=(0.9)))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216103)]' (**arg(9, 1216103, size=(0.9)))
hide p56
hide p2
get_char('c0') '[convertstrid(1216104)]' (**arg(10, 1216104, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216105)]' (**arg(11, 1216105, size=(0.9)))
hide p56
get_char('c0') '[convertstrid(1216106)]' (**arg(12, 1216106, size=(0.9)))
get_char('c0') '[convertstrid(1216107)]' (**arg(13, 1216107, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216108)]':
        call avg19012
    '[convertstrid(1216109)]':
        call avg19013
    '[convertstrid(1216110)]':
        call avg19014
return