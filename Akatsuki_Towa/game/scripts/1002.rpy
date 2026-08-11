label avg1002(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2100030)]' (**arg(1, 2100030))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100031)]' (**arg(2, 2100031))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100032)]' (**arg(3, 2100032))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100033)]' (**arg(4, 2100033))
menu:
    extend ""
    '[convertstrid(2100034)]':
        call avg1003
    '[convertstrid(2100035)]':
        call avg1004
    '[convertstrid(2100036)]':
        call avg1005
return _return