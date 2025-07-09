label avg102704:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1219451]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 3', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219452]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219453]]'
menu:
    extend ""
    "[textdict[1219454]]":
        call avg102705
    "[textdict[1219455]]":
        call avg102706
    "[textdict[1219456]]":
        call avg102707
return