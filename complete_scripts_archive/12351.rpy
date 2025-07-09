label avg12351:
stop music

play music "ed9999.ogg"
scene avg_bg_074
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1133578]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1133579]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133580]]'
hide p2
$ update_portrait('st032_01 5', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
c13 '[textdict[1133581]]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 6', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133582]]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133583]]'
$ update_portrait('st032_01 1', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133584]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133585]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 4', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133586]]'
hide p1
$ update_portrait('st032_01 4', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1133587]]'
hide p2
$ update_portrait('st032_01 4', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1133588]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 2', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133589]]'
hide p1
$ update_portrait('st032_01 2', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1133590]]'
hide p2
$ update_portrait('st032_01 2', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 5)
play sfxvoice "bcv_oc003_com_01.ogg"
c33 '[textdict[1133591]]'
$ update_portrait('oc003_01 14', 'p3', [r(-6), dark], 5)
$ update_portrait('st032_01 6', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133592]]'
hide p3
$ update_portrait('st032_01 6', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1133593]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 4', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133594]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133595]]'
hide p2
$ update_portrait('st032_01 1', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1133596]]'
hide p231
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
c41 '[textdict[1133597]]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
c23 '[textdict[1133598]]'
hide p4
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133599]]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133600]]'
hide p2
$ update_portrait('st032_01 5', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1133601]]'
hide p231
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
play sfx2 "common_quest.ogg"
play sfxvoice "avg_vocal_li05.ogg"
c41 '[textdict[1133602]]'
return