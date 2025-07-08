label avg10347:
stop music

play music "ed7302.ogg"
scene avg_bg_031
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1131282]]'
hide p1
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_hurt_01.ogg"
c21 '[textdict[1131283]]'
hide p1
hide p2
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li20.ogg"
c43 '[textdict[1131284]]'
hide p2
hide p4
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
c31 '[textdict[1131285]]'
hide p3
hide p4
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131286]]'
hide p1004
hide p4
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131287]]'
hide p4
hide p1004
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1131288]]'
hide p1
hide p1004
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131289]]'
hide p1
hide p1004
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li20.ogg"
c43 '[textdict[1131290]]' (what_size=(gui.text_size*1.2))
hide p1004
hide p4
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131291]]'
hide p4
hide p1004
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1131292]]'
hide p2
hide p1004
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[textdict[1131293]]'
hide p1004
hide p3
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131294]]'
hide p1004
hide p3
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131295]]'
hide p3
hide p1004
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na12.ogg"
c13 '[textdict[1131296]]' (what_size=(gui.text_size*1.4)) with shake
hide p1004
hide p1
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
c10201 '[textdict[1131297]]' (what_size=(gui.text_size*1.4))
hide p1
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 2', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1131298]]'
hide p1
hide p236
$ update_portrait('st037_01 2', 'p236', [l(-10), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1131299]]'
hide p236
hide p2
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1131300]]'
hide p2
hide p236
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 6)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[textdict[1131301]]'
hide p3
hide p236
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 6)
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro22.ogg"
c33 '[textdict[1131302]]'
hide p3
hide p236
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 6)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[textdict[1131303]]'
hide p236
hide p4
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na18.ogg"
c11 '[textdict[1131304]]'
hide p4
hide p1
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li10.ogg"
c43 '[textdict[1131305]]'
hide p1
hide p4
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
c10041 '[textdict[1131306]]'
hide p4
hide p1004
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 6)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[textdict[1131307]]'
hide p1004
hide p4
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
c10211 '[textdict[1131308]]' (what_size=(gui.text_size*1.2))
hide p4
c0 '[textdict[1131309]]' (what_size=(gui.text_size*1.4))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1131310]]'
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131311]]'
hide p1
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1131312]]'
hide p2
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1131313]]'
hide p1
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li03.ogg"
c43 '[textdict[1131314]]'
hide p4
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[textdict[1131315]]'
hide p2
hide p4
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
c10211 '[textdict[1131316]]'
hide p4
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_die_01.ogg"
c21 '[textdict[1131317]]' (what_size=(gui.text_size*1.4))
hide p4
hide p2
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1131318]]'
hide p2
hide p1
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li26.ogg"
c41 '[textdict[1131319]]'
hide p1
hide p4
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[textdict[1131320]]'
hide p4
hide p3
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1131321]]' (what_size=(gui.text_size*1.2))
hide p3
hide p4
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro18.ogg"
c33 '[textdict[1131322]]'
hide p3
hide p4
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131323]]'
hide p4
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1131324]]'
hide p1
hide p4
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1131325]]'
hide p4
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[textdict[1131326]]'
hide p4
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
c21 '[textdict[1131327]]'
hide p1
hide p2
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131328]]'
hide p1
hide p2
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131329]]'
hide p1
hide p2
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1131330]]'
hide p2
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 2', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1131331]]'
hide p236
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1131332]]'
hide p236
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
c41 '[textdict[1131333]]'
hide p1
hide p4
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro16.ogg"
c33 '[textdict[1131334]]'
hide p4
hide p3
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
c41 '[textdict[1131335]]'
hide p4
hide p3
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch14.ogg"
c21 '[textdict[1131336]]' (what_size=(gui.text_size*1.2))
hide p3
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1131337]]' (what_size=(gui.text_size*1.4))
hide p1
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[textdict[1131338]]' (what_size=(gui.text_size*1.8))
return