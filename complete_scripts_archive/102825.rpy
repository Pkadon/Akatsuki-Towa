label avg102825:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with fade_in
c281 '[convertstrid(1219788)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1219789)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1219790)]'
menu:
    extend ""
    "[textdict[1219791]]":
        call avg102826
    "[textdict[1219792]]":
        call avg102827
    "[textdict[1219793]]":
        call avg102828
return