label avg101625:
stop music

scene placeholderbackground
$ update_portrait('sc008_01 3', 'p16', [l(-18), light, flip], 6)
window show
with fade_in
c161 '[textdict[1221596]]'
hide p16
$ update_portrait('sc008_01 3', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1221597]]'
hide p16
hide p1
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1221598]]'
menu:
    extend ""
    "[textdict[1221599]]":
        call avg101626
    "[textdict[1221600]]":
        call avg101627
    "[textdict[1221601]]":
        call avg101628
return