label avg25302:

stop music
scene placeholderbackground
$ update_narrator('c20273')
window show
with fade_in
play sfx2 "fight_6024.ogg"
c20273 '[convertstrid(1211164)]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1211165)]'
hide p2
c20273 '[convertstrid(1211166)]'
return