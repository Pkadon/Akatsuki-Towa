label avg101608:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
window show
with fade_in
c161 '[textdict[1221549]]'
$ update_portrait('sc008_01 1', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1221550]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1221551]]'
menu:
    extend ""
    "[textdict[1221552]]":
        call avg101609
    "[textdict[1221553]]":
        call avg101610
    "[textdict[1221554]]":
        call avg101611
return