label avg101504(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with trans
get_char('c151') '[convertstrid(1221271)]' (**arg(1, 1221271))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221272)]' (**arg(2, 1221272))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1221273)]' (**arg(3, 1221273))
menu:
    extend ""
    '[convertstrid(1221274)]':
        call avg101505
    '[convertstrid(1221275)]':
        call avg101506
    '[convertstrid(1221276)]':
        call avg101507
return _return