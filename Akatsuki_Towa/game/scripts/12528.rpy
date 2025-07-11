label avg12528:

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
window show
with fade_in
c161 '[textdict[1151522]]'
$ update_portrait('sc008_01 1', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1151523]]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1151524]]'
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151525]]'
hide p16
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li15.ogg"
c41 '[textdict[1151526]]'
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1151527]]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151528]]'
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[textdict[1151529]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151530]]'
hide p13
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1151531]]'
hide p3
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1151532]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1151533]]'
return