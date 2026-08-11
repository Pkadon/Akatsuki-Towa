label avg101625(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 3', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221596)]' (**arg(1, 1221596))
$ update_portrait('sc008_01 3', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221597)]' (**arg(2, 1221597))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1221598)]' (**arg(3, 1221598))
menu:
    extend ""
    '[convertstrid(1221599)]':
        call avg101626
    '[convertstrid(1221600)]':
        call avg101627
    '[convertstrid(1221601)]':
        call avg101628
return _return