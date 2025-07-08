label avg102025:
stop music

scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
window show
with fade_in
c201 '[textdict[1218695]]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1218696]]'
hide p20
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
c201 '[textdict[1218697]]'
menu:
    extend ""
    "[textdict[1218698]]":
        call avg102026
    "[textdict[1218699]]":
        call avg102027
    "[textdict[1218700]]":
        call avg102028
return