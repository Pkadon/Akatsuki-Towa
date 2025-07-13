label avg106008:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1219067]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219068]]'
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1219069]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 5', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1219070]]'
menu:
    extend ""
    "[textdict[1219071]]":
        call avg106009
    "[textdict[1219072]]":
        call avg106010
    "[textdict[1219073]]":
        call avg106011
return