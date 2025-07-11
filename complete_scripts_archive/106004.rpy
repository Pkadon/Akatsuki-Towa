label avg106004:

stop music
scene placeholderbackground
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
window show
with fade_in
c601 '[textdict[1219056]]'
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1219057]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219058]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219059]]'
menu:
    extend ""
    "[textdict[1219060]]":
        call avg106005
    "[textdict[1219061]]":
        call avg106006
    "[textdict[1219062]]":
        call avg106007
return