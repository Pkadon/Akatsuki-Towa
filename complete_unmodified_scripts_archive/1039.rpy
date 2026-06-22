label avg1039:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
$ update_narrator('c581')
window show
with fade_in
get_char('c581') '[convertstrid(2100620)]' (**arg(1, 2100620))
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100621)]' (**arg(2, 2100621))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
get_char('c581') '[convertstrid(2100622)]' (**arg(3, 2100622))
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100623)]' (**arg(4, 2100623))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
get_char('c581') '[convertstrid(2100624)]' (**arg(5, 2100624))
hide p2
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100625)]' (**arg(6, 2100625))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
get_char('c581') '[convertstrid(2100626)]' (**arg(7, 2100626))
return