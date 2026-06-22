label avg1035:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with fade_in
get_char('c601') '[convertstrid(2100584)]' (**arg(1, 2100584))
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100585)]' (**arg(2, 2100585))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100586)]' (**arg(3, 2100586))
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100587)]' (**arg(4, 2100587))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100588)]' (**arg(5, 2100588))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100589)]' (**arg(6, 2100589))
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100590)]' (**arg(7, 2100590))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100591)]' (**arg(8, 2100591))
return