label avg102708:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
$ update_narrator('c271')
window show
with fade_in
c271 '[textdict[1219461]]'
$ update_portrait('sc019_01 1', 'p27', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1219462]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219463]]'
menu:
    extend ""
    "[textdict[1219464]]":
        call avg102709
    "[textdict[1219465]]":
        call avg102710
    "[textdict[1219466]]":
        call avg102711
return