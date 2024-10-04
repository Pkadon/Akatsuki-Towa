label avg25047:
stop music

scene placeholderbackground
with fade
show uc001_02 3 as c2002portrait at centerpos(6), zorder 5
c20023 '[textdict[1210120]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c2002portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210121]]'
hide c2portrait
show uc001_02 2 as c2002portrait at centerpos(6), zorder 5
c20023 '[textdict[1210122]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25048
    "[textdict[1215000]]":
        call avg25000
return