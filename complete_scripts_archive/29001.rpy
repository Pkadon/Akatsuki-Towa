label avg29001:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[textdict[1216000]]'
c0 '[textdict[1216001]]'
c0 '[textdict[1216002]]'
c0 '[textdict[1216003]]'
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[textdict[1216004]]'
hide p209
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1216005]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1216006]]'
hide p1
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[textdict[1216007]]'
hide p209
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
c23 '[textdict[1216008]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1216009]]'
hide p1
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[textdict[1216010]]'
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[textdict[1216011]]'
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[textdict[1216012]]'
menu:
    extend ""
    "[textdict[1216013]]":
        call avg29002
    "[textdict[1216014]]":
        call avg29003
return