label avg101521:
stop music

scene placeholderbackground
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
window show
with fade_in
c151 '[textdict[1221319]]'
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1221320]]'
hide p15
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1221321]]'
hide p15
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1221322]]'
hide p1
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1221323]]'
menu:
    extend ""
    "[textdict[1221324]]":
        call avg101522
    "[textdict[1221325]]":
        call avg101523
    "[textdict[1221326]]":
        call avg101524
return