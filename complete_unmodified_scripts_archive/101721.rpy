label avg101721(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1221932)]' (**arg(1, 1221932))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(1221933)]' (**arg(2, 1221933))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221934)]' (**arg(3, 1221934))
menu:
    extend ""
    '[convertstrid(1221935)]':
        call avg101722
    '[convertstrid(1221936)]':
        call avg101723
    '[convertstrid(1221937)]':
        call avg101724
return _return