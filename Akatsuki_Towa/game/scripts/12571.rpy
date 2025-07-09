label avg12571:
stop music

play music "ED6200.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1155153]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1155154]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155155]]'
return