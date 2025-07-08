label avg24521:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1206033]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1206034]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1206035]]'
return