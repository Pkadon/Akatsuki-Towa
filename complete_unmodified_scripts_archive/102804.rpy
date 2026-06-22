label avg102804:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with fade_in
get_char('c281') '[convertstrid(1219724)]' (**arg(1, 1219724))
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219725)]' (**arg(2, 1219725))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1219726)]' (**arg(3, 1219726))
menu:
    extend ""
    '[convertstrid(1219727)]':
        call avg102805
    '[convertstrid(1219728)]':
        call avg102806
    '[convertstrid(1219729)]':
        call avg102807
return