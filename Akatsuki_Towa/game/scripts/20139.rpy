label avg20139:

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1003722)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1003723)]'
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
c5533 '[convertstrid(1003724)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7020.ogg"
c23 '[convertstrid(1003725)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc042_01 1', 'p641', [l_entrance(-19), light, flip], 6)
c6411 '[convertstrid(1003726)]'
$ update_portrait('sc042_01 1', 'p641', [l(-19), light, flip], 6)
c6411 '[convertstrid(1003727)]'
$ update_portrait('sc042_01 1', 'p641', [l_exit(-19), light, flip], 6)
c6411 '[convertstrid(1003728)]'
hide p641
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[convertstrid(1003729)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1003730)]'
return