label avg10348:

$ play_music("ed7567.ogg")
scene avg_bg_031
$ update_narrator('c43')
window show
with fade_in
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
c43 '[convertstrid(1131284)]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[convertstrid(1131285)]'
hide p3
hide p4
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
$ update_narrator('c10041')
with fade
c10041 '[convertstrid(1131286)]'
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
c10041 '[convertstrid(1131287)]'
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1131288)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131289)]'
hide p1
$ update_portrait('oc004_01 3', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[convertstrid(1131290)]' (what_size=(gui.text_size*1.2))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), l_shake, light, flip], 6)
c10041 '[convertstrid(1131291)]'
hide p4
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1131292)]'
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1131293)]'
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
c10041 '[convertstrid(1131294)]'
$ update_portrait('sc046_01 3', 'p1004', [l_exit(-5), light, flip], 6)
play sfx2 "other_7057.ogg"
c10041 '[convertstrid(1131295)]' with shake
hide p1004
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131296)]' (what_size=(gui.text_size*1.4))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c10201 '[convertstrid(1131297)]' (what_size=(gui.text_size*1.4))
$ update_portrait('st037_01 2', 'p236', [l_entrance(-10), l_shake, light, flip], 6)
c2361 '[convertstrid(1131298)]'
hide p1
$ update_portrait('st037_01 2', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1131299)]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
c2361 '[convertstrid(1131300)]'
hide p2
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1131301)]'
$ update_portrait('oc003_01 3', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1131302)]'
hide p236
hide p3
$ update_narrator('c43')
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
with fade
$ update_portrait('oc004_01 3', 'p4', [r_midback(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[convertstrid(1131303)]'
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l_exit(-2), light, flip], 6)
c11 '[convertstrid(1131304)]'
hide p1
hide p4
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 16', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1131305)]'
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l_entrance(-5), light, flip], 6)
c10041 '[convertstrid(1131306)]'
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1131307)]'
hide p1004
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
c10211 '[convertstrid(1131308)]' (what_size=(gui.text_size*1.2))
hide p4
play sfx2 "other_7088.ogg"
c0 '[convertstrid(1131309)]' (what_size=(gui.text_size*1.4))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131310)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131311)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131312)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131313)]'
hide p2
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
c43 '[convertstrid(1131314)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1131315)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c10211 '[convertstrid(1131316)]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
c21 '[convertstrid(1131317)]' (what_size=(gui.text_size*1.4))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131318)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131319)]'
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r_entrance(-6), light], 6)
c33 '[convertstrid(1131320)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l_midback(-5), light, flip], 6)
c41 '[convertstrid(1131321)]' (what_size=(gui.text_size*1.2))
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r_exit(-6), light], 6)
c33 '[convertstrid(1131322)]'
hide p3
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1131323)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131324)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131325)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131326)]'
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131327)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131328)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131329)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131330)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
c2361 '[convertstrid(1131331)]'
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
c2361 '[convertstrid(1131332)]'
hide p1
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1131333)]'
hide p236
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
c33 '[convertstrid(1131334)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131335)]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1131336)]' (what_size=(gui.text_size*1.2))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131337)]' (what_size=(gui.text_size*1.4))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7007.ogg"
c31 '[convertstrid(1131338)]' (what_size=(gui.text_size*1.8)) with shake
return