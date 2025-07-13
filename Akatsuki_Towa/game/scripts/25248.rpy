label avg25248:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6025.ogg"
c23 '[textdict[1210906]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210907]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210908]]'
return