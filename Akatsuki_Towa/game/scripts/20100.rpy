label avg20100:

play music "ed7104.ogg"
scene avg_bg_037
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1004850)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfx2 "other_7044.ogg"
c13 '[convertstrid(1004851)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
play sfx2 "other_7047.ogg"
c6871 '[convertstrid(1004852)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004853)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
play sfx2 "other_7004.ogg"
c6871 '[convertstrid(1004854)]'
hide p1
play sfx2 "other_7064.ogg"
c0 '[convertstrid(1004855)]'
c6881 '[convertstrid(1004856)]'
c6881 '[convertstrid(1004857)]'
c5053 '[convertstrid(1004858)]'
play sfx2 "other_7085.ogg"
c6883 '[convertstrid(1004859)]'
$ update_narrator('c6871')
with fade
c6871 '[convertstrid(1004860)]'
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1004861)]'
return