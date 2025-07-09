label avg12831:
stop music

play music "ed7511.ogg"
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1185406]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1185407]]'
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1185408]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
c43 '[textdict[1185409]]'
hide p16
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1185410]]'
return