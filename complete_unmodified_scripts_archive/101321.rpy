label avg101321(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1221012)]' (**arg(1, 1221012))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221013)]' (**arg(2, 1221013))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1221014)]' (**arg(3, 1221014))
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1221015)]' (**arg(4, 1221015))
$ update_portrait('sc005_01 2', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221016)]' (**arg(5, 1221016))
menu:
    extend ""
    '[convertstrid(1221017)]':
        call avg101322
    '[convertstrid(1221018)]':
        call avg101323
    '[convertstrid(1221019)]':
        call avg101324
return _return