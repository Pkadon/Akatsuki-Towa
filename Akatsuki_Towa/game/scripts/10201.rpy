label avg10201:

$ play_music("ed7151.ogg")
scene avg_bg_071
$ update_portrait('st028_02 4', 'p664', [l(8), light, flip], 6)
$ update_narrator('c6641')
window show
with fade_in
c6641 '[convertstrid(1001032)]'
$ update_portrait('st028_02 4', 'p664', [l(8), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1004279)]'
hide p664
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1004280)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004281)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[convertstrid(1004282)]'
hide p3
$ update_portrait('st028_02 2', 'p664', [l(8), light, flip], 6)
play sfx2 "other_7085.ogg"
c6641 '[convertstrid(1000306)]'
hide p664
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1004284)]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1004285)]'
hide p3
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('st028_02 4', 'p666', [l(8), light, flip], 6)
c6661 '[convertstrid(1004286)]'
hide p666
hide p1
play sfx2 "other_7022.ogg"
c0 '[convertstrid(1004287)]'
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
c31 '[convertstrid(1004288)]'
hide p3
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004289)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc003_01 9', 'p3', [r(-6), r_shake, light], 6)
play sfxvoice "avg_vocal_ro15.ogg"
c33 '[convertstrid(1004290)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch22.ogg"
c21 '[convertstrid(1004291)]'
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
c43 '[convertstrid(1004292)]'
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004293)]'
return