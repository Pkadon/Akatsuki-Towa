label avg12520:
stop music

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
window show
with fade_in
c131 '[textdict[1151252]]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1151253]]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1151254]]'
hide p3
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151255]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151256]]'
return