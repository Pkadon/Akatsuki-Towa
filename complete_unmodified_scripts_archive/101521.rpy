label avg101521(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with trans
get_char('c151') '[convertstrid(1221319)]' (**arg(1, 1221319))
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221320)]' (**arg(2, 1221320))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1221321)]' (**arg(3, 1221321))
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1221322)]' (**arg(4, 1221322))
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221323)]' (**arg(5, 1221323))
menu:
    extend ""
    '[convertstrid(1221324)]':
        call avg101522
    '[convertstrid(1221325)]':
        call avg101523
    '[convertstrid(1221326)]':
        call avg101524
return _return