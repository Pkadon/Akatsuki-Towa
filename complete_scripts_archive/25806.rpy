label avg25806:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[textdict[1211265]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211266]]'
return