label avg10357:

play music "ed7161.ogg"
scene avg_bg_050
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 14', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1131661)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131662)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131663)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131664)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1131665)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
c10303 '[convertstrid(1131666)]'
c10313 '[convertstrid(1131667)]'
play sfx2 "other_7007.ogg"
c10303 '[convertstrid(1131668)]' (what_size=(gui.text_size*1.3))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1131669)]'
hide p2
hide p1
play sfx2 "other_7012.ogg"
c0 '[convertstrid(1131670)]' with shake
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[convertstrid(1131671)]' with shake
hide p2
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[convertstrid(1131672)]'
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131673)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[convertstrid(1131675)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[convertstrid(1131676)]'
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1131677)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1131678)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131679)]'
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c21 '[convertstrid(1131680)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1131681)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131682)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1131683)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c21 '[convertstrid(1131684)]'
return