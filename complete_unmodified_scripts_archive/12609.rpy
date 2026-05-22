label avg12609:

$ play_music("ED6302.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1161340)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1161341)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1161342)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161343)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1161344)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1161345)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161346)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1161347)]'
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161348)]'
hide p3
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1161349)]'
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1161350)]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161351)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li11.ogg"
c43 '[convertstrid(1161352)]'
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161353)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1161354)]'
hide p2
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161355)]'
$ update_portrait('oc003_01 13', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1161356)]'
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[convertstrid(1161357)]'
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r_midback(-5), light], 6)
play sfx2 "fight_6010.ogg"
c43 '[convertstrid(1161358)]'
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161359)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161360)]'
hide p4
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1161361)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1161362)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161363)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1161364)]'
$ update_portrait('oc002_01 5', 'p2', [r_exit(-3), light], 6)
play sfx2 "other_7085.ogg"
c23 '[convertstrid(1161365)]'
hide p2
hide p3
$ update_portrait('oc004_01 13', 'p4', [l_midback(-5), light, flip], 6)
c41 '[convertstrid(1161366)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[convertstrid(1161367)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1161368)]'
stop music
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
play sfx2 "other_7045.ogg"
c12601 '[convertstrid(1161369)]' (what_size=(gui.text_size*1.25)) with shake
$ play_music("ed7511.ogg")
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1161370)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161371)]' (what_size=(gui.text_size*1.25))
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
play sfx2 "other_7087.ogg"
c43 '[convertstrid(1161372)]' (what_size=(gui.text_size*1.5)) with shake
hide p2
$ update_portrait('oc004_01 15', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 20', 'p3', [l(-6), l_shake, light, flip], 6)
c31 '[convertstrid(1161373)]'
$ update_portrait('oc003_01 20', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
play sfx2 "other_7087.ogg"
c43 '[convertstrid(1161374)]' with shake
hide p4
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfx2 "other_7080.ogg"
c13 '[convertstrid(1161375)]'
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161376)]'
return