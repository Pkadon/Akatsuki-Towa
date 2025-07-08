label avg102721:
stop music

scene placeholderbackground
$ update_portrait('sc019_01 2', 'p27', [l(-18), light, flip], 6)
window show
with fade_in
c271 '[textdict[1219497]]'
hide p27
$ update_portrait('sc019_01 2', 'p27', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1219498]]'
hide p27
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219499]]'
menu:
    extend ""
    "[textdict[1219500]]":
        call avg102722
    "[textdict[1219501]]":
        call avg102723
    "[textdict[1219502]]":
        call avg102724
return