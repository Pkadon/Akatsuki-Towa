label avg101525:

stop music
scene placeholderbackground
$ update_portrait('sc007_01 6', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with fade_in
get_char('c151') '[convertstrid(1221331)]' (**arg(1, 1221331))
$ update_portrait('sc007_01 6', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221332)]' (**arg(2, 1221332))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1221333)]' (**arg(3, 1221333))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221334)]' (**arg(4, 1221334))
menu:
    extend ""
    '[convertstrid(1221335)]':
        call avg101526
    '[convertstrid(1221336)]':
        call avg101527
    '[convertstrid(1221337)]':
        call avg101528
return