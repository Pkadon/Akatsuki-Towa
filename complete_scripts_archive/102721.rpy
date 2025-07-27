label avg102721:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 2', 'p27', [l(-18), light, flip], 6)
$ update_narrator('c271')
window show
with fade_in
c271 '[convertstrid(1219497)]'
$ update_portrait('sc019_01 2', 'p27', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1219498)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
c271 '[convertstrid(1219499)]'
menu:
    extend ""
    "[textdict[1219500]]":
        call avg102722
    "[textdict[1219501]]":
        call avg102723
    "[textdict[1219502]]":
        call avg102724
return