label avg102925:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1219964]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219965]]'
$ update_portrait('sc021_01 3', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219966]]'
menu:
    extend ""
    "[textdict[1219967]]":
        call avg102926
    "[textdict[1219968]]":
        call avg102927
    "[textdict[1219969]]":
        call avg102928
return