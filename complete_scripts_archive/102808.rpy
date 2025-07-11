label avg102808:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1219734]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 5', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1219735]]'
$ update_portrait('sc020_01 5', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1219736]]'
menu:
    extend ""
    "[textdict[1219737]]":
        call avg102809
    "[textdict[1219738]]":
        call avg102810
    "[textdict[1219739]]":
        call avg102811
return