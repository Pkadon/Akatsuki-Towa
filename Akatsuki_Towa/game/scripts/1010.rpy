label avg1010:

$ play_music("ed7106.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
get_char('c561') '[convertstrid(2100125)]' (**arg(1, 2100125))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100126)]' (**arg(2, 2100126))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100127)]' (**arg(3, 2100127))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100128)]' (**arg(4, 2100128))
menu:
    extend ""
    '[convertstrid(2100129)]':
        call avg1011
    '[convertstrid(2100130)]':
        call avg1012
    '[convertstrid(2100131)]':
        call avg1013
return