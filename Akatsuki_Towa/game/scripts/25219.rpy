label avg25219:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210759]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6015.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210760]]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210761]]'
return