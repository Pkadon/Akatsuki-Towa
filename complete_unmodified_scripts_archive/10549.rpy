label avg10549:

$ play_music("ED6102.ogg")
scene avg_bg_105
$ update_narrator('c5531')
window show
with fade_in
play sfx2 "other_7085.ogg"
c5531 '[convertstrid(1153492)]'
$ update_portrait('oc004_01 23', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1153493)]'
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l_entrance(-24), light, flip], 6)
c71 '[convertstrid(1153494)]'
hide p4
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1153495)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153496)]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1153497)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153498)]'
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153499)]'
$ update_portrait('oc007_01 1', 'p7', [l(-24), l_shake, light, flip], 6)
c71 '[convertstrid(1153500)]'
hide p3
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153501)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153502)]'
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153503)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc007_01 3', 'p7', [l(-24), light, flip], 6)
play sfxvoice "avg_vocal_ar02.ogg"
c71 '[convertstrid(1153504)]' with shake
hide p2
$ update_portrait('oc007_01 3', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1153505)]'
hide p3
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1153506)]'
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 3', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153507)]' with shake
hide p4
$ update_portrait('oc007_01 3', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153508)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
play sfxvoice "avg_vocal_ar08b.ogg"
c71 '[convertstrid(1153509)]'
$ update_portrait('oc007_01 4', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153510)]'
hide p1
$ update_portrait('oc007_01 4', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153511)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153512)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153513)]'
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1153514)]'
$ update_portrait('oc007_01 1', 'p7', [l_exit(-24), light, flip], 6)
play sfx2 "other_7085.ogg"
c71 '[convertstrid(1153515)]'
hide p7
hide p2
$ update_narrator('c31')
with fade
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[convertstrid(1153516)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1153517)]'
return