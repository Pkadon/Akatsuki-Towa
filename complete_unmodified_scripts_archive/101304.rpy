label avg101304(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with trans
get_char('c131') '[convertstrid(1220959)]' (**arg(1, 1220959))
$ update_portrait('sc005_01 2', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220960)]' (**arg(2, 1220960))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1220961)]' (**arg(3, 1220961))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1220962)]' (**arg(4, 1220962))
menu:
    extend ""
    '[convertstrid(1220963)]':
        call avg101305
    '[convertstrid(1220964)]':
        call avg101306
    '[convertstrid(1220965)]':
        call avg101307
return _return