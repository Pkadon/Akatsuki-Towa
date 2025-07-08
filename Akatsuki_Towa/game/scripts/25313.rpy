label avg25313:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211202]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211203]]'
hide p1
c20153 '[textdict[1211204]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7057.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1211205]]'
return