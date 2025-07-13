label avg25037:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210095]]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210096]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6024.ogg"
c23 '[textdict[1210097]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25038
    "[textdict[1215000]]":
        call avg25026
return