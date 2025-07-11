label avg106021:

stop music
scene placeholderbackground
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
window show
with fade_in
c601 '[textdict[1219108]]'
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219109]]'
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1219110]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219111]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219112]]'
menu:
    extend ""
    "[textdict[1219113]]":
        call avg106022
    "[textdict[1219114]]":
        call avg106023
    "[textdict[1219115]]":
        call avg106024
return