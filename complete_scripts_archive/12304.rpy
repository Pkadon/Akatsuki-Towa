label avg12304:
stop music

play music "ed7518.ogg"
scene avg_bg_010
window show
with fade_in
play sfx2 "common_select.ogg"
c10841 '[textdict[1133151]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1133152]]'
hide p2
$ update_portrait('oc001_01 24', 'p1', [r(-2), light], 5)
c13 '[textdict[1133153]]'
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
c10841 '[textdict[1133154]]'
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
c10841 '[textdict[1133155]]'
play music "ed7511.ogg"
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_c04_01.ogg"
c13 '[textdict[1133161]]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
play sfx2 "other_7086.ogg"
c10851 '[textdict[1133162]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [r_midback(-3), light], 5)
c23 '[textdict[1133163]]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
play sfx2 "other_7007.ogg"
c10851 '[textdict[1133164]]' with shake
hide p2
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
c43 '[textdict[1133165]]'
hide p4
$ update_portrait('sc046_01 4', 'p1004', [r(-5), light], 5)
play sfx2 "other_7029.ogg"
c10043 '[textdict[1133166]]'
$ update_portrait('sc046_01 4', 'p1004', [r(-5), dark], 5)
c10851 '[textdict[1133167]]'
hide p1004
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 5)
c43 '[textdict[1133168]]'
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
c10851 '[textdict[1133169]]'
hide p4
$ update_portrait('sc046_01 3', 'p1004', [r(-5), light], 5)
c10043 '[textdict[1133170]]'
hide p1004
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
play sfx2 "other_7004.ogg"
c33 '[textdict[1133171]]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
c10851 '[textdict[1133172]]' (what_size=(gui.text_size*1.2)) with shake
play music "ed7105.ogg"
scene avg_bg_070
$ update_portrait('sc046_01 5', 'p1004', [r(-5), light], 5)
with fade
c10043 '[textdict[1133173]]'
scene avg_bg_010
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
with fade
c31 '[textdict[1133174]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('sc046_01 2', 'p1004', [r(-5), r_shake, light], 5)
c10043 '[textdict[1133175]]'
$ update_portrait('sc046_01 2', 'p1004', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1133176]]'
hide p1004
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1133177]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro20.ogg"
c31 '[textdict[1133178]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1133179]]'
hide p3
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[textdict[1133180]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li09.ogg"
c41 '[textdict[1133181]]'
hide p1
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('sc046_01 5', 'p1004', [r(-5), light], 5)
c10043 '[textdict[1133182]]'
$ update_portrait('sc046_01 5', 'p1004', [r(-5), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1133183]]'
return