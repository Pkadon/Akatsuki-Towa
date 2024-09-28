label avg25111:
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210329]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210330]]'
play sfxvoice "avg_vocal_ch31.ogg"
hide c1portrait
show oc002_01 7 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210331]]'
return