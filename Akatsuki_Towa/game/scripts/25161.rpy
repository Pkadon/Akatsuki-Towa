label avg25161:

stop music
scene placeholderbackground
$ update_narrator('c20153')
window show
with fade_in
c20153 '[convertstrid(1210522)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210523)]'
hide p2
c20153 '[convertstrid(1210524)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[convertstrid(1210525)]'
hide p2
c20153 '[convertstrid(1210526)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210527)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210528)]'
return