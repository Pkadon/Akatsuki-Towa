label avg25117:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1210344)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1210346)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c13 '[convertstrid(1210347)]'
return