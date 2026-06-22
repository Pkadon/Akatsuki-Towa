label avg101608:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with fade_in
get_char('c161') '[convertstrid(1221549)]' (**arg(1, 1221549))
$ update_portrait('sc008_01 1', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221550)]' (**arg(2, 1221550))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1221551)]' (**arg(3, 1221551))
menu:
    extend ""
    '[convertstrid(1221552)]':
        call avg101609
    '[convertstrid(1221553)]':
        call avg101610
    '[convertstrid(1221554)]':
        call avg101611
return