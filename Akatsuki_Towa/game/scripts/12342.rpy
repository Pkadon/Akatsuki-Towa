label avg12342:
stop music

play music "ed7120.ogg"
scene avg_bg_070
window show
with fade_in
play sfx2 "other_7021.ogg"
c0 '[textdict[1133506]]'
scene avg_bg_055
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
with fade
c10071 '[textdict[1133507]]'
hide p1007
$ update_portrait('st053_01 1', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1133508]]'
hide p1007
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 5', 'p1007', [l(-12), light, flip], 6)
c10071 '[textdict[1133509]]'
hide p1007
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7021.ogg"
c10901 '[textdict[1133510]]'
hide p1
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
c13 '[textdict[1133511]]'
hide p1
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
c10911 '[textdict[1133512]]'
hide p1
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133513]]'
hide p1007
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
c10901 '[textdict[1133514]]'
hide p1007
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
c10911 '[textdict[1133515]]'
hide p1007
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro11.ogg"
c33 '[textdict[1133516]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133517]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133518]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c10901 '[textdict[1133519]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133520]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c10911 '[textdict[1133521]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c10911 '[textdict[1133522]]'
stop music
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c21 '[textdict[1133523]]'
play music "ed7151.ogg"
hide p1
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1133524]]'
hide p1
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1133525]]'
hide p2
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133526]]'
hide p1
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li07.ogg"
c43 '[textdict[1133527]]'
hide p4
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 5)
c43 '[textdict[1133528]]'
hide p4
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 5)
c43 '[textdict[1133529]]'
hide p4
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 5)
c43 '[textdict[1133530]]'
hide p4
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li30.ogg"
c43 '[textdict[1133531]]'
hide p2
hide p4
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
c21 '[textdict[1133532]]' (what_size=(gui.text_size*1.4))
hide p4
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 5)
play sfx2 "other_7057.ogg"
play sfxvoice "bcv_oc004_hurt_02.ogg"
c43 '[textdict[1133533]]' (what_size=(gui.text_size*1.2)) with shake
hide p4
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li11.ogg"
c43 '[textdict[1133534]]'
hide p2
hide p4
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133535]]'
hide p4
hide p2
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 5)
c43 '[textdict[1133536]]'
hide p4
hide p2
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133537]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1133538]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1133539]]'
hide p4
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1133540]]'
stop music
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "other_7077.ogg"
c13 '[textdict[1133541]]'
hide p3
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
c21 '[textdict[1133542]]'
hide p1
hide p2
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1133543]]'
hide p3
hide p2
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1133544]]'
hide p2
hide p1
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133545]]'
play music "ed7511.ogg"
hide p2
hide p1
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7080.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1133546]]'
hide p1
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 5)
c33 '[textdict[1133547]]'
hide p3
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1133548]]'
hide p1
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 5)
c43 '[textdict[1133549]]'
hide p2
hide p4
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133550]]'
return