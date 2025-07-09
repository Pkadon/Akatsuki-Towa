label avg100104:
stop music

scene placeholderbackground
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
window show
with fade_in
c91 '[textdict[1218021]]'
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218022]]'
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218023]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218024]]'
menu:
    extend ""
    "[textdict[1218025]]":
        call avg100105
    "[textdict[1218026]]":
        call avg100106
    "[textdict[1218026]]":
        call avg100107
return