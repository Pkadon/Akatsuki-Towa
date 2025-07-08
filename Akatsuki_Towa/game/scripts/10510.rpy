label avg10510:
stop music

play music "ED6300.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[1150488]]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1150489]]'
return