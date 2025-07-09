label avg12581:
stop music

play music "ed7151.ogg"
scene avg_bg_080
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1155400]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1155401]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l_entrance(-17), light, flip], 6)
c291 '[textdict[1155402]]'
hide p2
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1155403]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 3', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155404]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155405]]'
hide p3
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1155406]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155407]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155408]]'
hide p4
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[textdict[1155409]]'
return