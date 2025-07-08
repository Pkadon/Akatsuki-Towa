label avg12343:
stop music

play music "ed7151.ogg"
scene avg_bg_055
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
window show
with fade_in
play sfx2 "other_7057.ogg"
c33 '[textdict[1133551]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1133552]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 2', 'p1007', [l(-12), light, flip], 6)
c10071 '[textdict[1133553]]'
hide p1
hide p1007
$ update_portrait('st053_01 2', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 5)
c43 '[textdict[1133554]]'
hide p4
hide p1007
$ update_portrait('st053_01 2', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 5)
c43 '[textdict[1133555]]'
hide p4
hide p1007
$ update_portrait('st053_01 2', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1133556]]'
hide p1007
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133557]]'
hide p2
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 2', 'p1007', [l(-12), light, flip], 6)
play sfx2 "other_7021.ogg"
c10071 '[textdict[1133558]]'
hide p1007
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
c7401 '[textdict[1133559]]'
hide p1
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133560]]'
hide p1007
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
c7401 '[textdict[1133561]]'
hide p1007
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
c7401 '[textdict[1133562]]'
hide p1007
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1133563]]'
hide p1
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 5)
c43 '[textdict[1133564]]'
hide p4
play sfx2 "other_7086.ogg"
c0 '[textdict[1133565]]'
play music "ed7120.ogg"
$ update_portrait('st053_01 5', 'p1007', [l(-12), light, flip], 6)
c10071 '[textdict[1133566]]'
hide p1007
$ update_portrait('st053_01 5', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
c23 '[textdict[1133567]]'
hide p2
hide p1007
$ update_portrait('st053_01 5', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc004_01 6', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li02.ogg"
c43 '[textdict[1133568]]'
hide p4
hide p1007
$ update_portrait('st053_01 5', 'p1007', [l(-12), dark, flip], 6)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1133569]]'
hide p1007
hide p4
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
c21 '[textdict[1133570]]' (what_size=(gui.text_size*1.4))
hide p4
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 5)
play sfx2 "other_7057.ogg"
play sfxvoice "bcv_oc004_hurt_02.ogg"
c43 '[textdict[1133571]]' (what_size=(gui.text_size*1.2)) with shake
hide p4
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 5)
c43 '[textdict[1133572]]'
hide p4
hide p2
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1133573]]'
return