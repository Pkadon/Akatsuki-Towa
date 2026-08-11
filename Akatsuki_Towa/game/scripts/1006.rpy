label avg1006(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with trans
get_char('c561') '[convertstrid(2100084)]' (**arg(1, 2100084))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100085)]' (**arg(2, 2100085))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100086)]' (**arg(3, 2100086))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100087)]' (**arg(4, 2100087))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100088)]' (**arg(5, 2100088))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100089)]' (**arg(6, 2100089))
menu:
    extend ""
    '[convertstrid(2100091)]':
        call avg1007
    '[convertstrid(2100092)]':
        call avg1008
    '[convertstrid(2100093)]':
        call avg1009
return _return