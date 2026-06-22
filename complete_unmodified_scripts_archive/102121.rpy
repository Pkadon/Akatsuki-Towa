label avg102121:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with fade_in
get_char('c211') '[convertstrid(1218869)]' (**arg(1, 1218869))
$ update_portrait('sc013_01 3', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218870)]' (**arg(2, 1218870))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1218871)]' (**arg(3, 1218871))
menu:
    extend ""
    '[convertstrid(1218872)]':
        call avg102122
    '[convertstrid(1218873)]':
        call avg102123
    '[convertstrid(1218874)]':
        call avg102124
return