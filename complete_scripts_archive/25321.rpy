label avg25321:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1211241)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1211242)]'
return