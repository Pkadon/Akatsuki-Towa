label avg12583:

play music "ed7151.ogg"
scene avg_bg_080
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
window show
with fade_in
c291 '[textdict[1155427]]'
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155428]]'
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[textdict[1155429]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1155430]]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155431]]'
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155432]]'
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155433]]'
return