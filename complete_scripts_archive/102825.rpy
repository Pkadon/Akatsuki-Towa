label avg102825:
stop music

scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
window show
with fade_in
c281 '[textdict[1219788]]'
hide p28
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1219789]]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1219790]]'
menu:
    extend ""
    "[textdict[1219791]]":
        call avg102826
    "[textdict[1219792]]":
        call avg102827
    "[textdict[1219793]]":
        call avg102828
return