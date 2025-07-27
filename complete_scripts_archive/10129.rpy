label avg10129:

play music "ed7104.ogg"
scene avg_bg_019
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007286)]'
$ update_portrait('oc001_01 22', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7060.ogg"
c11 '[convertstrid(1007287)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7020.ogg"
c11 '[convertstrid(1007288)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r_entrance(-3), light], 5)
c23 '[convertstrid(1007289)]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 19', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007290)]'
$ update_portrait('oc001_01 19', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 19', 'p2', [r_exit(-3), light], 5)
play sfx2 "other_7085.ogg"
c23 '[convertstrid(1007291)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfx2 "fight_6021.ogg"
play sfxvoice "avg_vocal_na21.ogg"
c11 '[convertstrid(1007292)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 5)
play sfxvoice "avg_vocal_ch18.ogg"
c23 '[convertstrid(1007293)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007294)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1007295)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007296)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1007297)]'
return