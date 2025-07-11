label avg12114:

play music "ed7117.ogg"
scene avg_bg_017
window show
with fade_in
play sfx2 "other_7048.ogg"
c9573 '[textdict[1128181]]'
play sfx2 "other_7091.ogg"
c9573 '[textdict[1128182]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
c11 '[textdict[1128183]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128184]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
c9573 '[textdict[1128185]]'
hide p2
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128186]]'
hide p3
c0 '[textdict[1128187]]'
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128188]]'
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 6)
c9573 '[textdict[1128189]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128190]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
c9573 '[textdict[1128191]]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7004.ogg"
c21 '[textdict[1128192]]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c21 '[textdict[1128193]]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
c9573 '[textdict[1128194]]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
c31 '[textdict[1128195]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
c9573 '[textdict[1128196]]'
c9573 '[textdict[1128197]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128198]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128199]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128200]]'
hide p2
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1128201]]'
return