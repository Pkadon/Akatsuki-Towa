label avg101704(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with trans
get_char('c171') '[convertstrid(1221883)]' (**arg(1, 1221883))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221884)]' (**arg(2, 1221884))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(1221885)]' (**arg(3, 1221885))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221886)]' (**arg(4, 1221886))
menu:
    extend ""
    '[convertstrid(1221887)]':
        call avg101705
    '[convertstrid(1221888)]':
        call avg101706
    '[convertstrid(1221889)]':
        call avg101707
return _return